import random
import time
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
    print(f'Rocket launched!')


def rockets():
    n = 10_000
    return [(random_delay(), random_countdown()) for _ in range(n)]


# use threads
def run_threads():
    threads = [Thread(target=launch_rocket, args=(d, c)) for d, c in rockets()]
    for t in threads:
        t.start()  # start the thread
    for t in threads:
        t.join()


if __name__ == "__main__":
    run_threads()


""" run in on macOs 
1. $ brew install brew install gnu-time  
2. $ gtime -v python l_16_01_synchronous_tasks_with_threads.py 
3. or $ time python l_16_01_synchronous_tasks_with_threads.py 

run on ubuntu 
$ time -v python l_16_01_synchronous_tasks_with_threads.py
"""