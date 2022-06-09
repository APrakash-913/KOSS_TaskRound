import requests
import time

start = time.time()

for i in range(1, 201):
    r = requests.get(f'https://xkcd.com/{i}/info.0.json') # comic_id = i
    with open(f'task2{i}.json', "w") as f:
        f.write(r.text)

end = time.time()
print(f"Time taken: {end - start}") # Time taken: 144.1226773262024