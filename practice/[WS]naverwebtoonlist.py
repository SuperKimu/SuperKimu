import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("a", attrs={"class":"title"})
#class の 属性　が　title　である　全ての　"a" の　elementを　返す
for cartoon in cartoons:
    print(cartoon.get_text())