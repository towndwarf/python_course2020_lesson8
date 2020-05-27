import asyncio


async def count1():
    print("One")
    time.sleep(1)
    print("Two")


async def main1():
    await asyncio.gather(count1(), count1(), count1())

if __name__ == "__main__":
    import time

    count1()

    s = time.perf_counter()
    asyncio.run(main1())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
    print('==============================')

import asyncio


async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.4f} seconds.")