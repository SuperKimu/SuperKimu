from posixpath import commonpath
import requests
from bs4 import BeautifulSoup

url = "https://travel.rakuten.co.jp/HOTEL/158346/review.html"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.content, "lxml")
commants = soup.find_all("p", attrs={"class":"commentSentence"})

guest1 = commants[0].get_text()
guest2 = commants[2].get_text()
guest3 = commants[4].get_text()
guest4 = commants[6].get_text()
guest5 = commants[8].get_text()

staff1 = commants[1].get_text()
staff2 = commants[3].get_text()
staff3 = commants[5].get_text()
staff4 = commants[7].get_text()
staff5 = commants[9].get_text()


print(guest1)
print(" ")
print(staff1)
print(" ")
print(guest2)
print(" ")
print(staff2)
print(" ")
print(guest3)
print(" ")
print(staff3)
print(" ")
print(guest4)
print(" ")
print(staff5)
print(" ")
print(guest5)
print(" ")
print(staff5)
print(" ")
