import typer
from . import config, browser, splash

app = typer.Typer()


@app.command()
def main():
    splash.splash()
    settings = config.load()
    browser.run(settings)
    typer.pause("  press any key to close...")


def run():
    app()
