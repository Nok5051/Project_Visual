import imp
import json
from unittest import result
import requests
import urllib.request
from bs4 import BeautifulSoup
from pprint import pprint

key = "76466b686e6a736e3132305a486c4d4c"

url="http://openapi.seoul.go.kr:8088/" + key + "/json/LOCALDATA_072404/1/5/"

resp = requests.get(url)
# print(resp)

resp1 = resp.json()['LOCALDATA_072404']

ple = list(map(lambda x: x['row'], resp1))
print(ple)
# SITEWHLADDR = list(map(lambda x: x['SITEWHLADDR'], resp1))
# BPLCNM = list(map(lambda x: x['BPLCNM'], resp1))
# print(SITEWHLADDR)
# print(BPLCNM)
# print(resp1[0])

'''
result =[]

for i in range(0, 11):
    try:
        a = resp1[i]
        result.append(a)
    except:
        pass

print(len(result))
'''





