import json, urllib.request
from collections import Counter

url="https://qrng.anu.edu.au/API/jsonI.php?length=1000&type=uint8"
response = urllib.request.urlopen(url)

jsonForm = json.loads(response.read())

randonNums = jsonForm["data"]

moduled = [i%20 for i in randonNums]

for i in range(0,20):
    print(i , "occurs:" , Counter(moduled)[i] )
