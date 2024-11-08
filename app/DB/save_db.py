import sqlite3
import pandas as pd

def csv_to_sql(csv_name, table_name):
    # CSVファイルを読み込む
    df = pd.read_csv(csv_name)
    
    # SQLiteデータベースに接続
    conn = sqlite3.connect('food_info.db')
    
    # DataFrameを指定のテーブル名でデータベースに保存
    df.to_sql(table_name, conn, if_exists='replace', index=False)  # index=FalseでDataFrameのインデックス列は含めない

    # テーブルからデータを読み込んで表示
    c = conn.cursor()
    query = 'SELECT * FROM ' + table_name
    c.execute(query)
    
    # 結果をすべて取得し表示
    rows = c.fetchall()
    for row in rows:
        print(row)

    # 接続を閉じる
    conn.close()

