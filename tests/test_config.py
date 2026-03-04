from jobsearch import config

def test_load_config(monkeypatch, tmp_path):
    config_file = tmp_path / "config.toml"
    config_file.write_text("""
    [search]
    terms = ["python"]

    [sites]
    enabled = ["linkedin"]
    """)
    
    monkeypatch.setattr("jobsearch.config.CONFIG_PATH", config_file)
    
    result = config.load()
    
    assert result["search"]["terms"] == ["python"]

def test_load_config_with_linkedin_profiles(monkeypatch, tmp_path):
    config_file = tmp_path / "config.toml"
    config_file.write_text("""
    [search]
    terms = ["python"]

    [sites]
    enabled = ["linkedin"]
    """)
    
    monkeypatch.setattr("jobsearch.config.CONFIG_PATH", config_file)
    monkeypatch.setenv("LINKEDIN_PROFILES", "user1,user2")
    
    result = config.load()
    
    assert result["linkedin_profiles"] == ["user1", "user2"]
    assert result["search"]["terms"] == ["python"]