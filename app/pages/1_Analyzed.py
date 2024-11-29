import streamlit as st
import pandas as pd
from datetime import datetime
from DB.save_db import load_data

# 商品名と消費期限までの日数を表示する
def display_product_expiry():
    # データを読み込む
    df = load_data()

    # 現在の日付を取得
    today = datetime.today()

    # 消費期限カラムをdatetime型に変換
    df['消費期限'] = pd.to_datetime(df['消費期限'])

    # 商品名と消費期限までの日数を計算
    df['days_until_expiration'] = (df['消費期限'] - today).dt.days

    # 消費期限までの日数で昇順に並べ替え
    df_sorted = df.sort_values(by='days_until_expiration', ascending=True)

    # 商品ごとのメッセージを作成して、枠の色を変更して表示
    for index, row in df_sorted.iterrows():
        product_name = row['商品名']
        days_until_expiration = row['days_until_expiration']
        
        # 枠の色の設定 (日数に応じて枠線の色を変更)
        if days_until_expiration <= 3:
            border_color = '#B22222'  # ダーク赤
            bg_color = '#FFDDDD'  # 淡い赤
        elif days_until_expiration <= 7:
            border_color = '#FFD700'  # ゴールド
            bg_color = '#FFF9E6'  # 淡い黄色
        else:
            border_color = '#228B22'  # ダークグリーン
            bg_color = '#DDFFDD'  # 淡い緑
        
        # メッセージをHTML形式で表示（枠線の色とサイズを調整）
        message = f"""
        <div style='
            border: 3px solid {border_color}; 
            padding: 10px; 
            margin: 10px auto; 
            width: 80%; 
            text-align: center;
            border-radius: 12px;
            background-color: {bg_color};
            box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);'>
            <strong>{product_name}</strong><br>
            消費期限まであと{days_until_expiration}日
        </div>
        """
        
        # スタイルを適用して表示
        st.markdown(message, unsafe_allow_html=True)

# 商品名と消費期限までの日数を表示する
st.write('<h2>商品ごとの消費期限までの日数</h2>', unsafe_allow_html=True)
display_product_expiry() 

# Streamlitのボタンで表示
if st.sidebar.button('更新'):
    # 現在の表示を消してから新しい表示をする
    st.empty()  # 現在の表示をリセット
    display_product_expiry()  # 新しい内容を表示
