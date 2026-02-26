import typer
from . import config, browser, splash

app = typer.Typer()


@app.command()
def main(
    site: str | None = typer.Option(None, "--site", "-s", help="Search only the specified site.")
):
    splash.splash()
    settings = config.load()
    
    if site and site not in browser.SITES:
        typer.echo(f"Unknown site '{site}'. Valid options: {', '.join(browser.SITES.keys())}")
        raise typer.Exit(1)
    elif site:
        settings["sites"]["enabled"] = [site]

    browser.run(settings, on_ready=lambda: typer.pause("  press any key to close..."), site=site)


def run():
    app()
