#re = 正規式？
#羅列されたものをみて、それが規格に当てはまるか正しいか、確認すること→とても難しい

#例
"""
誕生日
851212(●)
8x1212(x)

E-mail
abc@abc.com(●)
abc@abc@abc.com(x)

IPアドレス
192.168.0.1(●)
1000.2000.3000.1000(x)
"""

#正規式ライブラリ　re
import re


p = re.compile("ca.e") #どんな正規式を使うか、()に入れる。.は一つの文字を意味
#(ca?e) 
#cafe, care, cave, case .... など
# ^ : 文字列の始まり
#(^de) : desk, destination ..など
# $ ：文字列の終わり
#(se$) : case, base... など

# m = p.match("case") # caseが、上の定義した、正規式にマッチングしているのか?
# print(m.group())
# #マッチングできないと、エラー発生

# if m:
#           print(m.group())
# else:
#           print("マッチングしてません")

def print_match(m):
          if m:
                    print("m.group()", m.group())
          else:
                    print("マッチングしてません")

# m = p.match("care")
# print_match(m)
#出力　：　care

# m = p.match("cccc")
# print_match(m)
#出力：　エラー

# m = p.match("careless")
# print_match(m)
# #出力 : care 、　後ろになにがあっても関係なし、最初から4文字、ca.eでマッチング判断

m = p.search("good care")
print_match(m)