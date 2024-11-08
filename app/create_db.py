import sqlite3
from datetime import datetime

db = sqlite3.connect('vege_info.db')
print('接続')

cur = db.cursor()

cur.execute('CREATE TABLE all_list(name STRING PRIMARY KEY, time INTGER, limit, INTEGER)')

sql = 'INSERT INTO all_list (name) values(?)'
data = [('aaaa')]

cur.executemany(sql, data)

db.commit()

cur.close()
db.close()
print('接続解除')