"""
Sites with low enough update rates that no search is necessary, just open the url
"""

SITES = [
    "https://www.pyjobs.com/",
    "https://www.hireculture.org/findjob.aspx",
    "https://www.python.org/jobs/",
    "https://djangojobboard.com/",
]


def get_urls(sites: list[str] = SITES) -> list[str]:
    return sites
