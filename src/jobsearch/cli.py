import typer
from . import config, browser, splash

app = typer.Typer()


@app.command()
def main(
    site: str | None = typer.Option(
        None, "--site", "-s", help="Search only the specified site."
    ),
):
    splash.splash()
    settings = config.load()

    if site and site not in settings['sites']['enabled']:
        typer.echo(
            f"Unrecognized site: '{site}'. Valid options: {', '.join(settings['sites']['enabled'])}"
        )
        raise typer.Exit(1)
    elif site:
        settings["sites"]["enabled"] = [site]

    browser.run(
        settings, on_ready=lambda: typer.pause("  press any key to close..."), site=site
    )


def run():
    app()
