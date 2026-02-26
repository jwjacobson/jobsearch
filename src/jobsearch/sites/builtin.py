from urllib import parse

BASE_URL = "https://www.builtinboston.com/jobs/remote/hybrid/office"
TIMESPAN = "daysSinceUpdated=1"


def build_url(term: str) -> str:
    term = parse.quote_plus(term)
    return f"{BASE_URL}?search={term}&{TIMESPAN}"


def get_urls(term: str) -> list[str]:
    return [build_url(term)]
