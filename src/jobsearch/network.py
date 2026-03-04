def get_urls(usernames: list[str]) -> list[str]:
    """Generate LinkedIn profile activity URLs from usernames."""
    return [
        f"https://www.linkedin.com/in/{username}/recent-activity/all/"
        for username in usernames
    ]