import asyncio

"""Eventy loop - ядро или цикл собітий асинхронного скрипта, эдакий планировщик задач, в который пробрасываются (и в рамках которого выполняются)
асинхронные функции Tasks. В него передается управление, когда асинхронная сопрограмма залипает на блокирующей операции

Task - обертка для корутины, позволяющая ей выполняться в рамках Event Loop'а """


async def say_hello():
    print("hello")
    await asyncio.sleep(3)
    print(' of not?')


# Example 2
async def teatime():
    await asyncio.sleep(1)
    print('take a cup of tea')
    await  asyncio.sleep(1)


async def read():
    print("Reading for 1 hour", end='')
    await teatime()
    print('conntinue reading')


# exaple 3 https://www.youtube.com/watch?v=pIXiChn5j4E


import time

start = time.time()


def two():
    print('starting two')
    time.sleep(2)
    print('hey two')


def four():
    print('starting four')
    time.sleep(4)
    print('hey for')


end = time.time()


# and the same exampe 3 only with asyncio
async def two_a():
    print('starting, two')
    await asyncio.sleep(2)
    print('hey two')
    return 2


async def four_a():
    print('starting four')
    await asyncio.sleep(4)
    print('hey four')
    return 4


async def main():
    print(await asyncio.gather(two_a(), four_a()))


if __name__ == '__main__':  # asyncio.run(say_hello())
    # asyncio.run(read()) # example 2
    # run example 3
    # two()
    # four()
    # print(f'{end - start}')
    asyncio.run(main())  # only one coroutines
