import streamlit as st
import sqlite3
import pandas as pd
from DB.save_db import load_data, clear_table,update_database



# 初期表示としてデータベースの内容を表示
st.subheader("現在のデータベース内容")
df_from_db = load_data()

# 編集可能なデータフレームを表示（画面いっぱいに表示）
edited_df = st.data_editor(df_from_db, use_container_width=True)


# 編集内容をデータベースに反映するボタン
if st.button('保存'):
    update_database(edited_df)  # 更新処理を関数呼び出しに変更
    st.success("データが更新されました")


# ALL CLEARボタン
if st.sidebar.button('ALL CLEAR'):
    clear_table('info')  # クリア処理を関数呼び出しに変更
    st.success("データが削除されました")
