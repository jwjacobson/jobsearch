import pytest
from jobsearch.sites.linkedin import build_url

@pytest.mark.parametrize("term", ["python", "django", "fastapi", "backend", "pytest"])
def test_linkedin_url_single(term):
    url = build_url(term)
    assert url == f"https://www.linkedin.com/jobs/search/?keywords={term}&location=Boston%2C+MA&f_TPR=r86400"

def test_linkedin_url_location():
    term = "python"
    url = build_url(term, "New York, NY")
    assert url == f"https://www.linkedin.com/jobs/search/?keywords={term}&location=New+York%2C+NY&f_TPR=r86400"

def test_linkedin_url_multiple():
    term = "backend engineer"
    url = build_url(term)
    assert url == f"https://www.linkedin.com/jobs/search/?keywords=backend+engineer&location=Boston%2C+MA&f_TPR=r86400"
    