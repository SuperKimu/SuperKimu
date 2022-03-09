from posixpath import commonpath
import requests
from bs4 import BeautifulSoup

url = "https://travel.rakuten.co.jp/HOTEL/158346/review.html"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.content, "lxml")
commants = soup.find_all("p", attrs={"class":"commentSentence"})

for commant in commants:
    print(commant.get_text())