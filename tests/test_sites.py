import pytest
from jobsearch.sites import linkedin, greenhouse, builtin, google, others


@pytest.mark.parametrize("term", ["python", "django", "fastapi", "backend", "pytest"])
def test_linkedin_build_url_single(term):
    url = linkedin.build_url(term)
    assert (
        url
        == f"https://www.linkedin.com/jobs/search/?keywords={term}&location=Boston%2C+MA&f_TPR=r86400"
    )


def test_linkedin_build_url_location():
    term = "python"
    url = linkedin.build_url(term, "New York, NY")
    assert (
        url
        == f"https://www.linkedin.com/jobs/search/?keywords={term}&location=New+York%2C+NY&f_TPR=r86400"
    )


def test_linkedin_build_url_compound():
    term = "backend engineer"
    url = linkedin.build_url(term)
    assert (
        url
        == f"https://www.linkedin.com/jobs/search/?keywords=backend+engineer&location=Boston%2C+MA&f_TPR=r86400"
    )


@pytest.mark.parametrize("term", ["python", "django", "fastapi", "backend", "pytest"])
def test_greenhouse_build_url_single(term):
    url = greenhouse.build_url(term)
    assert (
        url
        == f"https://my.greenhouse.io/jobs?query={term}&lat=42.355492&lon=-71.048611"
    )


def test_greenhouse_build_url_location():
    term = "python"
    lat, lon = "40.68295", "-73.9708"
    url = greenhouse.build_url(term, lat, lon)
    assert url == f"https://my.greenhouse.io/jobs?query=python&lat={lat}&lon={lon}"


def test_greenhouse_build_url_compound():
    term = "backend engineer"
    url = greenhouse.build_url(term)
    assert (
        url
        == f"https://my.greenhouse.io/jobs?query=backend%20engineer&lat=42.355492&lon=-71.048611"
    )


@pytest.mark.parametrize("term", ["python", "django", "fastapi", "backend", "pytest"])
def test_builtin_build_url_single(term):
    url = builtin.build_url(term)
    assert (
        url == f"https://www.builtinboston.com/jobs/remote/hybrid/office?search={term}"
    )


def test_builtin_build_url_compound():
    term = "backend engineer"
    url = builtin.build_url(term)
    assert (
        url
        == f"https://www.builtinboston.com/jobs/remote/hybrid/office?search=backend+engineer"
    )


@pytest.mark.parametrize("term", ["python", "django", "fastapi", "backend", "pytest"])
def test_google_build_url_single(term):
    site = "lever.co"
    url = google.build_url(term, site)
    assert (
        url
        == f'https://www.google.com/search?q="{term}"%20site%3A{site}%20massachusetts&tbs=qdr:d'
    )


@pytest.mark.parametrize("site", [linkedin, greenhouse, builtin])
def test_get_urls_sites(site):
    term = "python"
    result = site.get_urls(term)
    assert result == [site.build_url(term)]


def test_get_urls_google():
    term = "python"
    result = google.get_urls(term)
    assert len(result) == len(google.SITES)
    assert all("python" in url for url in result)


def test_get_urls_others():
    assert others.get_urls() == others.SITES
