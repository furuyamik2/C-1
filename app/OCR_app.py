# ライブラリのインポート
import streamlit as st
import pandas as pd
import os
import sqlite3
from ocr_function import ocr_to_csv
from DB.save_db import csv_to_sql


# APP タイトル
st.title('Food Tracker')

# サイドバーにファイルアップローダーを追加
uploaded_files = st.sidebar.file_uploader("Upload PDF files", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

    # データベースの内容を取得する関数
def load_data():
    conn = sqlite3.connect('./DB/food_info.db')
    df = pd.read_sql("SELECT * FROM info", conn)
    conn.close()
    return df

# 初期表示としてデータベースの内容を表示
st.subheader("現在のデータベース内容")
df_from_db = load_data()
st.dataframe(df_from_db, use_container_width=True)

if uploaded_files:
    st.sidebar.write(f"{len(uploaded_files)} ファイルがアップロードされました。")
    
    # 出力ファイル名を入力
    output_folder = os.getcwd()
    output_filename = st.text_input("Enter output file name", value="ocr_results.csv", placeholder="ocr_results.csv")
    
    # OCR実行ボタン
    if st.sidebar.button('Run OCR'):
        # OCRを実行してCSVファイルを生成
        output_file, concat_df = ocr_to_csv(uploaded_files, output_folder, output_filename)
        st.success("OCR completed!")
        
        # OCR結果を表示
        st.dataframe(concat_df, use_container_width=True)
        
        # 保存ボタン
        with open(output_file, 'rb') as f:
            st.download_button('Download CSV', f, file_name=output_filename)
            
            st.success("データベースに保存されました。")

            # 更新されたデータベースの内容を再表示
            df_from_db = load_data()
            st.subheader("更新されたデータベース内容")
            st.dataframe(df_from_db, use_container_width=True)
