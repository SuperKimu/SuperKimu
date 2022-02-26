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
#cafe, care, cave, case .... など caffe (X)
# ^ : 文字列の始まり
#(^de) : desk, destination ..など fade (X)
# $ ：文字列の終わり
#(se$) : case, base... など face (X)


# m = p.match("case") # caseが、上の定義した、正規式にマッチングしているのか?
# print(m.group())
# #マッチングできないと、エラー発生

# if m:
#           print(m.group())
# else:
#           print("マッチングしてません")

def print_match(m): #p = re.compile("ca.e") / m = p.search("careless")で実行したとき
          if m:
                    print("m.group() :", m.group()) #出力：care　一致する文字列を返す
                    print("m.string:", m.string)    #出力:careless　入力された文字列を返す
                    print("m.start():", m.start())  #出力:0　一致する文字列のスタートINDEX　0番からあってる
                    print("m.end():", m.end())      #出力：4　一致する文字列の終わり　INDEX　4番前まであってる
                    print("m.span()",m.span())    #出力：　0,4　一致する文字列のスタート/終わりINDEX 0番から、4番前まで合ってる
          else:
                    print("マッチングしてません")

# m = p.match("care") #match : 与えられた文字列の最初から一致しているか確認
# print_match(m)
# 出力　：　care

# m = p.match("cccc")
# print_match(m)
#出力：　エラー

# m = p.match("careless")
# print_match(m)
# #出力 : care 、　後ろになにがあっても関係なし、最初から4文字、ca.eでマッチング判断

m = p.search("careless") #search : 与えられた文字列の中に一致しているのがあるか確認
print_match(m)


list = p.findall("good care cafe") #一致するすべてをリストにして返す 
print(list) #出力：cafe, cafe

list = p.findall("good care") #一致するすべてをリストにして返す 
print(list) #出力：cafe


"""
正規式を使うときは
1. re.compile("求める形態")
※普通は p = re.compile("求める形態")でよく使う
2. m = p.match("比較する文字列") :与えられた文字列が最初から一致するか確認
   m = p.search("比較する文字列") :与えられた文字列の中で、一致するものがあるか確認
   list = p.findall("比較する文字列") :

"""