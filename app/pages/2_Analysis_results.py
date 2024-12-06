import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams
from DB.save_db import load_data
import japanize_matplotlib

# フォント設定（日本語対応）
plt.rcParams['font.family'] = 'IPAexGothic'  # 日本語フォント（例: IPAexGothic）

def display_all_charts():
    # データを読み込む
    df = load_data()
    df.columns = df.columns.str.strip()

    # レイアウト: 2列
    col1, col2 = st.columns(2)

    # カテゴリー別の商品割合（円グラフ）
    with col1:
        st.write("カテゴリー別の商品割合")
        category_counts = df["カテゴリー"].value_counts()
        fig1, ax1 = plt.subplots(figsize=(5, 3))
        ax1.pie(category_counts, labels=category_counts.index, autopct="%1.1f%%", startangle=90)
        ax1.axis("equal")
        st.pyplot(fig1)

    # 消費期限の分布（棒グラフ）
    with col2:
        st.write("消費期限の分布")
        df["消費期限"] = pd.to_datetime(df["消費期限"])
        expiry_counts = df["消費期限"].value_counts().sort_index()
        fig2, ax2 = plt.subplots(figsize=(5, 3))
        expiry_counts.plot(kind="bar", ax=ax2)
        ax2.set_xlabel("消費期限")
        ax2.set_ylabel("商品数")
        st.pyplot(fig2)

    # 価格帯の分布（ヒストグラム）
    with col1:
        st.write("価格帯の分布")
        fig3, ax3 = plt.subplots(figsize=(5, 3))
        sns.histplot(df["価格"], bins=10, kde=False, ax=ax3)
        ax3.set_xlabel("価格帯")
        ax3.set_ylabel("商品数")
        st.pyplot(fig3)

    # 登録日の商品数の推移（折れ線グラフ）
    with col2:
        st.write("登録日ごとの追加商品数の推移")
        df["登録日"] = pd.to_datetime(df["登録日"])
        daily_counts = df["登録日"].dt.date.value_counts().sort_index()
        fig4, ax4 = plt.subplots(figsize=(5, 3))
        daily_counts.plot(kind="line", ax=ax4)
        ax4.set_xlabel("登録日")
        ax4.set_ylabel("追加商品数")
        st.pyplot(fig4)

    # カテゴリー別の合計金額（棒グラフ）
    with col1:
        st.write("カテゴリーごとの合計金額")
        category_totals = df.groupby("カテゴリー")["価格"].sum()
        fig5, ax5 = plt.subplots(figsize=(5, 3))
        category_totals.plot(kind="bar", ax=ax5)
        ax5.set_xlabel("カテゴリー")
        ax5.set_ylabel("合計金額")
        st.pyplot(fig5)

    # 個数別商品分布（棒グラフ）
    with col2:
        st.write("個数別商品分布")
        quantity_counts = df["個数"].value_counts().sort_index()
        fig6, ax6 = plt.subplots(figsize=(5, 3))
        quantity_counts.plot(kind="bar", ax=ax6)
        ax6.set_xlabel("個数")
        ax6.set_ylabel("商品数")
        st.pyplot(fig6)

if __name__ == "__main__":
    display_all_charts()
