from urllib import parse

BASE_URL = "https://my.greenhouse.io/jobs"
BOSTON_LAT = "42.355492"
BOSTON_LON = "-71.048611"


def build_url(term: str, lat: str = BOSTON_LAT, lon: str = BOSTON_LON) -> str:
    term = parse.quote(term)
    return f"{BASE_URL}?query={term}&lat={lat}&lon={lon}"


def get_urls(term: str) -> list[str]:
    return [build_url(term)]
