import aiohttp
import aiofiles
import asyncio
import nest_asyncio
import time

nest_asyncio.apply()
start = time.time()

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
        # response = await session.get(url)
        # html = await response.text()
            return html

async def file_save(file,text):
    async with aiofiles.open(file, 'w') as f:
        await f.write(text)

async def main(urls):        
    tasks = []
    i = 1
    for url in urls:
        file = f'task2_AdvWay{i}.json'
        html = await fetch(url)
        tasks.append(file_save(file,html))
        i+=1
    await asyncio.gather(*tasks)

urls = []        
for i in range(1,201):
    link = f'https://xkcd.com/{i}/info.0.json'
    urls.append(link)

loop = asyncio.get_event_loop()
loop.run_until_complete(main(urls))

end =time.time()
print(f'Time Taken = {end - start}') # Time Taken = 114.6998028755188