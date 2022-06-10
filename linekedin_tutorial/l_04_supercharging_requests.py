from datetime import datetime
from pprint import pprint
import asyncio
import aiohttp


import click
import requests

urls = ["http://httpbin.org/get?text=python", "http://httpbin.org/get?text=java", "http://httpbin.org/get?text=perl",
        "http://httpbin.org/get?text=python3", "http://httpbin.org/get?text=java2", "http://httpbin.org/get?text=perl1",
        "http://httpbin.org/get?text=ops", "http://httpbin.org/get?text=interestingk",
        "http://httpbin.org/get?text=what", "http://httpbin.org/get?text=whill", "http://httpbin.org/get?text=be",
        "http://httpbin.org/get?text=next", ]


async def fetch_args(session, url):
    # https://docs.aiohttp.org/en/stable/client_reference.html
    async with session.get(url) as response:
        data = await response.json()
        return data["args"]

async def main():
    async with aiohttp.ClientSession() as session:
        # creating a collection of coroutines(can be done with comprehension)
        fetch_coroutines = []
        for url in urls:
            fetch_coroutines.append(fetch_args(session, url))
        # walk up coroutines with gather
        data = await asyncio.gather(*fetch_coroutines)
        pprint(data)

start = datetime.now()
asyncio.run(main())


# def get_args(url):
#     return requests.get(url).json()["args"]
#
#
# start = datetime.now()
#
# pprint([get_args(url) for url in urls])
click.secho(f"{datetime.now() - start} ", bold=True, bg="blue", fg="white")
