from re import T
import requests
from bs4 import BeautifulSoup

url = "https://www.jalan.net/yad395730/kuchikomi/?screenId=UWW3001&yadNo=395730&smlCd=272902&distCd=01"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.content, "lxml")
commants = soup.find_all("p", attrs={"class":"jlnpc-kuchikomiCassette__postBody"})

guest1 = commants[0].get_text()
guest2 = commants[1].get_text()
guest3 = commants[2].get_text()
guest4 = commants[3].get_text()
guest5 = commants[4].get_text()

print(guest1)
print("")
print(guest2)
print("")
print(guest3)
print("")
print(guest4)
print("")
print(guest5)
