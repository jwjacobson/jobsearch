import typer
from . import config, browser, splash

app = typer.Typer()


@app.command()
def main():
    splash.splash()
    settings = config.load()
    # browser.run(settings)
    browser.run(settings, on_ready=lambda: typer.pause("  press any key to close..."))
    # typer.pause("  press any key to close...")


def run():
    app()
