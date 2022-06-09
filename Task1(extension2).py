import asyncio
import nest_asyncio
import aiohttp
import time

nest_asyncio.apply()
start =time.time()

urls = {'https://reqres.in/api/users?page1', 'https://reqres.in/api/users?page2', 'https://reqres.in/api/users?page3'}

async def get_url(urls):
    i = 1
    for url in urls:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                html = await response.text()
                print(f'Done {i}')
                i +=1


async def print_num():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5) # something like we get request every 0.25sec .


async def print_alpha():
    for i in range(10):
        print(f'a{i}')
        await asyncio.sleep(0.25) # something like we get request every 0.25sec .

async def main():
    task1 = asyncio.create_task(get_url(urls))
    task2 = asyncio.create_task(print_num())
    task3 = asyncio.create_task(print_alpha())

    val = await task1 # Ensure that 'task 1' is finished && assign the return value(if it has) to 'val'.
    print(val)

    await task3
    await task2

asyncio.run(main())
end = time.time()
print(f'Total Time = {end - start}')            