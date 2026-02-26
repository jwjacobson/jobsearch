from datetime import date

import pyfiglet
from rich.console import Console

console = Console()

COLORS = ["magenta", "blue", "cyan", "bright_cyan", "bright_blue", "bright_magenta"]

def splash():
    art = pyfiglet.figlet_format("jobsearch", font="banner")
    lines = art.splitlines()

    console.print()
    for i, line in enumerate(lines):
        color = COLORS[i % len(COLORS)]
        console.print(f"  [{color}]{line}[/{color}]")
    console.print()
    console.print(f"  [bright_yellow]{date.today().isoformat()}[/bright_yellow]")
    console.print()

if __name__ == "__main__":
    splash()
    