import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from DB.save_db import load_data

# 日本語フォント設定（文字化け防止）
from matplotlib import rcParams
rcParams["font.family"] = "IPAexGothic"

# データのロード
df = load_data()
df.columns = df.columns.str.strip()  # 列名の余分なスペースを削除

# 表示用ラベル（日本語 → 英語）
label_map = {
    "カテゴリー": "Category",
    "消費期限": "Expiration Date",
    "価格": "Price",
    "登録日": "Registration Date",
    "個数": "Quantity",
}

# 日本語カラム → 英語ラベル変換
def get_label(col_name):
    return label_map.get(col_name, col_name)  # マッピングがない場合は元の名前

# グラフ表示関数
def plot_pie(data, column, title):
    counts = data[column].value_counts()
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(
        counts.values,
        labels=counts.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=sns.color_palette("pastel"),
    )
    ax.set_title(title, fontsize=14)
    st.pyplot(fig)

def plot_bar(data, x_col, y_col, title):
    totals = data.groupby(x_col)[y_col].sum()
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(x=totals.index, y=totals.values, palette="muted", ax=ax)
    ax.set_xlabel(get_label(x_col), fontsize=12)
    ax.set_ylabel(get_label(y_col), fontsize=12)
    ax.set_title(title, fontsize=14)
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

def plot_histogram(data, column, bins, title):
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(data[column], bins=bins, kde=False, color="salmon", ax=ax)
    ax.set_xlabel(get_label(column), fontsize=12)
    ax.set_ylabel("Number of Products", fontsize=12)
    ax.set_title(title, fontsize=14)
    st.pyplot(fig)

def plot_line(data, column, title):
    counts = data[column].dt.date.value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(counts.index, counts.values, marker='o', color="green", linestyle='-')
    ax.set_xlabel(get_label(column), fontsize=12)
    ax.set_ylabel("Number of Products", fontsize=12)
    ax.set_title(title, fontsize=14)
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

# メイン関数
def display_all_charts():
    # カテゴリー別の割合（円グラフ）
    st.header("Category Proportions")
    plot_pie(df, "カテゴリー", "Proportion of Products by Category")

    # 消費期限の分布（棒グラフ）
    st.header("Expiration Date Distribution")
    df["消費期限"] = pd.to_datetime(df["消費期限"])
    expiration_counts = df["消費期限"].dt.to_period('M').value_counts().sort_index()
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    expiration_counts.plot(kind="bar", ax=ax2, color="skyblue")
    ax2.set_xlabel(get_label("消費期限 (Month)"), fontsize=12)
    ax2.set_ylabel("Number of Products", fontsize=12)
    ax2.set_title("Products by Expiration Date", fontsize=14)
    ax2.tick_params(axis='x', rotation=45)
    st.pyplot(fig2)

    # 価格帯の分布（ヒストグラム）
    st.header("Price Distribution")
    plot_histogram(df, "価格", bins=10, title="Product Distribution by Price Range")

    # 登録日の商品数の推移（折れ線グラフ）
    st.header("Product Addition Trend by Registration Date")
    df["登録日"] = pd.to_datetime(df["登録日"])
    plot_line(df, "登録日", "Number of Products Added by Date")

    # カテゴリー別の合計金額（棒グラフ）
    st.header("Total Price by Category")
    plot_bar(df, "カテゴリー", "価格", "Total Price by Category")

# アプリ実行
if __name__ == "__main__":
    display_all_charts()
