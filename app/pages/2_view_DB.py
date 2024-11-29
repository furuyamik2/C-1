import streamlit as st
import sqlite3
import pandas as pd
from DB.save_db import load_data, clear_table

# 初期表示としてデータベースの内容を表示
st.subheader("現在のデータベース内容")
df_from_db = load_data()

# 編集可能なデータフレームを表示
edited_df = st.data_editor(df_from_db)

# 編集内容をデータベースに反映するボタン
if st.button('保存'):
    # データベースに接続
    conn = sqlite3.connect('food_info.db')  # 正しいデータベース名を指定
    cursor = conn.cursor()

    # 編集されたデータフレームをループして更新
    for index, row in edited_df.iterrows():
        # 編集後のデータ
        updated_row = {
            '商品名': row['商品名'],
            '価格': row['価格'],
            '個数': row['個数'],
            'カテゴリー': row['カテゴリー'],
            '消費期限': row['消費期限']
        }

        # SQL UPDATE文を使用してテーブルの行を更新
        cursor.execute("""
            UPDATE info 
            SET 商品名 = ?, 価格 = ?, 個数 = ?, カテゴリー = ?, 消費期限 = ?
            WHERE 商品名 = ?
        """, (
            updated_row['商品名'],
            updated_row['価格'],
            updated_row['個数'],
            updated_row['カテゴリー'],
            updated_row['消費期限'],
            updated_row['商品名']  # 商品名をWHERE句で指定
        ))

    # 変更をコミットしてデータベースを更新
    conn.commit()

    # 接続を閉じる
    conn.close()

    st.success("データベースが更新されました！")
# データベース内容が正しく表示されているかを確認
st.dataframe(edited_df, use_container_width=True)

# ALL CLEARボタン
if st.sidebar.button('ALL CLEAR'):
    clear_table('info')
    st.warning("データベースがクリアされました")
