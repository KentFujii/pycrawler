import urllib.request as req

local = "mushroom.csv"
base_url = "https://archive.ics.uci.edu"
rel_path = "/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"
url = base_url + rel_path
print(url)
req.urlretrieve(url, local)
print('ok')
