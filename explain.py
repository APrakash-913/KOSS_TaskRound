import asyncio
import time

start = time.time()

# couritine 1
async def fetch_data():
    print('start fetching')
    await asyncio.sleep(4) # depict that server take 2sec to respond
    print('done fetching')
    return {'data': 1} # depict some JSON responses are receieved

# couritine 2
async def print_num():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5) # something like we get request every 0.25sec .

# couritine 3
async def print_alpha():
    for i in range(10):
        print(f'a{i}')
        await asyncio.sleep(0.25) # something like we get request every 0.25sec .

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_num())
    task3 = asyncio.create_task(print_alpha())

    val = await task1 # Ensure that 'task 1' is finished && assign the return value(if it has) to 'val'.
    print(val)

    await task2
    await task3

    # val = task1
    # print(val)

asyncio.run(main())

end = time.time()
print(f'Total Time = {end - start}')