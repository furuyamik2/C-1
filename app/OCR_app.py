# ライブラリのインポート
import streamlit as st
import os
from ocr_function import ocr_to_csv
from DB.save_db import csv_to_sql
from DB.save_db import load_data


# APP タイトル
st.title('Food Tracker')

# サイドバーにファイルアップローダーを追加
uploaded_files = st.sidebar.file_uploader("Upload PDF files", type=["jpg", "jpeg", "png"], accept_multiple_files=True)


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
            if st.sidebar.button('Save'):
                csv_to_sql(output_file, 'info')
                st.success("データベースに保存されました。")
