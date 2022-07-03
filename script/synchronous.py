import json
import time

import requests as req


def main():
    f = open("values.json")
    data = json.load(f)
    for d in data:
        request = req.get('http://localhost:8080/primes?start=' + str(d[0]) + '&end=' + str(d[1]))
        print(request.json())


start=time.time()
main()
end=time.time()

with open("output.json") as f:
    js = json.load(f)

js.append({
    "type": "synchronous",
    "time(s)": end-start
})

with open("output.json", 'w') as f:
    json.dump(js,f,indent=1)
