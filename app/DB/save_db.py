import sqlite3
import pandas as pd
import streamlit as st

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

    # データベースを更新する関数
def update_database(edited_df):
    conn = sqlite3.connect('food_info.db')
    cursor = conn.cursor()

    try:
        # テーブルを全て削除して、新しいデータを挿入
        cursor.execute("DELETE FROM info")  # infoテーブルの内容をクリア
        conn.commit()

        # 編集されたデータフレームを一括挿入
        for index, row in edited_df.iterrows():
            cursor.execute("""
                INSERT INTO info (商品名, 価格, 個数, カテゴリー, 名称, 登録日, 消費期限, ファイル名)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                row['商品名'], 
                row['価格'], 
                row['個数'], 
                row['カテゴリー'], 
                row['名称'], 
                row['登録日'], 
                row['消費期限'], 
                row['ファイル名']
            ))

        # コミットして変更を保存
        conn.commit()
        st.success("データベースが更新されました")
    
    except Exception as e:
        # エラーメッセージを表示
        st.error(f"データベースの更新中にエラーが発生しました: {e}")
    
    finally:
        conn.close()  # 接続を閉じる