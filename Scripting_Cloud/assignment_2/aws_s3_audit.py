"""
Name: Talent Nyota
Date: 18-07-2025

Program Description
-------------------
This companion script audits every S3 bucket in an AWS account and:

1. Lists all buckets via boto3.
2. Checks three "doors" to the outside world:
     * Block-Public-Access configuration
     * Bucket policy (AllUsers / AuthenticatedUsers)
     * ACL grants to the same global groups
3. Marks any bucket that fails those checks as **public**.
4. Optionally seals risky buckets with --fix by:
     * Enabling all four BPA flags
     * Attaching a deny-all bucket policy
5. Renders a colored Rich table and summarizes the risk count.

The logic imitates the manual checklist I followed while studying the
Capital-One S3 breach case-study and practicing IAM policy crafting.
By writing the detection and remediation code (instead of using
AWS Config rules), I reinforced how ACLs, bucket policies, and BPA
interact—knowledge crucial for future cloud-security roles.

-----------------------------------------------------------------------
How to Test  (two minutes, no real AWS required)
-----------------------------------------------------------------------
1. Install dev deps in a fresh venv (already done for grading):

       pip install boto3 rich "moto[s3]" pytest

2. Start Moto's local S3 server in tab 1:

       python -m moto.server -p 5000

3. In tab 2 (same venv) point boto3 at Moto & seed two buckets:

       export AWS_ENDPOINT_URL=http://127.0.0.1:5000
       export AWS_ACCESS_KEY_ID=fake
       export AWS_SECRET_ACCESS_KEY=fake

       python - <<'PY'
       import boto3
       s3 = boto3.client("s3", region_name="us-east-1")
       s3.create_bucket(Bucket="public-bkt")          # public by default
       s3.create_bucket(Bucket="private-bkt")
       s3.put_public_access_block(
           Bucket="private-bkt",
           PublicAccessBlockConfiguration=dict(
               BlockPublicAcls=True, IgnorePublicAcls=True,
               BlockPublicPolicy=True, RestrictPublicBuckets=True))
       print("Seeded Moto with one public and one private bucket.")
       PY

4. Run the audit CLI:

       python aws_s3_audit.py --region us-east-1

   Expected table -> **public-bkt** in red, **private-bkt** in green.

5. Remediate and verify:

       python aws_s3_audit.py --region us-east-1 --fix
       python aws_s3_audit.py --region us-east-1 --quiet   # now green/0

-----------------------------------------------------------------------
How to Test  (real AWS, requires credentials)
-----------------------------------------------------------------------
1. Configure a profile:

       aws configure --profile mylab

2. Audit only:

       python aws_s3_audit.py --profile mylab --region us-east-1

3. Seal risky buckets (irreversible without manual policy edit):

       python aws_s3_audit.py --profile mylab --region us-east-1 --fix
"""
#!/usr/bin/env python
from __future__ import annotations
"""
aws_s3_audit.py
Audit all S3 buckets for unintended public access and—if requested—seal them.

Execution path
==============
CLI → boto3 client → list_buckets → is_public → (optional) seal_bucket → render
"""


# ─── INPUT‑STAGE IMPORTS ──────────────────────────────────────────────
import argparse               # Flag‑based user contract
import os                     # Read AWS_PROFILE / AWS_REGION fallbacks

# ─── PROCESS‑STAGE IMPORTS ────────────────────────────────────────────
import boto3
from botocore.exceptions import ClientError
import datetime
from typing import List, Dict

# ─── OUTPUT‑STAGE IMPORTS ─────────────────────────────────────────────
from rich.console import Console
from rich.table import Table


console = Console()

# ═════════════════════════════════════════════════════════════════════
# 1. CLI CONTRACT                                                      
# ═════════════════════════════════════════════════════════════════════
def parse_args() -> argparse.Namespace:
    """
    Build and parse the command‑line interface.

    WHY
    ---
    • Centralises user-facing knobs: profile, region, --fix, --quiet.  
    • Unit‑testable: individual tests can feed custom argv.  
    • Keeps `main()` declarative—no argparse noise mixed with business logic.

    RETURNS
    -------
    argparse.Namespace with attributes:
        profile  : Optional[str]   AWS named profile
        region   : str            AWS region ("us-east-1" fallback)
        fix      : bool           Whether to remediate risky buckets
        quiet    : bool           Hide compliant rows in Rich table
    """
    p = argparse.ArgumentParser(
        prog="aws_s3_audit",
        description="Find S3 buckets with public ACL/policy; optionally seal them."
    )
    p.add_argument("--profile", help="AWS named profile (overrides env[AWS_PROFILE]).")
    p.add_argument("--region",
                   default=os.getenv("AWS_REGION", "us-east-1"),
                   help="AWS region (default env[AWS_REGION] or us‑east‑1).")
    p.add_argument("--fix", action="store_true",
                   help="Apply Block‑Public‑Access + deny‑all bucket policy.")
    p.add_argument("--quiet", action="store_true",
                   help="Suppress OK rows; show only risky buckets.")
    return p.parse_args()


# ═════════════════════════════════════════════════════════════════════
# 2. DATA ACQUISITION (pure boto3 wrappers)                            
# ═════════════════════════════════════════════════════════════════════
def s3_client(profile: str | None, region: str):
    """
    Return a boto3 S3 client in the requested credential context.

    WHY
    ---
    • Abstracts profile/region wiring away from higher‑level functions.  
    • Allows dependency injection during unit tests (moto).
    """
    session = boto3.Session(profile_name=profile) if profile else boto3.Session()
    return session.client("s3", region_name=region)


