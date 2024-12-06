import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from DB.save_db import load_data
from matplotlib import rcParams

def display_all_charts():
    # 日本語フォントを設定
    rcParams["font.family"] = "Noto Sans CJK JP"  # 必要に応じて他のフォントを設定

    # データを読み込む
    df = load_data()
    df.columns = df.columns.str.strip()

    # グラフ設定（スタイリッシュに）
    sns.set_theme(style="whitegrid", palette="pastel")

    # カテゴリー別の商品割合（円グラフ）
    st.subheader("カテゴリー別の商品割合")
    category_counts = df["カテゴリー"].value_counts()
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    ax1.pie(
        category_counts, 
        labels=category_counts.index, 
        autopct="%1.1f%%", 
        startangle=90, 
        colors=sns.color_palette("pastel")
    )
    ax1.set_title("カテゴリーの割合", fontsize=14)
    ax1.axis("equal")
    st.pyplot(fig1)

    st.divider()

    # 消費期限の分布（棒グラフ）
    st.subheader("消費期限の分布")
    df["消費期限"] = pd.to_datetime(df["消費期限"])
    expiry_counts = df["消費期限"].value_counts().sort_index()
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    sns.barplot(x=expiry_counts.index, y=expiry_counts.values, palette="pastel", ax=ax2)
    ax2.set_xlabel("消費期限", fontsize=12)
    ax2.set_ylabel("商品数", fontsize=12)
    ax2.set_title("消費期限ごとの商品数", fontsize=14)
    ax2.tick_params(axis="x", rotation=45)
    st.pyplot(fig2)

    st.divider()

    # 価格帯の分布（ヒストグラム）
    st.subheader("価格帯の分布")
    fig3, ax3 = plt.subplots(figsize=(8, 4))
    sns.histplot(df["価格"], bins=10, kde=True, color="skyblue", ax=ax3)
    ax3.set_xlabel("価格帯", fontsize=12)
    ax3.set_ylabel("商品数", fontsize=12)
    ax3.set_title("価格帯ごとの商品分布", fontsize=14)
    st.pyplot(fig3)

    st.divider()

    # 登録日の商品数の推移（折れ線グラフ）
    st.subheader("登録日ごとの追加商品数の推移")
    df["登録日"] = pd.to_datetime(df["登録日"])
    daily_counts = df["登録日"].dt.date.value_counts().sort_index()
    fig4, ax4 = plt.subplots(figsize=(8, 4))
    sns.lineplot(x=daily_counts.index, y=daily_counts.values, marker="o", ax=ax4, color="coral")
    ax4.set_xlabel("登録日", fontsize=12)
    ax4.set_ylabel("追加商品数", fontsize=12)
    ax4.set_title("登録日ごとの商品数推移", fontsize=14)
    ax4.tick_params(axis="x", rotation=45)
    st.pyplot(fig4)

    st.divider()

    # カテゴリー別の合計金額（棒グラフ）
    st.subheader("カテゴリーごとの合計金額")
    category_totals = df.groupby("カテゴリー")["価格"].sum()
    fig5, ax5 = plt.subplots(figsize=(8, 4))
    sns.barplot(x=category_totals.index, y=category_totals.values, palette="muted", ax=ax5)
    ax5.set_xlabel("カテゴリー", fontsize=12)
    ax5.set_ylabel("合計金額", fontsize=12)
    ax5.set_title("カテゴリーごとの価格合計", fontsize=14)
    ax5.tick_params(axis="x", rotation=45)
    st.pyplot(fig5)

    st.divider()

    # 個数別商品分布（棒グラフ）
    st.subheader("個数別商品分布")
    quantity_counts = df["個数"].value_counts().sort_index()
    fig6, ax6 = plt.subplots(figsize=(8, 4))
    sns.barplot(x=quantity_counts.index, y=quantity_counts.values, palette="cool", ax=ax6)
    ax6.set_xlabel("個数", fontsize=12)
    ax6.set_ylabel("商品数", fontsize=12)
    ax6.set_title("個数ごとの商品数分布", fontsize=14)
    st.pyplot(fig6)

if __name__ == "__main__":
    display_all_charts()
