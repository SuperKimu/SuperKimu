#what is my user agent ?
"""
https://www.whatismybrowser.com/detect/what-is-my-user-agent/
上のサイトにアクセスすると、どんなブラウザーで接続しているか、ユーザーの情報が確認できる


"""

import requests
url = "http://google.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}
#headersで、User Agent情報を入力することで、ブラウザーで開くときと同じ情報がHTML文章として持ち込める
#こうすることで、ちゃんとしたHTMLのファイルで、web scrapingができる
res = requests.get(url, headers=headers)
res.raise_for_status()
with open("google.html", "w", encoding="utf8") as f:
          f.write(res.text) 