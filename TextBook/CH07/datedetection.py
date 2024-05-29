import re
from datetime import datetime

# 現在の日時を取得
now = datetime.now()
current_date = now.strftime("%d/%m/%Y")

# 日付の正規表現パターン
date_pattern = r"\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(19|20)\d{2}\b"

# テストする文字列
text = f"今日は{current_date}です。昨日は28/05/2024でした。"

# 日付を抽出して表示
dates = re.findall(date_pattern, text)
formatted_dates = ["/".join(date) for date in dates]

print("抽出された日付:", formatted_dates)
