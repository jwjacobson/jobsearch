from urllib import parse

BASE_URL = "https://www.linkedin.com/jobs/search/"
LOCATION = "Boston, MA"
TIMESPAN = "f_TPR=r86400"  # last day


def build_url(term: str, location: str = LOCATION) -> str:
    term = parse.quote_plus(term)
    location = parse.quote_plus(location)
    return f"{BASE_URL}?keywords={term}&location={location}&{TIMESPAN}"


def get_urls(term: str) -> list[str]:
    return [build_url(term)]
