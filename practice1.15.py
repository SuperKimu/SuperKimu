













# me = "121212-1234567"
# #順番数えるとき、1ではなくて0を起算点に

# print(me[5]) #2、左から5番目の値を表示
# print(me[0:5]) #12121、左から0～4番目まで値を表示
# print(me[1:3]) #21、左から1～2番目までの値を表示
# print(me[0:6]) #121212、左から0～5番目まで値を表示
# print(me[:6]) #121212、0は省ける
# print(me[7:14]) #1234567、左から7～13番目まで値を表示
# print(me[7:]) #1234567、0は省ける
# print(me[-7:]) #1234567、-符号を使い、右からでも表示可能


# print("a" + "b") #ab
# print("a", "b") #a b

# print("私たちは%d歳です。" %30) #dは整数
# print("%sは30歳です。" %"私たち") #sは文字列、""で囲む
# print("私は%s歳です。" %30)
# print("%cは30歳です。"%"私") #cは文字、""で囲むのは、sと一緒だが、一文字しかできない
# print("私は%s色と%s色が好きです。" %("赤","白"))

# print("私は{}歳です。".format(30)) #{}にformatの値を入れる

# print("私は{}色と{}色が好きです。".format("赤","白"))
# print("私は{0}色と{1}色が好きです。".format("赤","白"))
# print("私は{1}色と{0}色が好きです。".format("赤","白"))

# print("私は{age}歳で、{color}色が好きです。".format(age = 30 , color = "赤"))

# age=30
# color="赤"
# print(f"私は{age}歳で、{color}色が好きです。")

#\n : 行間を変える
# print("おはようございます\nこんにちは\nこんばんは")
# print('私は"男"です')

# #\ : ""か''をそのまま表示
# print("私は\"男\"です")
# print("私は\'男\'です")

# #\\ : 文字列の中で\を表示するとき使う
# #E:\practice が　出力したい場合
# print("E:\\practice")

# # \r : マウスカーソルを一番前へ移動する（文字列が上書きされながら書き換える）
# print("black sky\rgreen")
# print("red sky\rpink")

# # \b : バックスペース、\b前の一文字削除
# print("blacks\bsky")

# # \t : Tab、キーボードのTabと同じ効果
# print("blue\tsky")

# site = "http://youtube.com"
# site = "http://yahoo.com"
# url = site.replace("http://","")
# #siteの変数に入ってる文字列で、"http://"を""へ変換（空白にする）
# url = url[:url.index(".")] 
# #url変数の中の文字列で、最初から、"."の直前まで、スライスする
# password = url[:3] + str(len(url)) + str(url.count("n")) + "!"
# print(password)
# print("{0}のパスワードは{1}です。".format(site, password))



#tuple
#tupleはリストと違って、内容変更と追加はできない。しかし、速度がリストより速い。

# menu = ("うどん","そば")
# print(menu[0]) #うどん
# print(menu[1]) #そば
# # menu.add("ラーメン")　はできない。

# name = "bbobbi"
# age = 30
# hobby = "eat"
# print(name, age, hobby) #bobbi 30 eat

# name1, age1, hobby1 = "bbobbi1", 31, "eat"
# print(name1,age1,hobby1) #bobbi1 31 eat


# #set
# #重複されず、順序がない
# hello = {1,2,3,3,3,4,4,5,5,5,5}
# print(hello) #{1, 2, 3, 4, 5}

# java = {"mimi","nana","momo"}
# python = {"mimi","papa","hoho"}
# print(java & python) #javaとpython　両方ともできる人(積集合), mimi
# print(java.intersection(python)) #javaとpython 両方ともできる人(積集合), mimi

# #javaかpythonができる人，和集合
# print(java | python) #{'papa', 'hoho', 'momo', 'nana', 'mimi'}
# print(java.union(python)) #{'papa', 'hoho', 'momo', 'nana', 'mimi'}

# #javaはできるけど、pythonができない人、差集合
# print(java - python) #{'momo', 'nana'}
# print(java.difference(python)) #{'momo', 'nana'}

# #pythonできる人が増えたら？
# python.add("pipi")
# print(python) #{'papa', 'hoho', 'mimi', 'pipi'}

# #javaを忘れた！削除するには
# java.remove("mimi")
# print(java) #{'nana', 'momo'}


