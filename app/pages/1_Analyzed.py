import streamlit as st
import pandas as pd
from datetime import datetime
from DB.save_db import load_data

# 商品名と消費期限までの日数を参列で表示する
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

    # 全体をグリッド表示のコンテナにする
    st.markdown("""
    <style>
        .grid-container {
            display: grid;
            grid-template-columns: repeat(3, 1fr); /* 3列表示 */
            gap: 20px;
            margin: 20px 0;
        }
        .grid-item {
            border: 2px solid;
            border-radius: 10px;
            padding: 10px;
            text-align: center;
            box-shadow: 1px 1px 6px rgba(0, 0, 0, 0.1);
        }
        .red-border { border-color: #B22222; background-color: #FFDDDD; }
        .yellow-border { border-color: #FFD700; background-color: #FFF9E6; }
        .green-border { border-color: #228B22; background-color: #DDFFDD; }
        .product-name {
            font-size: 1.2em; /* 商品名を少し大きく表示 */
            font-weight: bold;
        }
        .expiration-info {
            font-size: 0.9em; /* 消費期限情報を少し小さく */
            margin-top: 5px;
        }
    </style>
    """, unsafe_allow_html=True)

    # 商品ごとのカードを作成してグリッドで表示
    st.markdown('<div class="grid-container">', unsafe_allow_html=True)
    for index, row in df_sorted.iterrows():
        product_name = row['商品名']
        days_until_expiration = row['days_until_expiration']

        # 枠の色の設定
        if days_until_expiration <= 3:
            border_class = 'red-border'
        elif days_until_expiration <= 7:
            border_class = 'yellow-border'
        else:
            border_class = 'green-border'

        # 商品ごとのカードHTML
        item_html = f"""
        <div class="grid-item {border_class}">
            <div class="product-name">{product_name}</div>
            <div class="expiration-info">あと{days_until_expiration}日</div>
        </div>
        """
        st.markdown(item_html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 商品名と消費期限までの日数を表示する
st.write('<h2>商品ごとの消費期限までの日数</h2>', unsafe_allow_html=True)
display_product_expiry() 

# Streamlitのボタンで表示
if st.sidebar.button('更新'):
    # 現在の表示を消してから新しい表示をする
    st.empty()  # 現在の表示をリセット
    display_product_expiry()  # 新しい内容を表示
