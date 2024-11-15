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
selected_option = option_menu(**const.OPTION_MENU_CONFIG)

# HTML コードを直接指定して表示
html_code = """
    <h1 style="color: blue;">Hello, Streamlit!</h1>
    <p>これは直接 Streamlit に書き込んだ HTML コードの表示例です。</p>
    <p>CSS や JavaScript を含む内容も表示できます。</p>
"""
components.html(html_code, height=300) 

 # ファイルアップローダーを追加
uploaded_files = st.file_uploader("Upload PDF files", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

# OCRに関する実装
if uploaded_files:
    st.write(f"{len(uploaded_files)} ファイルがアップロードされました。")
    
    # 出力ファイル名を入力
    output_folder = os.getcwd()
    output_filename = st.text_input("Enter output file name", value="ocr_results.csv", placeholder="ocr_results.csv")
    
    # OCR実行ボタン
    if st.button('Run OCR'):
        # OCRを実行してCSVファイルを生成
        output_file, concat_df = ocr_to_csv(uploaded_files, output_folder, output_filename)
        csv_to_sql(output_file, 'info')
        st.success("OCR completed!")
        
        # OCR結果を表示
        st.dataframe(concat_df, use_container_width=True)
# メニューごとのコンテンツ表示
if selected_option == "OCR":
    st.title("OCR セクション")
    st.write("ここではOCRに関する情報を扱います。")

elif selected_option == "DataBase":
    st.title("データベース セクション")
    st.write("ここではデータベースに関する情報を扱います。")
    # データベースに関する実装を追加

elif selected_option == "Other":
    st.title("その他のセクション")
    st.write("ここではその他の情報を表示します。")






