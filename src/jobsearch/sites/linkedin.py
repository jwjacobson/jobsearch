from urllib import parse

BASE_URL = "https://www.linkedin.com/jobs/search-results/"
GEO_ID = "90000007"  # Boston, MA
TIMESPAN = "f_TPR=r86400"  # last day
ORDER_BY = "sortBy=DD"  # most recent first


def build_url(term: str, geo_id: str = GEO_ID) -> str:
    term = parse.quote_plus(term)
    return f"{BASE_URL}?keywords={term}&geoId={geo_id}&{TIMESPAN}&{ORDER_BY}"


def get_urls(term: str) -> list[str]:
    return [build_url(term)]
