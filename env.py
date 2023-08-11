"""
Load environment variables from a file.
"""


import os
import sys


def load(filepath):  # i.e. ".env"
    frozen = getattr(sys, "frozen", False)  # Pyinstaller compatible
    base_path = sys._MEIPASS if frozen else os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(base_path, filepath)

    if not os.path.exists(env_path):
        return

    with open(env_path, "r") as f:
        for line in f:
            if "=" in line:
                key, value = line.strip().split("=")
                os.environ[key.strip()] = value.strip()
