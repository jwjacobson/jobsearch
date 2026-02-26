![Tests](https://github.com/jwjacobson/jobsearch/actions/workflows/tests.yaml/badge.svg)
# jobsearch - automate job board searches
Jobsearch launches a browser instance and automatically searches all provided search terms on all configured URLs, one tab per search. It is built using [Playwright](https://playwright.dev/python/) and [Python 3.14](https://www.python.org/).

It is designed to be easily extensible and configurable, and is free to use, modify, and distribute under the terms of the [GPL](https://github.com/jwjacobson/jobsearch/blob/main/LICENSE).

## Installation
First, [Install uv](https://docs.astral.sh/uv/getting-started/installation/) and [Clone this repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

Navigate to the project directory:
```bash
 cd jobsearch
```
Install jobsearch locally:
```bash
uv pip install -e . 
```

Install the Playwright browsers:
```bash
uv run playwright install 
```

## Configuration
Jobsearch is configured as-is to be useful to me. Unless you live in the same place and are looking for the same types of jobs, you will want to configure it to be useful to you.

Of the included sites (located in `src/jobsearch/sites`), `builtin.py` is Boston-specific, while `greenhouse.py` and `linkedin.py` default to Boston searches, and `google.py` defaults to Massachusetts. You can update them to suit your requirements.

The file `config.toml` in the root directory contains search terms and the sites to be searched. To add or edit search terms, just edit the list `terms` on line 2.

Jobsearch currently supports searches on LinkedIn, Greenhouse, BuiltinBoston, and Google. To add support for another site, you will need to:
1. Add a module for it in the `sites` directory (use the existing modules as models; the tricky part is figuring out each site's url format);
2. Import it and add it to the SITES dict in `browser.py`  ;
3. Add it to the `enabled` list in the `[sites]` table of `config.toml`;
4. (Optional but recommended) Add tests of your new module to `test_sites.py`.

> [!NOTE]
> The searches in the Google module tend to trigger Google's captchas, which eliminates the convenience of including them at all. For now I'm disabling the google module by default, but you can enable it in `config.toml` if you'd like to try it out. In the meantime, I recommend using [Brian's Job Search](https://briansjobsearch.com/) instead (more clicks than jobsearch, but less than doing a Google captcha for each search)


## Running jobsearch
```bash
uv run jobsearch 
```

## Loading user settings
Sites like LinkedIn are easier to use if you're logged in. You can point jobsearch at your browser's config folder (and thus run jobsearch with all your saved logins) by copying the file `.env-template` into a file called `.env`:
```bash
cp .env-template .env 
```
The value of `USER_DATA_DIR` should be the path to your browser's settings directory. For example, for the Chromium browser on my system, this is `~/.config/chromium`.

> [!NOTE]
> If you are already running a separate instance of Chromium, it will block Playwright's access to the user settings folder. One way around this is to copy the folder somewhere else (like into the project folder) and then point jobsearch at that folder.

## Feedback
- For bug reports, please open an issue with a description of what you expected vs what you got
- For suggestions, please open an issue with a description of the desired behavior
- For gratuitous praise, please send a toot to https://fosstodon.org/@jeffjacobson
- Thanks for stopping by!

## Acknowledgments
The google searches in `google.py` reproduce functionality provided by [Brian's Job Search](https://briansjobsearch.com/).