from jobsearch import network

usernames = ["hsimpson", "bsimpson", "lsimpson", "mbouvier"]

def test_get_urls():
    result = network.get_urls(usernames)
    expected = [
        f"https://www.linkedin.com/in/{username}/recent-activity/all/"
        for username in usernames
    ]

    assert result == expected

def test_get_urls_empty():
    result = network.get_urls([])
    assert result == []