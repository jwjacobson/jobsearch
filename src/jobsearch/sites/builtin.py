from urllib import parse

BASE_URL = "https://www.builtinboston.com/jobs/remote/hybrid/office"

def build_url(term: str) -> str:
    term = parse.quote_plus(term)
    return f"{BASE_URL}?search={term}"