from cgitb import reset
import requests
import re #正規式
from bs4 import BeautifulSoup

url = "https://www.amazon.co.jp/s?k=%E3%83%8E%E3%83%BC%E3%83%88%E3%83%91%E3%82%BD%E3%82%B3%E3%83%B3&page=2&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=2R1N6RW104WL3&qid=1647246955&sprefix=%E3%83%8E%E3%83%BC%E3%83%88%E3%83%91%E3%82%BD%E3%82%B3%E3%83%B3%2Caps%2C221&ref=sr_pg_2"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("span", attrs={"class":"a-size-base-plus a-color-base a-text-normal"})
print(items[0].get_text())
print("")
print(items[1].get_text())
print("")
print(items[2].get_text())
print("")
print(items[3].get_text())
print("")
print(items[4].get_text())
"""出力
Lenovo ノートパソコン Yoga 650(マルチタッチ対応13.3型FHD/Ryzen 5/8GBメモリ/256GB/360°回転ディスプレイ/デジタルタッチペン付属)【Windows 11 無料アップグレード対応】

HP ノートパソコン 13.3インチ IPSディスプレイ 軽量957g AMD Ryzen5 16GB 512GB SSD HP Pavilion Aero 13-be ピンクベージュ Windows 11 Home WPS Office付き（型番：483X0PA-AAAC）

Lenovo ノートパソコン IdeaPad Slim 350i(14.0型FHD Core i7 8GBメモリ 512GB Microsoft Office搭載)【Windows 11 無料アップグレード対応】

Lenovo ノートパソコン IdeaPad Flex 550i(14.0型FHD Core i3 8GBメモリ 256GB )【Windows 11 無料アップグレード対応】 グレー

ASUSTek ゲーミングノートパソコン TUF Gaming F15 FX506HM(15.6インチ/Core i7-11800H/16GB, 512GB/RTX 3060 Laptop GPU/1,920×1,080(144Hz)/Webカメラ内蔵/ブラック)【日本正規代理店品】【あんしん保証】FX506HM-I7R3060BEC【Windows 11 無料アップグレード対応
】
"""

