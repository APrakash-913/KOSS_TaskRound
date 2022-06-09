import asyncio
import time

start = time.time()

async def main():
    # i don't want to wait for "foo" to complete, instead i want to run next line of code (i will create TASK for this)
    print("Output:")
    print("ap")
    task = asyncio.create_task(foo('text'))
    # await foo('text')
    # await task
    await asyncio.sleep(2)
    print("finished")

async def foo(text):
    print(text)
    # asyncio.sleep(1) doesn't work, as we are creating a couritine no running it.
    await asyncio.sleep(1) # we need awit to execute the coroutine.

asyncio.run(main()) # here asyncio created an event loop -> added this coroutine to events loop -> run
# await main() # --> this is wrong as 'await' has to be inside 'async' fn.
               # whenevev we create Asynchronous program in python, we need to create an EVENT.

end = time.time()
print(f'Total Time = {end - start}')