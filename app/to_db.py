import sqlite3
import pandas as pd

def csv_to_sql(csv_name, db_name, sql_name):
    df = pd.read_csv(csv_name)

    df = df.drop(df.columns[0], axis=1)

    conn = sqlite3.connect(db_name)

    df.to_sql(sql_name, conn, if_exists='replace')

    c = conn.cursor()
    query = 'SELECT * FROM ' + sql_name
    c.execute(query)

    c.fetchone

    for row in c.execute(query):
        print(row)

    conn.close()

#input('csv_name')
#input('db_name')
#input('sql_name')

csv_name = 'vege_list.csv'
db_name = 'vege_info.db'
sql_name = 'vege_limit'
csv_to_sql(csv_name, db_name, sql_name)