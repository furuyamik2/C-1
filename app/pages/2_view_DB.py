import streamlit as st
import pandas as pd
from DB.save_db import load_data, update_row
from DB.save_db import clear_table

# データベースの内容を表示
st.subheader("現在のデータベース内容")
df_from_db = load_data()
st.dataframe(df_from_db, use_container_width=True)

# 編集するためのフォーム
st.sidebar.subheader("データの編集")

# 編集する商品の選択
product_to_edit = st.sidebar.selectbox("編集する商品を選択", df_from_db['商品名'].tolist())

# 商品を選んだ後、編集可能なフォームを表示
selected_product = df_from_db[df_from_db['商品名'] == product_to_edit].iloc[0]

# 現在の情報を表示
product_name = st.sidebar.text_input("商品名", selected_product['商品名'])
price = st.sidebar.number_input("価格", value=selected_product['価格'], min_value=0)
quantity = st.sidebar.number_input("個数", value=selected_product['個数'], min_value=0)
category = st.sidebar.selectbox("カテゴリー", df_from_db['カテゴリー'].unique(), index=df_from_db['カテゴリー'].tolist().index(selected_product['カテゴリー']))
expiry_date = st.sidebar.date_input("消費期限", value=pd.to_datetime(selected_product['消費期限']).date())

# 編集内容を保存するボタン
if st.sidebar.button('保存'):
    # 編集内容をデータベースに反映
    updated_row = {
        '商品名': product_name,
        '価格': price,
        '個数': quantity,
        'カテゴリー': category,
        '消費期限': str(expiry_date)
    }
    
    # 商品情報をデータベースに更新する関数を呼び出し
    update_row('info', selected_product['商品名'], updated_row)
    st.sidebar.success(f"{product_name}の情報が更新されました。")

# ALL CLEARボタン
if st.sidebar.button('ALL CLEAR'):
    clear_table('info')

