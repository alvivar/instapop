# instapop

Simple Instagram image scrapper.

```
python instapop.py someuser
```

```
usage: instapop.py [-h] user

Scraps Instagram images

positional arguments:
  user        User name to scrap

options:
  -h, --help  show this help message and exit
```

## Authentication

This scripts expects an ".env" file with the following variables:

```
INSTAGRAM_EMAIL = your_instagram_email
INSTAGRAM_PASSWORD = your_instagram_password
```

## You need to install

-   [Playwright](https://playwright.dev/python/docs/intro)

```

pip install pytest-playwright

```

Then to install the required browsers:

```

playwright install

```

-   [Requests](https://pypi.org/project/requests/)

```

pip install requests

```

## TODO

-   [ ] Detect and download new top images without scanning all.
-   [ ] Add support for videos.
-   [ ] Add support for stories.

```

```
