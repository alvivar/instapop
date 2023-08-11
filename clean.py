import re
from urllib.parse import urlparse, urlunparse


def to_filepath(name):
    name = re.sub(r"[^\w\-.]|[\s]", "_", name)
    name = re.sub(r"__+", "_", name)

    return name


def normalize_url(url):
    url_parts = urlparse(url)
    scheme = url_parts.scheme.lower()
    netloc = url_parts.netloc.lower().replace("www.", "")
    path = url_parts.path.rstrip("/")
    cleaned = urlunparse((scheme, netloc, path, "", "", ""))

    return cleaned


def url_filename(url):
    url_parts = urlparse(url)
    path = url_parts.path.strip("/")
    if "/" in path:
        path = path.split("/")[-1]

    return path
