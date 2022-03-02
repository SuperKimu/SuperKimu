#beautifulsoup4 scrapingする為のPKG
#lxml 　コードを分析するPKG


import requests
from bs4 import BeautifulSoup
#yahooニュースのトピックス

url = "https://news.yahoo.co.jp/ranking/access/news"
res = requests.get(url)
res.raise_for_status() #問題あったら、プログラム終了

soup = BeautifulSoup(res.text, "lxml") 
#html情報をlxmlを通して、BeautifulSoupの客体として作る
print(soup.title.get_text())
#htmlのtitleの文字のみ持ってくる


#現在日付と時間
import datetime
now = datetime.datetime.today()
thistime = "今日は" + str(now.month) + "月" + str(now.day) + "日、現在時刻は" + str(now.hour) + "時"  + str(now.minute) + "分です。 只今の主なトピックス"
print(thistime)

print(".")
print(".")
print(".")

news1 = soup.find("li", attrs={"class":"sc-kjoXOD joqeOG yjnSubTopics_list_item"})
#soup客体で、一番最初に見つかったliのelementで、classの値がsc-kjoXOD joqeOG yjnSubTopics_list_itemのところを探して返す。
print("1 : " + news1.get_text())

news2 = news1.next_sibling
print("2 : " + news2.get_text())
#.next_siblingを使い、当初見つけたelementの次のelementへいける　previous_siblingは逆 、兄弟
#print(news1.parent) で、親elementへもいける
news3 = news2.next_sibling
print("3 : " + news3.get_text())

news4 = news3.next_sibling
print("4 : " + news4.get_text())

news5 = news4.next_sibling
print("5 : " + news5.get_text())

news6 = news5.next_sibling
print("6 : " + news6.get_text())

news7 = news6.next_sibling
print("7 : " + news7.get_text())

news8 = news7.next_sibling
print("8 : " + news8.get_text())

"""
3/2 22:28 出力結果

アクセスランキング（ニュース - 総合） - Yahoo!ニュース
今日は3月2日、現在時刻は22時27分です。 只今の主なトピックス
.
.
.
1 : 民間人計2000人超死亡 ウクライナ
2 : ウクライナ避難民受け入れへ 首相
3 : EU 露7銀行のSWIFT排除を発動
4 : プーチン氏 誤算でより強硬策に?
5 : たたずむだけ 露若者ひそかな抗議
6 : 河野氏 非難の投稿は「注意喚起」
7 : 名代富士そば 正しくは「なだい」
8 : テンダラー浜本 不倫認め謝罪

"""


"""参考
print(news1.find_next_siblings("li"))
で 同じelementに入ってるすべてのliの値を返すこともできる

"""