"""
Writes and reads JSON files.
"""


import json
import os


def write(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def read(filename, default=None):
    if not os.path.exists(filename):
        return default

    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return default
