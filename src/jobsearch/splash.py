from datetime import date

import pyfiglet
from rich.console import Console

console = Console()

RAINBOW = ["red", "yellow", "green", "cyan", "blue", "magenta"]


def splash():
    art = pyfiglet.figlet_format("jobsearch", font="banner")
    lines = art.splitlines()

    console.print()
    for i, line in enumerate(lines):
        color = RAINBOW[i % len(RAINBOW)]
        console.print(f"  [{color}]{line}[/{color}]")
    console.print()
    console.print(f"  [white]{date.today().isoformat()}[/white]")
    console.print()
