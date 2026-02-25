import tomllib
from pathlib import Path

CONFIG_PATH = Path(__file__).parent.parent.parent / "config.toml"


def load() -> dict:
    with open(CONFIG_PATH, "rb") as f:
        config = tomllib.load(f)
    return config