# menu = {"coffe", "milk", "juice"}
# print(menu, type(menu)) #{'milk', 'coffe', 'juice'} <class 'set'>

# menu = list(menu)
# print(menu, type(menu)) #['milk', 'coffe', 'juice'] <class 'list'> タイプをリストへ変更

# menu = tuple(menu)
# print(menu, type(menu)) #('coffe', 'milk', 'juice') <class 'tuple'> タイプをtupleへ変更

# menu = set(menu)
# print(menu, type(menu)) #('coffe', 'milk', 'juice') <class 'tuple'> タイプをsetへ変更

# from random import *
# member = range(1,21) #1~20の数字を入れる
# print(type(member)) 
# member = list(member) #range タイプを　リストへ変更
# shuffle(member) #1~20までの数字を混ぜ並べる
# print(member)

# winners = sample(member,4) #member変数から、4つの値を抽出
# print(winners)

# print("♥♥♥♥♥♥当選者発表♥♥♥♥♥♥")
# print("お茶当選者:{0}".format(winners[0]))
# print("お菓子当選者:{0}".format(winners[1:]))
# print("♥♥♥♥♥♥おめでとうございます♥♥♥♥♥♥")

# 出力
# ♥♥♥♥♥♥当選者発表♥♥♥♥♥♥
# お茶当選者:3
# お菓子当選者:[2, 15, 5]
# ♥♥♥♥♥♥おめでとうございます♥♥♥♥♥♥

#if
# weather = "晴れ"
# if weather == "雨": #もし、weatherが雨だったら、
#    print("傘をお持ちください")
# elif weather == "黄砂": #ifでなく、黄砂だったら、
#   print("マスクをお持ちください")
# else: #ifでも、elifでもなかったら、
#    print("何も要りません")

# weather = input("今日の天気はいかがですか？") #使用者入力欄を設ける
# if weather == "雨": #もし、weatherが雨だったら、
#    print("傘をお持ちください")
# elif weather == "黄砂": #ifでなく、黄砂だったら、
#   print("マスクをお持ちください")
# else: #ifでも、elifでもなかったら、
#    print("何も要りません")

# weather = input("今日の天気はいかがですか？") #使用者入力欄を設ける
# if weather == "雨" or weather == "雪": #もし、weatherが雨か雪だったら
#    print("傘をお持ちください。")
# elif weather == "黄砂": #ifでなく、黄砂だったら、
#   print("マスクをお持ちください。")
# else: #ifでも、elifでもなかったら、
#    print("何も要りません。")

# temp = int(input("気温はいかがですか？")) #使用者入力欄の数字を整数に変換するとき、intを使う
# if 30 <= temp: 
#            print("とても暑いです。")
# elif 10 <= temp and temp < 30 :
#           print("ちょうどいいです。")
# elif 0 <= temp < 10 :
#           print("上着を準備してください。")
# else:
#           print("外出は控えてください。")

# #for
# print("待ち順番 : 0 ")
# print("待ち順番 : 1 ")
# print("待ち順番 : 2 ")
# print("待ち順番 : 3 ")
# print("待ち順番 : 4 ")
# print("待ち順番 : 5 ")

# for waiting_number in [0,1, 2, 3, 4, 5]: 
#  print("待ち順番 : {0}".format(waiting_number))

# for waiting_number in range(5):
#     print("待ち順番 : {0}".format(waiting_number)) 

# for waiting_number in range(1, 6):
#     print("待ち順番 : {0}".format(waiting_number)) 


# """
# 上の4つは、全て同じ結果が出力される

# 待ち順番 : 0 
# 待ち順番 : 1 
# 待ち順番 : 2
# 待ち順番 : 3
# 待ち順番 : 4
# 待ち順番 : 5

# """

# for guest in ["mimi", "momo", "meme", "mumu", "myamya", "myomyo"]: 
#  print("{0}様 こんにちは".format(guest))

# """
# 出力
# mimi様 こんにちは
# momo様 こんにちは
# meme様 こんにちは
# mumu様 こんにちは
# myamya様 こんにちは
# myomyo様 こんにちは

# """

# cafe = ["mama", "papa","koko"]
# for guest in cafe:
#           print("{0}様、コーヒーが用意できました。".format(guest))


#while
# customer = "mimi"
# index = 5
# while index >= 1:
#            print("{0}", )