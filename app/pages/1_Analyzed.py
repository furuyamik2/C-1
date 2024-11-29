import streamlit as st
import pandas as pd
from datetime import datetime
from DB.save_db import load_data, delete_row  

def display_product_expiry():
    # データを読み込む
    df = load_data()

    # 列名の確認と空白を取り除く
    df.columns = df.columns.str.strip()

    # 現在の日付を取得
    today = datetime.today()

    # 消費期限カラムをdatetime型に変換
    df['消費期限'] = pd.to_datetime(df['消費期限'])

    # 商品名と消費期限までの日数を計算
    df['days_until_expiration'] = (df['消費期限'] - today).dt.days

    # 消費期限までの日数で昇順に並べ替え
    df_sorted = df.sort_values(by='days_until_expiration', ascending=True)

    # 商品ごとのデータを3列に分けて表示
    columns = st.columns(3)  # 3列のレイアウトを作成

    for index, row in df_sorted.iterrows():
        product_name = row['商品名']
        days_until_expiration = row['days_until_expiration']

        # 枠の色の設定
        if days_until_expiration <= 3:
            border_color = '#B22222'  # ダーク赤
            bg_color = '#FFDDDD'  # 淡い赤
        elif days_until_expiration <= 7:
            border_color = '#FFD700'  # ゴールド
            bg_color = '#FFF9E6'  # 淡い黄色
        else:
            border_color = '#228B22'  # ダークグリーン
            bg_color = '#DDFFDD'  # 淡い緑

        # 商品ごとのHTMLを作成
        card_html = f"""
        <div style='
            border: 2px solid {border_color}; 
            padding: 10px; 
            margin: 10px auto; 
            text-align: center;
            border-radius: 10px;
            background-color: {bg_color};
            box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.1);'>
            <strong style='font-size: 1.1em;'>{product_name}</strong><br>
            <span style='font-size: 0.9em;'>消費期限まであと{days_until_expiration}日</span>
        </div>
        """

        # カードを順に3列に割り当てて表示
        column_index = index % 3
        with columns[column_index]:
            st.markdown(card_html, unsafe_allow_html=True)
            # 削除ボタンを追加
            if st.button(f"削除: {product_name}", key=f"delete_{index}"):
                delete_row(product_name)  # 削除関数の呼び出し
                st.experimental_rerun()  # 再読み込みして表示を更新

# 商品名と消費期限までの日数を表示する
st.write('<h2>商品ごとの消費期限までの日数</h2>', unsafe_allow_html=True)
display_product_expiry()