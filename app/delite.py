import sqlite3

# データベースに接続
db = sqlite3.connect('vege_info.db')
print('接続')

# カーソルを作成
cur = db.cursor()

# テーブルの削除
cur.execute('DROP TABLE IF EXISTS vege_limit')

# コミットして変更を保存
db.commit()

# 接続を閉じる
cur.close()
db.close()
print('テーブル削除と接続解除')