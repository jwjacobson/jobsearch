import typer
from . import config, browser

app = typer.Typer()

@app.command()
def main():
    settings = config.load()
    browser.run(settings)

def run():
    app()