import pdfplumber
import pandas as pd
import re

# PDFファイルのパス
pdf_path = 'list.pdf'

# データを格納するリスト
data = []

# PDFを開く
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        # テキストを抽出
        text = page.extract_text()
        # データの始まりを特定して分割
        if "品目名" in text:
            lines = text.split('\n')
            for line in lines:
                # 行を分割してリストに格納
                cells = line.split()
                # 必要な列（品目名と貯蔵限界）だけ抽出
                if len(cells) > 5:
                    item_name = cells[0]
                    storage_limit = cells[3]  # 貯蔵限界の列を指定
                    data.append([item_name, storage_limit])

# データフレームに変換
df = pd.DataFrame(data[1:], columns=data[0])
df = df.rename(columns={'品目名': 'name', '貯蔵限界': 'limit'})


def calculate_average_days(storage_limit):
    # 貯蔵限界の文字列から数値を抽出
    numbers = [float(num) for num in re.findall(r'\d+\.?\d*', storage_limit)]
    if not numbers:
        return None  # 数値がない場合は None
    
    # 数値の平均を計算（整数に変換）
    avg = int(sum(numbers) // len(numbers))
    
    # 単位に応じて変換
    if "月" in storage_limit:
        return avg * 30  # 月を日数に変換
    elif "週" in storage_limit:
        return avg * 7   # 週を日数に変換
    elif "日" in storage_limit:
        return avg       # すでに日数なのでそのまま
    else:
        return None      # 単位がない場合は None

df['number'] = df['limit'].apply(calculate_average_days)

df = df.groupby("name", as_index=False).agg({"number": "mean", "limit": "first"})
df = df[df['name'] != 'トマト(緑熟)']
df = df.drop('limit', axis=1)
df.to_csv('vege_list.csv')
