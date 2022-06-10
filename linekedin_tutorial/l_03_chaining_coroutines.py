import asyncio
from datetime import datetime
import click


async def sleep_five():
    print(f"starting 5 sleep 😴")
    await asyncio.sleep(5)
    print(f"finished 5 sleep ⏰")


async def sleep_three_then_five():
    print(f"starting 3 and 5 sleep 😴")
    await asyncio.sleep(3)
    await sleep_five()
    print(f"finished 3 and 5 sleep ⏰")


async def main():
    results = await asyncio.gather(sleep_five(), sleep_three_then_five())
    print(results)


start = datetime.now()
asyncio.run(main())
click.secho(f"{datetime.now() - start}", bold=True, bg="blue", fg="white")
