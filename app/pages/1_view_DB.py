# ライブラリのインポート
import streamlit as st
import os
from ocr_function import ocr_to_csv
from DB.save_db import csv_to_sql
from DB.save_db import load_data

# 初期表示としてデータベースの内容を表示
st.subheader("現在のデータベース内容")
df_from_db = load_data()
st.dataframe(df_from_db, use_container_width=True)

if st.sidebar.button('Reroll'):
    # 更新されたデータベースの内容を再表示
    df_from_db = load_data()
    st.subheader("更新されたデータベース内容")
    st.dataframe(df_from_db, use_container_width=True)