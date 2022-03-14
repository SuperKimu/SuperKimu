import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=758037&weekday=mon"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("td", attrs={"class":"title"})
title = cartoons[1].a.get_text()
link = cartoons[1].a["href"]
print(title)
print("https://comic.naver.com"+link)

"""出力
69화
https://comic.naver.com/webtoon/detail?titleId=758037&no=69&weekday=mon
"""


for cartoon in cartoons: #反復
          title = cartoon.a.get_text()
          link = "https://comic.naver.com" + cartoon.a["href"]
          print(title, link)

"""出力
70화 https://comic.naver.com/webtoon/detail?titleId=758037&no=70&weekday=mon
69화 https://comic.naver.com/webtoon/detail?titleId=758037&no=69&weekday=mon
68화 https://comic.naver.com/webtoon/detail?titleId=758037&no=68&weekday=mon
67화 https://comic.naver.com/webtoon/detail?titleId=758037&no=67&weekday=mon
66화 https://comic.naver.com/webtoon/detail?titleId=758037&no=66&weekday=mon
65화 https://comic.naver.com/webtoon/detail?titleId=758037&no=65&weekday=mon
64화 https://comic.naver.com/webtoon/detail?titleId=758037&no=64&weekday=mon
63화 https://comic.naver.com/webtoon/detail?titleId=758037&no=63&weekday=mon
62화 https://comic.naver.com/webtoon/detail?titleId=758037&no=62&weekday=mon
61화 https://comic.naver.com/webtoon/detail?titleId=758037&no=61&weekday=mon

"""

#点数情報

total_rates = 0
points = soup.find_all("div",attrs={"class":"rating_type"})
for point in points:
          rate = point.find("strong").get_text()
          print(rate)
          total_rates += float(rate)
print(" 合計点数 :", total_rates)
print(" 平均点数 :", total_rates/ len(points))