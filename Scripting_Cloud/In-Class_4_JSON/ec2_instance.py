# Author: Talent Nyota
# Modified: July 3, 2025
# Description:
# This script is a small console program that helps you pick AWS EC2 instance
# types that meet a CPU‑core and memory range you give on the keyboard.
#
# What it does – step by step
#   1. Reads a very large JSON file that lists every EC2 instance size.
#   2. Turns each JSON record into an Ec2Instance object with clean numbers.
#   3. Asks you for your minimum / maximum vCPUs and GiB of memory.
#   4. Prints an easy‑to‑read table of only the instance types that match.


import json
import re # re → built-in “regular-expression” tools for finding patterns inside text
from typing import List, Optional 
# typing → lets us write hints like List[int] or Optional[float] so readers (and IDEs)
# know what kinds of values a variable should hold


class Ec2Instance:
    """Represents one AWS EC2 instance type with tidy, usable data.

    AWS sometimes puts extra words in the *vcpu* and *memory* fields.  The
    constructor strips out that noise so we always end up with:
      • `self.vcpu`   → an **int** (ex: 8)
      • `self.memory` → a **float** in GiB (ex: 15.0)
    Anything we cannot clean up causes that row to be skipped with a warning.
    """

    # Pre-built regex that retrieves the FIRST number it finds in a string.
    # Works for “32”, “0.5”, “768.0”, etc.
    _MEM_RE = re.compile(r"(\d*\.?\d+)")

    def __init__(
        self,
        name_value: str,
        vcpu_value,
        memory_value,
        storage_value: str,
        bandwidth_value: str,
        availability_value: str,
    ) -> None:
        """Turn raw JSON values into neat Python attributes.

        Args:
            name_value: The AWS instance type string (for example "t3.micro").
            vcpu_value: Can be a number *or* a string that starts with a
                number.  Always stored as an **int**.
            memory_value: Same idea – could be 8 or "0.5 GiB".  Always stored
                as a **float**.
            storage_value: Text from AWS about local storage ("EBS only", etc.).
            bandwidth_value: Text about network speed.
            availability_value: AWS availability/burst info.
        """
        self.name = str(name_value)

        # Clean up vCPU field
        if isinstance(vcpu_value, str):
            digits = re.match(r"(\d+)", vcpu_value)
            if not digits:
                raise ValueError(f"Bad vCPU field: {vcpu_value!r}")
            self.vcpu = int(digits.group(1))
        else:
            self.vcpu = int(vcpu_value)

        # Clean up memory field
        if isinstance(memory_value, str):
            match = self._MEM_RE.match(memory_value)
            if not match:
                raise ValueError(f"Bad memory field: {memory_value!r}")
            self.memory = float(match.group(1))
        else:
            self.memory = float(memory_value)

        # The rest are already strings we can keep as‑is
        self.storage = storage_value
        self.bandwidth = bandwidth_value
        self.availability = availability_value

    # ───────────────────────────────────────── helper methods ─────────────────────────────────────────

    def display(self) -> str:
        """Return a short, human‑friendly summary of this instance."""
        return f"{self.name} ({self.vcpu} vCPUs, {self.memory}\u00A0GiB, {self.storage})"

    def __str__(self) -> str:  # noqa: Dunder
        """When you call *print(instance)* you only get the instance type."""
        return self.name

    def to_json(self) -> str:
        """Return the object as pretty JSON (handy for debugging)."""
        return json.dumps(self.__dict__, indent=2)


# ═════════════════════════════ JSON → objects helper ═════════════════════════════

def load_ec2_instances(path: str) -> List[Ec2Instance]:
    """Read *path* and build a list of clean Ec2Instance objects.

    If any row throws an error while we try to clean it, we print a warning and
    skip that row.  The rest of the data keeps loading.
    """
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)

    instances: List[Ec2Instance] = []
    for row in raw:
        try:
            instances.append(
                Ec2Instance(
                    row["name"],
                    row["vcpu"],
                    row["memory"],
                    row["storage"],
                    row["bandwidth"],
                    row["availability"],
                )
            )
        except Exception as exc:
            print(f"  Skipped {row.get('name', '?')}: {exc}")
    return instances


# ═════════════════════════════ user input helpers ═════════════════════════════

def _ask_number(prompt: str, *, allow_blank: bool = True, minimum: float = 0) -> Optional[float]:
    """Ask the user for a number.  Keeps asking until it gets a valid one.

    If *allow_blank* is True, hitting *Enter* returns **None** so callers can
    treat a blank as "no limit".
    """
    while True:
        text = input(prompt).strip()
        if text == "" and allow_blank:
            return None
        try:
            value = float(text)
            if value >= minimum:
                return value
            print(f"  Value must be ≥ {minimum}.")
        except ValueError:
            print("  Please enter a number.")


def _print_table(rows: List[Ec2Instance]) -> None:
    """Show matching instances in a simple table."""
    if not rows:
        print("\nNo instance types meet your criteria!!!")
        return

    name_width = max(len(r.name) for r in rows) + 2
    print(f"\n{'Instance Type'.ljust(name_width)}vCPUs\tMemory (GiB)")
    print("-" * (name_width + 18))
    for r in rows:
        print(f"{r.name.ljust(name_width)}{r.vcpu:>5}\t{r.memory:>11.1f}")

# ═════════════════════════════ sort helper ═════════════════════════════
def _sort_key(instance: Ec2Instance):
    """
    Return a tuple that Python can compare when it sorts the list.

    We want the list ordered by:
      1. Fewest vCPUs first
      2. If vCPUs tie, smaller memory first
    """
    return (instance.vcpu, instance.memory)

# ═════════════════════════════ main program ═════════════════════════════

def main() -> None:
    """Run the interactive *EC2 Instance Finder*.

    Steps:
      • Load and clean the JSON data.
      • Ask the user for min/max vCPUs and GiB.
      • Filter the list and show the results.
    """

    JSON_FILE = (
        "/Users/home123/scripting_python_2025/"
        "Scripting_Cloud/In-Class_4_JSON/ec2_instance_types.json"
    )

    instances = load_ec2_instances(JSON_FILE)
    if not instances:
        print("No data loaded.  Check the JSON file path.")
        return

    print("=== AWS EC2 Instance Finder ===")
    min_cpu = _ask_number("Minimum vCPUs (required): ", allow_blank=False, minimum=1)
    max_cpu = _ask_number("Maximum vCPUs (optional): ")
    min_mem = _ask_number("Minimum GiB (required): ", allow_blank=False, minimum=0)
    max_mem = _ask_number("Maximum GiB (optional): ")

    # Filter based on what the user typed
    matches = [
        inst
        for inst in instances
        if inst.vcpu >= min_cpu
        and (max_cpu is None or inst.vcpu <= max_cpu)
        and inst.memory >= min_mem
        and (max_mem is None or inst.memory <= max_mem)
    ]

    # Sort by useful order: first by vCPU, then by memory
    matches.sort(key=_sort_key)     
    _print_table(matches)



if __name__ == "__main__":
    """
    Entry point of the script. Ensures main() is called only when the script is run
    directly, not when imported as a module.
    """
    main()
