from unittest.mock import patch
from typer.testing import CliRunner
from jobsearch.cli import app

runner = CliRunner()

FAKE_SETTINGS = {
    "search": {"terms": ["python"]},
    "sites": {"enabled": ["linkedin"]},
}

FAKE_SETTINGS_WITH_PROFILES = {
    **FAKE_SETTINGS,
    "linkedin_profiles": ["user1", "user2"],
}


def test_invalid_site_option():
    with patch("jobsearch.cli.config.load", return_value=FAKE_SETTINGS):
        result = runner.invoke(app, ["main", "--site", "fake-site"])
    assert result.exit_code == 1
    assert "Unrecognized site" in result.output


def test_network_no_profiles():
    with patch("jobsearch.cli.config.load", return_value=FAKE_SETTINGS):
        result = runner.invoke(app, ["network"])
    assert result.exit_code == 1
    assert "No LinkedIn profiles configured" in result.output