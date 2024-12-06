import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from DB.save_db import load_data

# フォント設定
from matplotlib import rcParams
rcParams["font.family"] = "IPAexGothic"  # 日本語フォント対応

# データのロード
df = load_data()
df.columns = df.columns.str.strip()  # 列名の余分なスペースを削除

def display_all_charts():
    # カテゴリー別の割合（円グラフ）
    st.header("カテゴリー別の割合")
    category_counts = df["Category"].value_counts()
    fig1, ax1 = plt.subplots(figsize=(6, 6))
    ax1.pie(
        category_counts.values,
        labels=category_counts.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=sns.color_palette("pastel"),
    )
    ax1.set_title("カテゴリーごとの商品割合", fontsize=14)
    st.pyplot(fig1)

    # 消費期限の分布（棒グラフ）
    st.header("消費期限の分布")
    df["Expiration Date"] = pd.to_datetime(df["Expiration Date"])
    expiration_counts = df["Expiration Date"].dt.to_period('M').value_counts().sort_index()
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    expiration_counts.plot(kind="bar", ax=ax2, color="skyblue")
    ax2.set_xlabel("消費期限（月）", fontsize=12)
    ax2.set_ylabel("商品数", fontsize=12)
    ax2.set_title("消費期限ごとの商品数", fontsize=14)
    ax2.tick_params(axis='x', rotation=45)
    st.pyplot(fig2)

    # 価格帯の分布（ヒストグラム）
    st.header("価格帯の分布")
    fig3, ax3 = plt.subplots(figsize=(8, 4))
    sns.histplot(df["Price"], bins=10, kde=False, color="salmon", ax=ax3)
    ax3.set_xlabel("価格帯", fontsize=12)
    ax3.set_ylabel("商品数", fontsize=12)
    ax3.set_title("価格帯ごとの商品分布", fontsize=14)
    st.pyplot(fig3)

    # 登録日の商品数の推移（折れ線グラフ）
    st.header("登録日の商品数の推移")
    df["Registration Date"] = pd.to_datetime(df["Registration Date"])
    registration_counts = df["Registration Date"].dt.date.value_counts().sort_index()
    fig4, ax4 = plt.subplots(figsize=(8, 4))
    ax4.plot(registration_counts.index, registration_counts.values, marker='o', color="green", linestyle='-')
    ax4.set_xlabel("登録日", fontsize=12)
    ax4.set_ylabel("商品数", fontsize=12)
    ax4.set_title("登録日ごとの追加商品数", fontsize=14)
    ax4.tick_params(axis='x', rotation=45)
    st.pyplot(fig4)

    # カテゴリー別の合計金額（棒グラフ）
    st.header("カテゴリーごとの合計金額")
    category_totals = df.groupby("Category")["Price"].sum()
    fig5, ax5 = plt.subplots(figsize=(8, 4))
    sns.barplot(x=category_totals.index, y=category_totals.values, palette="muted", ax=ax5)
    ax5.set_xlabel("カテゴリー", fontsize=12)
    ax5.set_ylabel("合計金額", fontsize=12)
    ax5.set_title("カテゴリー別の合計金額", fontsize=14)
    ax5.tick_params(axis='x', rotation=45)
    st.pyplot(fig5)

    # 個数別商品分布（棒グラフ）
    st.header("個数別商品分布")
    quantity_counts = df["個数"].value_counts().sort_index()
    fig6, ax6 = plt.subplots(figsize=(8, 4))
    quantity_counts.plot(kind="bar", ax=ax6, color="purple")
    ax6.set_xlabel("個数", fontsize=12)
    ax6.set_ylabel("商品数", fontsize=12)
    ax6.set_title("個数ごとの商品分布", fontsize=14)
    st.pyplot(fig6)

if __name__ == "__main__":
    display_all_charts()
