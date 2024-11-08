# ライブラリのインポート
import streamlit as st
import pandas as pd
import os
import base64
import requests
from io import StringIO
from datetime import datetime
from PIL import Image
import sqlite3
from ocr_function import ocr_to_csv
from DB.save_db import csv_to_sql

# APP
st.title('Food Tracker')

# サイドバー
uploaded_files = st.sidebar.file_uploader("Upload PDF files", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files:
    st.sidebar.write(f"{len(uploaded_files)} ファイルがアップロードされました。")

    output_folder = os.getcwd()
    output_filename = st.text_input("Enter output file name", value="ocr_results.csv", placeholder="ocr_results.csv")
    
    if st.sidebar.button('Run OCR'):
        # OCRを実行してCSVファイルを生成
        output_file, concat_df = ocr_to_csv(uploaded_files, output_folder, output_filename)
        st.success("OCR completed!")
        
        # OCR結果を表示
        st.dataframe(concat_df, use_container_width=True)

        # CSVをデータベースに保存
        with open(output_file, 'rb') as f:
            if st.sidebar.button('Save'):

