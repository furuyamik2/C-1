# ライブラリのインポート
import streamlit as st
import os
from DB.save_db import load_data
from DB.save_db import clear_table

# 初期表示としてデータベースの内容を表示
st.subheader("現在のデータベース内容")
df_from_db = load_data()
st.dataframe(df_from_db, use_container_width=True)

if st.sidebar.button('ALL CLEAR'):
    clear_table('info')