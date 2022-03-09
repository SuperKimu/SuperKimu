import requests
from bs4 import BeautifulSoup

url = "https://www.jalan.net/yad395730/kuchikomi/?screenId=UWW3001&yadNo=395730&smlCd=272902&distCd=01"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.content, "lxml")
commants = soup.find_all("p", attrs={"class":"jlnpc-kuchikomiCassette__postBody"})

for commant in commants:
    print(commant.get_text())