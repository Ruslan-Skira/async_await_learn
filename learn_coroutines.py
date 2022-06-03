# sync code https://www.youtube.com/watch?v=uDqkMIL_1pc
# CPU Bound тяжеловесные задачи вроде работы с матрицами, изорбражениями или майнинга . tasks, Video rendering.
# IO input output. Net working. Задачи ожидающие ввода и вывода (работа с диском или сетью)
# async relates to the sockets

"""Coroutines are basically functions whose execution can be paused/suspended at a particular point,
 and then we can resume the execution from that same point later whenever we want."""


# 1. need to learn how to use send in generators

def g():
    i = 0
    while (i < 10):
        i += 1
        from_send = (yield i ** 2)
        print(f"gen received {from_send}")


gen = g()

# for num in gen:
#     print(f"Main: {num}")

for num in gen:
    print(f"Main: {num}")
    next_val = gen.send(f"Thanks for {num}")
    print(f"Main2: {next_val}")

# 1. read this https://book.pythontips.com/en/latest/coroutines.html
# read it very nice https://medium.com/better-programming/coroutines-in-python-building-blocks-of-asynchronous-programming-40c39d9ed420
# 2. read this http://www.dabeaz.com/coroutines/Coroutines.pdf
# 3. read this http://www.dabeaz.com/coroutines/Coroutines.pdf video https://www.youtube.com/watch?v=Z_OAlIhXziw
