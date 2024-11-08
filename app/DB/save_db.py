import sqlite3
import pandas as pd

def csv_to_sql(csv_name, table_name):
    df = pd.read_csv(csv_name)

    df = df.drop(df.columns[0], axis=1)

    conn = sqlite3.connect('food_info.db')

    df.to_sql(table_name, conn, if_exists='replace')

    c = conn.cursor()
    query = 'SELECT * FROM ' + table_name
    c.execute(query)

    c.fetchone

    for row in c.execute(query):
        print(row)

    conn.close()
