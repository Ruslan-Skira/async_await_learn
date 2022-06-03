import random
import time
from threading import Thread
from enum import Enum, auto


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


# машинное состояние

class State(Enum):
    """Стан"""
    WAITING = auto()
    COUNTING = auto()
    LAUNCHING = auto()


class Op(Enum):
    """Стан"""
    WAIT = auto()
    STOP = auto()



class Launch:
    """кінцевий автомат"""

    def __init__(self, delay, countdown):
        self._state = State.WAITING
        self._delay = delay
        self._countdown = countdown


    def step(self):
        if self._state is State.WAITING:
            self._state = State.COUNTING
            return Op.WAIT, self._delay
        if self._state is State.COUNTING:
            if self._countdown == 0:
                self._state = State.LAUNCHING
            else:
                print(f"{self._countdown}...")
                self._countdown -= 1
                return Op.WAIT, 1
        if self._state is State.LAUNCHING:
            print("rocket Launched!")
            return Op.STOP, None
        assert False, self._state

# def run(rockets): ніххера не зрозуміло https://www.youtube.com/watch?v=x6JZmBK2I8Y&t=1122s далі дивись

if __name__ == "__main__":
    run_threads()

""" run in on macOs 
1. $ brew install brew install gnu-time  
2. $ gtime -v python l_16_01_synchronous_tasks_with_threads.py 
3. or $ time python l_16_01_synchronous_tasks_with_threads.py 

run on ubuntu 
$ time -v python l_16_01_synchronous_tasks_with_threads.py
"""
