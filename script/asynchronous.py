import json
import time

import aiohttp
import asyncio


async def getResponse(pair):
    async with aiohttp.ClientSession() as session:
        async with session.get(
                'http://localhost:8080/primes?start=' + str(pair[0]) + '&end=' + str(pair[1])) as response:
            response = await response.json()
            print(response)


async def main():
    f = open("values.json")
    data = json.load(f)
    await asyncio.gather(*[getResponse(d) for d in data])


start = time.time()
asyncio.run(main())
end = time.time()

with open("output.json") as f:
    js = json.load(f)

js.append({
    "type": "asynchronous",
    "time(s)": end - start
})

with open("output.json", 'w') as f:
    json.dump(js, f, indent=1)
