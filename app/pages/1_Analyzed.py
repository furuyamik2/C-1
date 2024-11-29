import streamlit as st
import pandas as pd
from DB.save_db import load_data
from datetime import datetime

# 商品名と消費期限までの日数を表示
def display_product_expiry():
    # データを読み込む
    df = load_data()

    # 現在の日付を取得
    today = datetime.today()

    # 消費期限カラムをdatetime型に変換
    df['消費期限'] = pd.to_datetime(df['消費期限'])

    # 商品名と消費期限までの日数を計算
    df['days_until_expiration'] = (df['消費期限'] - today).dt.days

    # 商品名と消費期限までの日数を表示する
    st.write('<h2>商品ごとの消費期限までの日数</h2>', unsafe_allow_html=True)

    # 商品ごとのメッセージを作成して表示
    for index, row in df.iterrows():
        product_name = row['商品名']
        days_until_expiration = row['days_until_expiration']
        message = f"<h4>{product_name}の消費期限まであと{days_until_expiration}日<h4>"
        st.write(message)

display_product_expiry()

# Streamlitのボタンで更新処理
if st.button("更新"):
    display_product_expiry()
