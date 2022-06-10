import time
from datetime import datetime
import click


def sleep_and_print(sec):
    print(f"starting {sec} sleep 😴")
    time.sleep(sec)
    print(f"finished {sec} sleep ⏰")
    return sec


start = datetime.now()
print([sleep_and_print(3), sleep_and_print(6)])

click.secho(f"{datetime.now() - start}", bold=True, bg="blue", fg="white")
