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

## [Disclaimer](DISCLAIMER.md)

If you choose to use this script, you are doing so entirely at your own risk. The script is intended solely for educational purposes, and I cannot be held responsible for any actions that Instagram may take against you for using it. For example, some users have been unable to log in temporarily (6h~) after downloading approximately 5,000 images in a couple hours.

So, it's uncertain what might happen if you were to use this script excessively.

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

-   [ ] Needs to rest to fake humanity.
-   [ ] Detect and download new top images without scanning all.
-   [ ] Add support for videos.
-   [ ] Add support for stories.
