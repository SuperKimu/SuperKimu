import requests
from bs4 import BeautifulSoup

url ="https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("a", attrs={"class":"title"})
#soupファイルの中で、tag名がaでclassの属性がtitleである全ての値を持ってくる
for cartoon in cartoons: #反復
          print(cartoon.get_text())