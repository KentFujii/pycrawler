import requests

r = requests.get('http://api.aoikujira.com/time/get.php')

text = r.text
print(text)

b = r.content
print(b)
