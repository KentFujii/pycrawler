from urllib import request
from os import path
import random
import json

url = 'http://api.aoikujira.com/hyakunin/get.php?fmt=json'
savename = 'hyakunin.json'
if not path.exists(url):
    request.urlretrieve(url, savename)

data = json.load(open(savename, 'r', encoding='utf-8'))
r = random.choice(data)
print(r['kami'], r['simo'])
