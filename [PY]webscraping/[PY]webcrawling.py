from sys import dllhandle
from urllib.request import urlopen #url.requestのライブラリからのurlopen関数を持ってくる
from bs4 import BeautifulSoup #bs4のライブラリから 、BeautifulSoup関数を持ってくる
#pythonインストール後、初めて利用するときは、pip install BeautifulSoup4　で　インストール



html = urlopen("https://travel.rakuten.co.jp/HOTEL/158346/review.html")

bsobject = BeautifulSoup(html, "html.parser")

# a href = リンク名、リンク先
for link in bsobject.find_all('title'):
               print(link.text.strip(), link.get('commentSentence'))

# #img src = イメージ名、イメージリンク先
# for link in bsobject.find_all('img'):
#           print(link.text.strip(), link.get('src'))