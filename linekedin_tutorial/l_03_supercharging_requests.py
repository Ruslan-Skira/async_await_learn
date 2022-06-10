from datetime import datetime
from pprint import pprint

import click
import requests

urls = ["http://httpbin.org/get?text=python", "http://httpbin.org/get?text=java", "http://httpbin.org/get?text=perl",
        "http://httpbin.org/get?text=python3", "http://httpbin.org/get?text=java2", "http://httpbin.org/get?text=perl1",
        "http://httpbin.org/get?text=ops", "http://httpbin.org/get?text=interestingk",
        "http://httpbin.org/get?text=what", "http://httpbin.org/get?text=whill", "http://httpbin.org/get?text=be",
        "http://httpbin.org/get?text=next", ]


def get_args(url):
    return requests.get(url).json()["args"]


start = datetime.now()

pprint([get_args(url) for url in urls])
click.secho(f"{datetime.now() - start} ", bold=True, bg="blue", fg="white")
