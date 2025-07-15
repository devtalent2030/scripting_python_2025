from rich.console import Console
from rich.table import Table


"""
Feature.           Why It's Useful
--------------------------------------------------
Console            Print stylish, readable output

Table              Structure data in clean tables

Progress           Show progress bars easily

Markdown           Render markdown in terminal

Traceback          Pretty exception stack traces

"""



# 1. Console – Pretty Printing
console = Console()

console.print("🚀 Hello, world!", style="bold green")
console.print("[bold red]Error:[/] Something went wrong.")

# 2. Table – Tabular Output
console = Console()
table = Table(title="AWS Daily Cost Report")

table.add_column("Date", justify="center", style="cyan", no_wrap=True)
table.add_column("Service", style="magenta")
table.add_column("Cost ($)", justify="right", style="green")

table.add_row("2023-10-01", "EC2", "2.45")
table.add_row("2023-10-01", "S3", "0.12")
table.add_row("2023-10-02", "EC2", "10.88")

console.print(table)

# Experiment 2 – Full Table Example
console = Console()
table = Table(title="Sample Cost Report")

table.add_column("Date", style="cyan")
table.add_column("Service", style="magenta")
table.add_column("Cost", justify="right", style="green")

data = [
    ["2023-10-01", "EC2", "2.45"],
    ["2023-10-01", "S3", "0.12"],
    ["2023-10-02", "EC2", "10.88"]
]

for row in data:
    table.add_row(*row)

console.print(table)
