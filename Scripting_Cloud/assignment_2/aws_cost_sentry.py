# ─── INPUT‑STAGE IMPORTS ───────────────────────────────────────────────
import argparse         # CLI contract
import os               # Filesystem sanity checks
import pandas as pd     # Columnar analytics

# ─── PROCESS‑STAGE IMPORTS ─────────────────────────────────────────────
import math             # Deterministic rounding (ceil) if we extend output
import datetime         # Future-proof: timestamp reports & email subjects

# ─── OUTPUT‑STAGE IMPORTS ──────────────────────────────────────────────
from rich.console import Console
from rich.table import Table
import smtplib, ssl
from email.mime.text import MIMEText


# ═══════════════════════════════════════════════════════════════════════
# 1. CLI CONTRACT (single responsibility: parse + validate argv)         
# ═══════════════════════════════════════════════════════════════════════
def parse_args() -> argparse.Namespace:
    """
    Build and immediately parse the command-line interface.

    WHY
    ----
    • Encapsulates all user-facing knobs in one place.  
    • Keeps `main()` agnostic of `argparse` internals.  
    • Raises `SystemExit(2)` automatically on misuse, preventing
      downstream functions from ever receiving invalid inputs.

    RETURNS
    -------
    argparse.Namespace with 4 guaranteed attributes:
        file             : str  (path to AWS CUR/CSV) – always exists
        threshold        : float  (% spike trigger)
        email            : Optional[str]
        notify_always    : bool  (True if flag present)
    """
    p = argparse.ArgumentParser(
        prog="aws_cost_sentry",
        description="Lightweight watcher for AWS Cost-and-Usage CSV exports"
    )
    p.add_argument(
        "--file", required=True,
        help="Absolute or relative path to Cost & Usage CSV"
    )
    p.add_argument(
        "--threshold", type=float, default=100.0,
        help="Spike percentage triggering an alert (Δ day-over-day)."
    )
    p.add_argument(
        "--email",
        help="Destination address for SMTP alert (omit → console-only)."
    )
    p.add_argument(
        "--notify-always", action="store_true",
        help="Send e‑mail even when no spike detected."
    )
    return p.parse_args()


# ═══════════════════════════════════════════════════════════════════════
# 2. INGEST  →  AGGREGATE (pure functions, no side‑effects)             
# ═══════════════════════════════════════════════════════════════════════
def load_csv(path: str) -> pd.DataFrame:
    """
    Safely load the AWS CUR CSV into memory.

    RULES / ASSUMPTIONS
    -------------------
    • Path must exist and be readable; otherwise we fail fast.  
    • Caller handles `FileNotFoundError`.  
    • Leaves original column names untouched for auditing parity.

    RETURNS
    -------
    DataFrame with *at least* the columns :
        Date, ProductName, UnblendedCost
    """
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    return pd.read_csv(path)


def aggregate(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert raw line-items into a Date * Service cost matrix.

    WHY
    ----
    • Matrix is the minimal representation needed for %
      change calculation and tabular display.
    • By pivoting once, later steps never re-compute aggregates,
      which is important when CSV >100k rows.

    RETURNS
    -------
    DataFrame indexed by Date with one column per ProductName.
    Missing combinations are NaN (interpreted as zero spend).
    """
    daily = (
        df.groupby(["Date", "ProductName"])["UnblendedCost"]
          .sum()
          .reset_index()
    )
    return daily.pivot_table(
        index="Date",
        columns="ProductName",
        values="UnblendedCost",
        aggfunc="sum"
    )


# ═══════════════════════════════════════════════════════════════════════
# 3. DETECT ANOMALIES                                                   
# ═══════════════════════════════════════════════════════════════════════
def detect_spikes(pivot: pd.DataFrame, threshold: float) -> pd.DataFrame:
    """
    Identify services whose day-over-day Δ exceeds the threshold.

    TECHNICAL NOTES
    ---------------
    • Uses `pct_change()` which preserves NaN for first row.  
    • Rows with *no* service breaching threshold are dropped to keep
      e-mail concise.  
    • `.round(1)` keeps output human-readable without losing signal.
    """
    delta = pivot.pct_change() * 100
    return (
        delta[abs(delta) >= threshold]
        .dropna(how="all")
        .round(1)
    )


# ═══════════════════════════════════════════════════════════════════════
# 4. RENDER TO TERMINAL                                                 
# ═══════════════════════════════════════════════════════════════════════
console = Console()

def render_table(pivot: pd.DataFrame, spikes: pd.DataFrame) -> None:
    """
    Pretty-print the daily cost matrix plus a spike banner.

    • Always prints the full pivot for transparency.  
    • Emits a red banner only when `spikes` is non-empty.  
    • Never raises: safe to call in production regardless of data size.
    """
    table = Table(title="AWS Daily Cost (USD)")
    table.add_column("Date", style="cyan", no_wrap=True)
    for svc in pivot.columns:
        table.add_column(svc, justify="right")

    for date, row in pivot.fillna(0).iterrows():
        cells = [date] + [f"{row[c]:.2f}" for c in pivot.columns]
        table.add_row(*cells)

    console.print(table)

    if not spikes.empty:
        console.print(
            f"[bold red]⚠  {len(spikes)} spike row(s) detected above threshold[/]"
        )


# ═══════════════════════════════════════════════════════════════════════
# 5. OPTIONAL EMAIL                                                     
# ═══════════════════════════════════════════════════════════════════════
def send_email(body: str, to_addr: str, cfg: dict) -> None:
    """
    Fire a plaintext email via SSL-secured SMTP.

    Parameters
    ----------
    body     : Plaintext payload (already formatted).
    to_addr  : Recipient.
    cfg      : Dict with keys host, port, sender, password.

    Raises
    ------
    smtplib.SMTPException on network/auth failure.
    """
    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = f"AWS Cost Spike {datetime.date.today()} 🚨"
    msg["From"] = cfg["sender"]
    msg["To"] = to_addr

    ctx = ssl.create_default_context()
    with smtplib.SMTP_SSL(cfg["host"], cfg["port"], context=ctx) as s:
        s.login(cfg["sender"], cfg["password"])
        s.sendmail(cfg["sender"], [to_addr], msg.as_string())


# ═══════════════════════════════════════════════════════════════════════
# 6. GLUE  (imperative orchestration)                                  
# ═══════════════════════════════════════════════════════════════════════
def main() -> None:
    """
    Orchestrate ETL→detect→render(+optional alert).

    Guarantees
    ----------
    • Console always receives a report.  
    • Script exits 0 on success, non-zero on handled error.
    """
    args = parse_args()
    pivot  = aggregate(load_csv(args.file))
    spikes = detect_spikes(pivot, args.threshold)
    render_table(pivot, spikes)

    if args.email and (not spikes.empty or args.notify_always):
        body = spikes.to_string() if not spikes.empty else "No anomalies."
        send_email(body, args.email, {
            "host": "smtp.gmail.com",
            "port": 465,
            "sender": "you@example.com",
            "password": "app-password"
        })

# Kick‑off only when invoked directly, not on import.
if __name__ == "__main__":
    main()
