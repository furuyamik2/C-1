import sqlite3
import pandas as pd

def csv_to_sql(csv_name, table_name):
    # CSVファイルを読み込む
    df = pd.read_csv(csv_name)
    
    # SQLiteデータベースに接続
    conn = sqlite3.connect('food_info.db')
    
    # DataFrameを指定のテーブル名でデータベースに保存
    df.to_sql(table_name, conn, if_exists='append', index=False)  # index=FalseでDataFrameのインデックス列は含めない

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

# データベースの内容を取得する関数
def load_data():
    conn = sqlite3.connect('food_info.db')
    df = pd.read_sql("SELECT * FROM info", conn)
    conn.close()
    return df

def clear_table(table_name):
    # SQLiteデータベースに接続
    conn = sqlite3.connect('food_info.db')
    c = conn.cursor()
    
    # テーブルのデータを全削除
    query = f'DELETE FROM {table_name}'
    c.execute(query)
    
    # 変更を保存
    conn.commit()
    print(f"'{table_name}' テーブルのデータが削除されました。")
    
    # 接続を閉じる
    conn.close()

# データベースから行を削除する関数
def delete_row(product_name):
    import sqlite3
    conn = sqlite3.connect('food_info.db')  # フルパスを指定
    cursor = conn.cursor()

    # データベースから指定された商品名を削除
    query = "DELETE FROM info WHERE 商品名 = ?"
    cursor.execute(query, (product_name,))
    conn.commit()
    conn.close()