import pytest
from jobsearch.sites import linkedin, greenhouse

@pytest.mark.parametrize("term", ["python", "django", "fastapi", "backend", "pytest"])
def test_linkedin_url_single(term):
    url = linkedin.build_url(term)
    assert url == f"https://www.linkedin.com/jobs/search/?keywords={term}&location=Boston%2C+MA&f_TPR=r86400"

def test_linkedin_url_location():
    term = "python"
    url = linkedin.build_url(term, "New York, NY")
    assert url == f"https://www.linkedin.com/jobs/search/?keywords={term}&location=New+York%2C+NY&f_TPR=r86400"

def test_linkedin_url_compound():
    term = "backend engineer"
    url = linkedin.build_url(term)
    assert url == f"https://www.linkedin.com/jobs/search/?keywords=backend+engineer&location=Boston%2C+MA&f_TPR=r86400"
    
@pytest.mark.parametrize("term", ["python", "django", "fastapi", "backend", "pytest"])
def test_greenhouse_url_single(term):
    url = greenhouse.build_url(term)
    assert url == f"https://my.greenhouse.io/jobs?query={term}&lat=42.355492&lon=-71.048611"

def test_greenhouse_url_location():
    term = "python"
    lat, lon = "40.68295", "-73.9708"
    url = greenhouse.build_url(term, lat, lon)
    assert url == f"https://my.greenhouse.io/jobs?query=python&lat={lat}&lon={lon}"

def test_greenhouse_url_compound():
    term = "backend engineer"
    url = greenhouse.build_url(term)
    assert url == f"https://my.greenhouse.io/jobs?query=backend%20engineer&lat=42.355492&lon=-71.048611"
