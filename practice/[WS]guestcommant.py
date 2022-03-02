import requests
from bs4 import BeautifulSoup
#yahooニュースのトピックス


#御宿野乃なんば　じゃらん　口コミ#
url = "https://www.jalan.net/yad395730/kuchikomi/?screenId=UWW3101&yadNo=395730&distCd=01&stayYear=&stayMonth=&stayDay=&dateUndecided=1&roomCount=1&roomCrack=000000"
res = requests.get(url)
res.raise_for_status() #問題あったら、プログラム終了

soup = BeautifulSoup(res.content, "lxml")  #BeautifulSoup(res.text, "lxml")で文字化けがする場合、BeautifulSoup(res.content, "lxml")にすると、95%は予防可能
#html情報をlxmlを通して、BeautifulSoupの客体として作る
print(soup.title.get_text())
#htmlのtitleの文字のみ持ってくる

commant1 = soup.find("p", attrs={"class":"jlnpc-kuchikomiCassette__postBody"})
#soup客体で、一番最初に見つかったliのelementで、classの値がsc-kjoXOD joqeOG yjnSubTopics_list_itemのところを探して返す。
print("1 : " + commant1.get_text())

commant2 = commant1.find_next_sibling("p")
print(commant2)

#最上段の口コミまでは読み込み成功(2022/3/2)