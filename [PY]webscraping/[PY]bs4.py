#beautifulsoup4 scrapingする為のPKG
#lxml 　コードを分析するPKG

import requests
from bs4 import BeautifulSoup
#yahoo 天気の情報を持ってくる

url = "https://weather.yahoo.co.jp/weather/"
res = requests.get(url)
res.raise_for_status() #問題あったら、プログラム終了

soup = BeautifulSoup(res.text, "lxml") 
#html情報をlxmlを通して、BeautifulSoupの客体として作る
print(soup.title)
#htmlのtitleのelementを持ってくる
#出力結果：<title>Yahoo!天気・災害 - 天気予報 / 防災情報</title>
print(soup.title.get_text())
#htmlのtitleの文字のみ持ってくる
#出力結果：Yahoo!天気・災害 - 天気予報 / 防災情報
print(soup.a)
#soup客体で一番最初に見つかるaのelementを返す
#出力結果：<a id="pagetop" name="pagetop"></a>
print(soup.a.attrs)
#aのtag下の属性情報を返す
#出力結果：{'name': 'pagetop', 'id': 'pagetop'}
print(soup.a["name"])
#aのtag下のnameの値を出力
# #出力結果：pagetop
print(soup.a["id"])
#出力結果：pagetop
print(soup.find("h2", attrs={"class":"yjM"}))
#soup客体で、一番最初に見つかったh2のelementで、classがyjMのところを探して返す。
# 出力結果：<h2 class="yjM">今日のアメダスランキング</h2>

