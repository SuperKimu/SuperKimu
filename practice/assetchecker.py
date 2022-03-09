#現在のbitcoin、ethereum、rippleの資産合計を円にして、GUIで表す

#現在日付と時間
import datetime
from sys import float_repr_style
now = datetime.datetime.today()
thistime = "本日は" + str(now.month) + "月" + str(now.day) + "日で、現在時刻は" + str(now.hour) + "時"  + str(now.minute) + "分です。"
print(thistime)

#2022.2.23
bit = float(0.02507351)
xrp = 10
ethereum = 0.05506036

import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/finance/quote/BTC-JPY"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.content, "lxml")
realbit = soup.find("div", attrs={"class":"YMlKec fxKbKc"}).get_text()
print("現在1ビットコインの値段は"+realbit+"円です。")


url1 = "https://www.google.com/finance/quote/ETH-JPY"
res = requests.get(url1)
res.raise_for_status()

soup = BeautifulSoup(res.content, "lxml")
realeth = soup.find("div", attrs={"class":"YMlKec fxKbKc"}).get_text()
print("現在1イーサリアムの値段は"+realeth+"円です。")


url2 = "https://www.google.com/finance/quote/XRP-JPY"
res = requests.get(url2)
res.raise_for_status()

soup = BeautifulSoup(res.content, "lxml")
realxrp = soup.find("div", attrs={"class":"YMlKec fxKbKc"}).get_text()
print("現在1リップルの値段は"+realxrp+"円です。")