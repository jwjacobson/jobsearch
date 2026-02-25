"""
This module replicates a portion of the google searches performed by Brian's Job Search - https://briansjobsearch.com/
"""

from urllib import parse

BASE_URL = "https://www.google.com/search?q="
SITES = [
    "lever.co",
    "ashbyhq.com",
    "jobs.*",
    "careers.*+OR+site%3A*%2Fcareers%2F*+OR+site%3A*%2Fcareer%2F*",
    "people.*",
    "talent.*",
    "workatastartup.comicims.com",
    "wellfound.com",
    "breezy.hr",
]
LOCATION = "massachusetts"
TIMESPAN = "tbs=qdr:d"  # last day


def build_url(term: str, site: str, location: str = LOCATION) -> str:
    term = parse.quote(term)
    return f'{BASE_URL}"{term}"%20site%3A{site}%20{location}&{TIMESPAN}'


def get_urls(term: str) -> list[str]:
    return [build_url(term, site) for site in SITES]
