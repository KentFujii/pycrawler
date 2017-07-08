from tinydb import TinyDB, Query

filepath = "test-tinydb.json"
db = TinyDB(filepath)
db.purge_table('fruits')
table = db.table('fruits')

table.insert({'name': 'Banana', 'price': 600})
table.insert({'name': 'Orange', 'price': 1200})
table.insert({'name': 'Mango', 'price': 840})

print(table.all())

Item = Query()
res = table.search(Item.name == 'Orange')
print('Orange is ', res[0]['price'])

print('800円以上のもの: ')
res = table.search(Item.price >= 800)
for it in res:
    print('-', it['name'])
