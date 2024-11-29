# ライブラリのインポート
import streamlit as st
import os
from ocr_function import ocr_to_csv
from DB.save_db import csv_to_sql
from DB.save_db import load_data
import streamlit.components.v1 as components
import const
from streamlit_option_menu import option_menu

st.set_page_config(**const.SET_PAGE_CONFIG)

# APP タイトル
st.title('Food Tracker')
st.markdown(const.HIDE_ST_STYLE, unsafe_allow_html=True)


 # ファイルアップローダーを追加
uploaded_files = st.file_uploader("Upload PDF files", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

# OCRに関する実装
if uploaded_files:
    st.sidebar.write(f"{len(uploaded_files)} ファイルがアップロードされました。")
    
    # 出力ファイル名を入力
    output_folder = os.getcwd()
    output_filename = "ocr_results.csv"

   

    # OCR実行ボタン
    if st.sidebar.button('Run OCR'):
        
        with st.spinner('OCRを実行中...'):
            # OCRを実行してCSVファイルを生成
            output_file, concat_df = ocr_to_csv(uploaded_files, output_folder, output_filename)
            csv_to_sql(output_file, 'info')
    
        
        st.success("OCR completed!")
        
        # OCR結果を表示
        st.dataframe(concat_df, use_container_width=True)







