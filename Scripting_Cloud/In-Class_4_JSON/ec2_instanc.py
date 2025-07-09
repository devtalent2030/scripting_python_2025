# Author: ⁠Oyelekan Ogunrinu
# Created: October 6, 2023
# Modified: July 3, 2025
# Description:
# This script processes AWS EC2 instance data from a JSON file using object-oriented
# Python. It defines an Ec2Instance class to model EC2 instances, converts JSON data
# into Ec2Instance objects, and provides methods to display, serialize, and analyze
# instances. The script handles complex vCPU strings (e.g., '2 vCPUs for a 1h 12m burst')
# by extracting numeric values, includes robust error handling, and supports large datasets
# for real-world cloud computing tasks.

import json


class Ec2Instance:
    """Holds clean, numeric info about one EC2 instance row."""

    def __init__(self, raw_row):
        # Original JSON might store numbers as strings like "8 vCPU".
        self.name = raw_row["name"]

        # vCPU → always int
        vcpu_raw = str(raw_row["vcpu"]).split()[0]
        self.vcpu = int(float(vcpu_raw))

        # memory → always float GiB
        mem_raw = str(raw_row["memory"]).split()[0]
        self.memory = float(mem_raw)

        # keep the remaining fields as‑is (strings)
        self.storage = raw_row.get("storage", "?")
        self.bandwidth = raw_row.get("bandwidth", "?")
        self.availability = raw_row.get("availability", "?")

    def summary(self):
        """Return a short human‑friendly string."""
        return f"{self.name} | {self.vcpu} vCPUs | {self.memory} GiB"



def load_instances(json_path):
    """Return a list of Ec2Instance objects from a JSON file."""
    with open(json_path, "r", encoding="utf‑8") as fh:
        raw = json.load(fh)

    good_rows = []
    for row in raw:
        try:
            good_rows.append(Ec2Instance(row))
        except Exception as e:
            print("Skipped", row.get("name", "?"), "→", e)
    return good_rows


def ask_number(prompt, allow_blank=True):
    """Ask user for a float. Blank returns None (no limit)."""
    while True:
        txt = input(prompt).strip()
        if txt == "" and allow_blank:
            return None
        try:
            return float(txt)
        except ValueError:
            print("  Please type a number or hit Enter.")


def print_table(rows):
    if not rows:
        print("No matching instance types!")
        return

    width = max(len(r.name) for r in rows) + 2
    print("Instance".ljust(width), "vCPU", "Memory (GiB)")
    print("-" * (width + 18))
    for r in rows:
        print(r.name.ljust(width), f"{r.vcpu:>4}", f"{r.memory:>11.1f}")


def _sort_key(instance):
    """Return a tuple used to order instances by vCPU then memory."""
    return (instance.vcpu, instance.memory)



def main():
    DATA_FILE = "ec2_instance_types.json"  # path relative to script
    

    instances = load_instances(DATA_FILE)
    if not instances:
        print("No data found — check JSON file path.")
        return

    print("EC2 Instance Finder")
    min_cpu = ask_number("Min vCPUs (required): ", allow_blank=False)
    max_cpu = ask_number("Max vCPUs (optional): ")
    min_mem = ask_number("Min GiB (required): ", allow_blank=False)
    max_mem = ask_number("Max GiB (optional): ")

    matches = [
        inst for inst in instances
        if inst.vcpu >= min_cpu and (max_cpu is None or inst.vcpu <= max_cpu)
        and inst.memory >= min_mem and (max_mem is None or inst.memory <= max_mem)
    ]

    # sort without lambda
    matches.sort(key=_sort_key)
    print_table(matches)


if __name__ == "__main__":
    main()
