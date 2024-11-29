import streamlit as st
import sqlite3
import pandas as pd
from DB.save_db import load_data, clear_table,update_database



# 初期表示としてデータベースの内容を表示
st.subheader("現在のデータベース内容")
df_from_db = load_data()

# 編集可能なデータフレームを表示（画面いっぱいに表示）
edited_df = st.data_editor(df_from_db, use_container_width=True)

# スタイルを適用してデータフレームの高さも最大にする
st.markdown("""
    <style>
        .stDataFrame {
            width: 100% !important;  /* 幅を画面いっぱいに */
            height: 90vh !important; /* 高さを画面いっぱいに調整 */
        }
    </style>
""", unsafe_allow_html=True)


# 編集内容をデータベースに反映するボタン
if st.sidebar.button('保存'):
    update_database(edited_df)  # 更新処理を関数呼び出しに変更

# データベースを全削除する関数
def clear_all_data():
    clear_table('info')
    st.warning("データベースがクリアされました")

# ALL CLEARボタン
if st.sidebar.button('ALL CLEAR'):
    clear_all_data()  # クリア処理を関数呼び出しに変更
