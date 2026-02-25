from urllib import parse

BASE_URL = "https://www.linkedin.com/jobs/search/"
TIMESPAN = "f_TPR=r86400"

def build_url(term: str, location: str = "Boston, MA") -> str:
    term = parse.quote_plus(term)
    location = parse.quote_plus(location)
    return f"{BASE_URL}?keywords={term}&location={location}&{TIMESPAN}"

def get_urls(term: str) -> list[str]:
    return [build_url(term)]