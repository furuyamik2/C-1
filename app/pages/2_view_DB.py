import streamlit as st
import pandas as pd
from DB.save_db import load_data, update_row, clear_table

# 初期表示としてデータベースの内容を表示
st.subheader("現在のデータベース内容")
df_from_db = load_data()

# 編集可能なデータフレームを表示
edited_df = st.data_editor(df_from_db)

# 編集されたデータフレームを表示
st.dataframe(edited_df, use_container_width=True)

# 編集内容をデータベースに反映するボタン
if st.button('保存'):
    # 編集後のデータフレームをデータベースに更新
    for index, row in edited_df.iterrows():
        updated_row = {
            '商品名': row['商品名'],
            '価格': row['価格'],
            '個数': row['個数'],
            'カテゴリー': row['カテゴリー'],
            '消費期限': row['消費期限']
        }
        # 商品名をキーにしてデータベースに更新
        update_row('info', row['商品名'], updated_row)
    st.success("データベースが更新されました")

# ALL CLEARボタン
if st.sidebar.button('ALL CLEAR'):
    clear_table('info')
    st.warning("データベースがクリアされました")
