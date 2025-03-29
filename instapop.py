"""
Scraps Instagram images from a user profile.
"""

import argparse
import os

import requests
from playwright.sync_api import sync_playwright

import clean
import dump
import env


# Default directories
SNAPS_DIR = "snaps"
SCRAPS_DIR = "scraps"
os.makedirs(SNAPS_DIR, exist_ok=True)
os.makedirs(SCRAPS_DIR, exist_ok=True)


# Environment variables
env.load(".env")
INSTAGRAM_EMAIL = os.environ.get("INSTAGRAM_EMAIL")
INSTAGRAM_PASSWORD = os.environ.get("INSTAGRAM_PASSWORD")


def download_image(url, file_path):
    response = requests.get(url)
    if response.status_code != 200:
        return False

    with open(file_path, "wb") as file:
        file.write(response.content)
    return True


def login(page):
    page.goto("https://www.instagram.com/accounts/login/")
    page.wait_for_selector("input[name='username']")
    page.fill("input[name='username']", INSTAGRAM_EMAIL)
    page.fill("input[name='password']", INSTAGRAM_PASSWORD)
    page.click("button[type='submit']")
    page.wait_for_selector("svg[aria-label='Instagram']")
    page.screenshot(path=f"{SNAPS_DIR}/last_login.png")


def goto_profile(page, username):
    page.goto(f"https://www.instagram.com/{username}/")
    page.wait_for_selector(f"img[alt^='{username}']")
    page.screenshot(path=f"{SNAPS_DIR}/{username}.png")


def scrap_images(user, urls=[]):
    with sync_playwright() as p:
        browser = p.chromium.launch()  # headless=False)  # Open browser visibly
        browser.new_context(viewport={"width": 3840, "height": 2160})
        page = browser.new_page()

        login(page)
        goto_profile(page, user)

        page.query_selector("div._aagv img").click()  # The magical tag
        page.wait_for_selector("svg[aria-label='Next']")
        page.wait_for_timeout(1000)
        page.screenshot(path=f"{SNAPS_DIR}/{user}_first.png")

        count = 0
        while True:
            page.wait_for_timeout(200)
            images = page.query_selector_all("div._aagv img")
            next_button = page.query_selector("svg[aria-label='Next']")

            if not next_button:
                page.wait_for_timeout(1000)
                page.screenshot(path=f"{SNAPS_DIR}/{user}_last.png")
                break
            next_button.click()

            for image in images:
                url = image.get_attribute("src")
                url_path = clean.url_filename(url)

                if url_path in urls:
                    continue

                if download_image(url, f"{user_path}/{url_path}"):
                    count += 1
                    urls.append(url_path)
                    print(f"Downloaded {url_path}")

        return (urls, count)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scraps Instagram images")
    parser.add_argument("user", help="User name to scrap")
    args = parser.parse_args()

    user = args.user
    user_path = f"{SCRAPS_DIR}/{user}"
    os.makedirs(user_path, exist_ok=True)

    past_urls = dump.read(f"{user_path}/{user}.json", [])
    print(f"Previous scrap had {len(past_urls)} images")

    new_urls, new_found = scrap_images(user, past_urls)
    print(f"Scraped {new_found} new images")

    dump.write(new_urls, f"{user_path}/{user}.json")
