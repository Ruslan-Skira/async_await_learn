import time
import random
from threading import Thread


def random_delay():
    return random.random() * 5


def random_countdown():
    return random.randrange(5)


def launch_rocket(delay, countdown):
    time.sleep(delay)
    for i in reversed(range(countdown)):
        print(f"{i + 1}...")
        time.sleep(1)
    print(f'Rocket launched!{counter}')


def rockets():
    n = 10_000
    return [(random_delay(), random_countdown()) for _ in range(n)]


if __name__ == "__main__":
    counter = 0
    for d, c in rockets():
        counter += 1

        launch_rocket(d, c)
