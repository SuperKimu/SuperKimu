# requests
"""
web scraping は webでほしい情報を抽出する行為。
その為、HTML文章の情報が必要 → それをもってくるとき、
使うライブラリがrequests
最初使うときは、要インストール、pip install requests
"""

import abc
import requests
url = requests.get("http://google.com")
# http://google.comからもってきた情報を、url変数に入れる
print("応答コード :", url.status_code) #応答コード 、200が出たら、正常
#403は、接続権限無し
if url.status_code == requests.codes.ok: #requestsの結果が200だったら、問題なかったら
          print("正常です")
else:
          print("問題があります。")

url.raise_for_status() #問題なかったら、プログラム実行、問題あったら、プログラム終了
print("web scrapingを実行します")

"""
import requests
url = requests.get("http://google.com")
url.raise_for_status()

こちらが基本コードセット
"""
print(len(url.text)) #google.com で使われた文字の数
print(url.text)

with open("google.html", "w", encoding="utf-8") as abc: 
          abc.write(url.text)  #url.textを、書くモード, utf-8の規格にして、google.htmlに保存
          