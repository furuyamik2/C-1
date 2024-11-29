import streamlit as st
import sqlite3
import pandas as pd
from DB.save_db import load_data, clear_table

# 初期表示としてデータベースの内容を表示
st.subheader("現在のデータベース内容")
df_from_db = load_data()

# 編集可能なデータフレームを表示
edited_df = st.data_editor(df_from_db)

if st.button('保存'):
    conn = sqlite3.connect('food_info.db')
    cursor = conn.cursor()

    try:
        # 編集されたデータフレームをループして更新
        for index, row in edited_df.iterrows():
            # 更新するデータを準備
            updated_row = {
                '商品名': row['商品名'],
                '価格': row['価格'],
                '個数': row['個数'],
                'カテゴリー': row['カテゴリー'],
                '消費期限': row['消費期限']
            }

            # SQL UPDATE文でデータを更新
            cursor.execute("""
                UPDATE info SET 商品名 = ?, 価格 = ?, 個数 = ?, カテゴリー = ?, 消費期限 = ? 
                WHERE 商品名 = ?
            """, (
                updated_row['商品名'], 
                updated_row['価格'], 
                updated_row['個数'], 
                updated_row['カテゴリー'], 
                updated_row['消費期限'], 
                row['商品名']
            ))

        # コミットして変更を保存
        conn.commit()
        st.success("データベースが更新されました")
    
    except Exception as e:
        # エラーメッセージを表示
        st.error(f"データベースの更新中にエラーが発生しました: {e}")
    
    finally:
        conn.close()  # 接続を閉じる

# データベース内容が正しく表示されているかを確認
st.dataframe(edited_df, use_container_width=True)

# ALL CLEARボタン
if st.sidebar.button('ALL CLEAR'):
    clear_table('info')
    st.warning("データベースがクリアされました")
