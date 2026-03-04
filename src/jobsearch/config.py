import tomllib
from pathlib import Path
from decouple import config as env_config, Csv

CONFIG_PATH = Path(__file__).parent.parent.parent / "config.toml"


def load() -> dict:
    with open(CONFIG_PATH, "rb") as f:
        config = tomllib.load(f)

    linkedin_profiles = env_config("LINKEDIN_PROFILES", default="", cast=Csv())

    if linkedin_profiles:
        config["linkedin_profiles"] = linkedin_profiles

    return config
