import asyncio


async def task1():
    print("Send first Email")
    asyncio.create_task(task2())
    await asyncio.sleep(5)
    print("first email replied")


async def task2():
    print("Second email send.")
    asyncio.create_task(task3())
    await asyncio.sleep(2)
    print("Second email reply")


async def task3():
    print("Third email send.")
    await asyncio.sleep(1)
    print("third email reply")


asyncio.run(task1())

