import typer
from . import config, browser, splash

app = typer.Typer()
settings: dict | None = None


@app.callback(invoke_without_command=True)
def setup(ctx: typer.Context):
    """Run setup before any command."""
    global settings
    splash.splash()
    settings = config.load()

    if ctx.invoked_subcommand is None:
        ctx.invoke(main, site=None)

@app.command()
def main(
    site: str | None = typer.Option(
        None, "--site", "-s", help="Search only the specified site."
    ),
):
    """Search all configured keywords on all configured sites or specified site"""
    assert settings is not None

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

@app.command()
def network():
    """Open LinkedIn profiles for networking and engagement."""
    assert settings is not None

    if "linkedin_profiles" not in settings or not settings["linkedin_profiles"]:
        typer.echo("No LinkedIn profiles configured in .env")
        typer.echo("Set LINKEDIN_PROFILES=username1,username2,...")
        raise typer.Exit(1)
    
    usernames = settings["linkedin_profiles"]
    
    typer.echo(f"Opening {len(usernames)} LinkedIn profiles...")
    browser.run_network(usernames, on_ready=lambda: typer.pause("  press any key to close..."))


def run():
    app()