def list_buckets(s3) -> List[Dict]:
    """
    List all buckets visible to the caller.

    RETURNS
    -------
    List[dict] with keys Name, CreationDate.
    """
    return s3.list_buckets()["Buckets"]


# ═════════════════════════════════════════════════════════════════════
# 3. ANALYSIS                                                          
# ═════════════════════════════════════════════════════════════════════
def is_public(s3, bucket: str) -> bool:
    """
    Heuristically decide if *bucket* is publicly accessible.

    Checks
    ------
    1.  Block-Public-Access configuration (all 4 flags must be True).  
    2.  Bucket policy containing 'AllUsers' or 'AuthenticatedUsers'.  
    3.  ACL grants to the same global groups.

    RETURNS
    -------
    True  → risky; bucket might leak data  
    False → compliant

    NOTES
    -----
    • Omits object-level ACL inspection for performance.  
    • Any AWS errors other than 'not configured' bubble upward.
    """
    # 1) Public‑access block
    try:
        bpa = s3.get_public_access_block(Bucket=bucket)["PublicAccessBlockConfiguration"]
        if not all(bpa.values()):
            return True
    except ClientError as e:
        if e.response["Error"]["Code"] != "NoSuchPublicAccessBlockConfiguration":
            raise
        return True  # No config at all = risky

    # 2) Bucket policy
    try:
        pol = s3.get_bucket_policy(Bucket=bucket)["Policy"]
        if "AllUsers" in pol or "AuthenticatedUsers" in pol:
            return True
    except ClientError as e:
        if e.response["Error"]["Code"] != "NoSuchBucketPolicy":
            raise

    # 3) ACL grants
    acl = s3.get_bucket_acl(Bucket=bucket)
    for g in acl["Grants"]:
        uri = g["Grantee"].get("URI", "")
        if uri.endswith(("Global/AllUsers", "Global/AuthenticatedUsers")):
            return True
    return False


# ═════════════════════════════════════════════════════════════════════
# 4. REMEDIATION                                                       
# ═════════════════════════════════════════════════════════════════════
_BLOCK_POLICY_TEMPLATE = {
    "Version": "2012-10-17",
    "Statement": [{
        "Sid": "DenyAll",
        "Effect": "Deny",
        "Principal": "*",
        "Action": "s3:*",
        "Resource": []  # Filled dynamically
    }]
}

def seal_bucket(s3, bucket: str) -> None:
    """
    Force the bucket to private by:
    1. Enabling *all four* Block-Public-Access flags.
    2. Attaching a deny-all bucket policy.

    Raises
    ------
    ClientError  on any AWS failure (caller decides to continue/abort).
    """
    console.log(f"🔒  Sealing {bucket}")
    s3.put_public_access_block(
        Bucket=bucket,
        PublicAccessBlockConfiguration=dict(
            BlockPublicAcls=True,
            IgnorePublicAcls=True,
            BlockPublicPolicy=True,
            RestrictPublicBuckets=True,
        ),
    )

    policy = _BLOCK_POLICY_TEMPLATE.copy()
    resources = [
        f"arn:aws:s3:::{bucket}",
        f"arn:aws:s3:::{bucket}/*",
    ]
    policy["Statement"][0]["Resource"] = resources
    s3.put_bucket_policy(Bucket=bucket, Policy=str(policy))


# ═════════════════════════════════════════════════════════════════════
# 5. PRESENTATION                                                      
# ═════════════════════════════════════════════════════════════════════
def render(findings: List[Dict], quiet: bool) -> None:
    """
    Render audit results as a Rich table.

    Parameters
    ----------
    findings : list of dict(name, public, created)
    quiet    : if True, omit NON public rows (speeds CI logs)
    """
    table = Table(title="S3 Public-Access Audit")
    table.add_column("Bucket", style="cyan")
    table.add_column("Public?", justify="center")
    table.add_column("Created", justify="right")

    for row in findings:
        if quiet and not row["public"]:
            continue
        style = "bold red" if row["public"] else "green"
        table.add_row(row["name"], f"[{style}]{row['public']}[/]", str(row["created"]))

    console.print(table)


# ═════════════════════════════════════════════════════════════════════
# 6. GLUE                                                              
# ═════════════════════════════════════════════════════════════════════
def main() -> None:
    """
    Full orchestration:

    1. Parse CLI → establish boto3 client.
    2. Enumerate *every* bucket.
    3. Classify each bucket's public status.
    4. Optionally remediate anything risky (--fix).
    5. Pretty-print summary; exit 0 always (non-compliance ≠ failure).

    Exit codes
    ----------
    0 : Script ran to completion; use output for compliance gating.
    """
    args = parse_args()
    s3   = s3_client(args.profile, args.region)

    findings = []
    for b in list_buckets(s3):
        name   = b["Name"]
        public = is_public(s3, name)
        findings.append(dict(name=name,
                             public=public,
                             created=b["CreationDate"]))

        if public and args.fix:
            try:
                seal_bucket(s3, name)
            except ClientError as e:
                console.log(f"[red]Failed to seal {name}: {e}[/]")

    render(findings, args.quiet)
    num_risky = sum(1 for f in findings if f["public"])
    console.print(
        f"[bold yellow]{num_risky}[/] public bucket(s) out of {len(findings)} total."
    )


if __name__ == "__main__":
    main()
