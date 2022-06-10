import time
from datetime import datetime
import click
import asyncio


async def sleep_and_print(sec):
    print(f"starting {sec} sleep 😴")
    await asyncio.sleep(sec)
    print(f"finished {sec} sleep ⏰")
    return sec

async def main():
    # using arguments
    # results = await asyncio.gather(sleep_and_print(3), sleep_and_print(6))

    # building list
    coroutines_lis = []
    for i in range(1, 11):
        coroutines_lis.append(sleep_and_print(i))
    results = await asyncio.gather(*coroutines_lis)
    print(results)


start = datetime.now()

asyncio.run(main())
click.secho(f"{datetime.now() - start}", bold=True, bg="blue", fg="white")

