from decouple import config
from playwright.sync_api import sync_playwright

from .sites import (
    linkedin,
    greenhouse,
    builtin,
    google,
    others
)

SITES = {
    "linkedin": linkedin.get_urls,
    "greenhouse": greenhouse.get_urls,
    "builtin": builtin.get_urls,
    "google": google.get_urls
}
USER_DATA_DIR = config("USER_DATA_DIR", None)

def run(settings):
    with sync_playwright() as p:
        if USER_DATA_DIR:
            context = p.chromium.launch_persistent_context(
                user_data_dir=USER_DATA_DIR,
                headless=False)
        else:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()

        for site in settings["sites"]["enabled"]:
            for term in settings["search"]["terms"]:
                for url in SITES[site](term):
                    page = context.new_page()
                    page.goto(url)

        for url in others.get_urls(): # Sites in others don't have a term so get searched separately
            page = context.new_page()
            page.goto(url)

        input("Press Enter to close browser...")
        context.close()