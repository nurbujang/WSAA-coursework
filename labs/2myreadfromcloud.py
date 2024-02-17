import requests
import json

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
#print (response.json()) # if you stop here, it's hard to read, so dont do this

data = response.json()
with open("mybitcoindump.json", "w") as fp:
   json.dump(data, fp)

# euroobject = data["bpi"]["EUR"]
# rate = euroobject["rate"]

# in lecture: (same result as above code)
bpi = data["bpi"]
rate = bpi["EUR"]["rate"]

print(rate)