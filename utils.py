import requests
import os
from dotenv import load_dotenv


def get_puzzle_input(url):
    load_dotenv()
    r = requests.get(url, cookies={"session": os.getenv("COOKIE")})
    return r.content.decode("utf-8")


def iter_lines(inp):
    for line in inp.split("\n"):
        if line:
            yield line
