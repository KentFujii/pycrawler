import sqlite3

dbpath = 'test.sqlite'
conn = sqlite3.connect(dbpath)
cur = conn.cursor()
cur.executescript("""
DROP TABLE IF EXISTS items;
CREATE TABLE ITEMS(
    item_id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    price INTEGER
);
INSERT INTO items(name, price)VALUES('APPLE', 800);
INSERT INTO items(name, price)VALUES('ORANGE', 780);
INSERT INTO items(name, price)VALUES('BANANA', 430);
""")
conn.commit()
cur.execute("SELECT item_id,name,price FROM items")
item_list = cur.fetchall()
for it in item_list:
    print(it)
