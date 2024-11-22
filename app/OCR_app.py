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

# HTML コードを直接指定して表示
html_code = """
        <h1 style="color: blue; line-height: 1.2;">ようこそ、Food Trackerへ！</h1>
    <p style="line-height: 1.5;">このアプリは、食品や商品の情報を効率的に管理するために作られました。</p>
    <p style="line-height: 1.5;">商品名や価格、カテゴリーを登録するだけで、簡単にデータを整理・分類できます。</p>
    <p style="line-height: 1.5;">さらに、登録されたデータは検索や分析にも活用可能で、買い物や在庫管理に役立てることができます。</p>
    <p style="line-height: 1.5;">直感的なインターフェースで、初心者の方でもすぐに使いこなせます。ぜひ試してみてください！</p>
    <p style="line-height: 1.5;">今後、さらに便利な機能やカスタマイズオプションを追加予定です。皆さんのフィードバックをお待ちしています！</p>
"""
components.html(html_code) 

 # ファイルアップローダーを追加
uploaded_files = st.sidebar.file_uploader("Upload PDF files", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

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







