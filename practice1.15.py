# python = "Python is Beautiful"
# print(python) #文字列が定義された通りに出力される
# print(python.lower()) #全て小文字にして出力　
# print(python.upper()) #全て大文字にして出力
# print(python[0].isupper()) #0番目のアルファベットは大文字か？
# print(python[1].islower()) #1番目のアルファベットは小文字か？
# print(len(python)) #文字列の全ての長さを数字で表示
# print(python.replace("Python","Java")) #　変数　～を～へ変更する

# index = python.index("t") 
# print(index) #2、python関数で、tは何番目に位置しているのか？
# index = python.index("t", index + 1) 
# print(index) #14、次のTは何番目に位置しているのか？

# print(python.find("t")) #2、python関数で、tは何番目に位置しているのか？
# print(python.find("q")) #-1、求めている値がなかったら、-1表示
# # print(python.index("q")) #エラー、求めている値がなかったら、エラー表示
# #プログラムが終了になり、次のコードからは実行しない
# print("hello")

# print(python.count("t")) #2、tの値がいくつあるのか




# name = "ミミ"
# age = 4
# hobby = "昼寝"
# is_adult = age >= 3

# print(" 我が家の" + animal + "の名前は" + name + "です")
# print( name + "は" + str(age) + "歳で" + hobby + "が好きです" )
# print( name,"は",age,"歳で",hobby,"が好きです")
# print( animal + "は大人ですか？" + str(is_adult))
# print( animal,"は大人ですか？",is_adult)
# animal = "犬"
# name = "モモ"
# print("我が家の" + animal + "の名前は" + name + "です")

# print(2+2) #4
# print(5-2) #3
# print(6*2) #12
# print(8/4) #2
# print(2**5) #32
# print(11%3) #2、余り
# print(11//3) #3、商(しょう)
# print(20 > 5) #true
# print(5 >=6) #false
# print(5< 20) #true
# print(5 <= 6) #true 
# print(5 == 5) #true、前と後ろの値は同じか？
# print(6 == 3) #false
# print(3+2+3 == 8) #true

# print(3 + 4 * 5) #23
# print((3+4)*5) #35
# number =  3 + 4 * 5 #23
# print(number) #23
# number = number + 5 #28
# print(number) #28
# number += 5 
# print(number) #33
# number -= 4 
# print(number) #29
# number *= 2
# print(number) #58
# number %= 3
# print(number) #1
# number /= 3
# print(number) # 0.3333333333333
# number = number + 1
# print(number) # 1.33333333333333


# print(abs(-10)) #10，絶対値
# print(pow(5,3)) #5^3,125
# print(max(3,18)) #18,最大値
# print(min(3,18)) #3,最小値
# print(round(3.12345)) #3,四捨五入　
# print(round(3.51)) #4

# from math import * #math　ライブラリの　全てを　利用する
# print(floor(5.88)) #5、切り捨て
# print(ceil(4.12345)) #5、切り上げ
# print(sqrt(25)) #5,ルート

# from os import nice
# from random import *
# from tkinter import N
# print(random()) #0.0～1.0未満　任意の値を生産
# print(random()*10) 
# print(int(random()*10)) #小数点以下切り捨てて任意の値を生産
# print(int ( random() * 10) + 1 )
# print(int(random()*50)+1) #1~50以下任意の値を作る
# print(randrange(1,51)) #1~51未満任意の値を作る
# print(randint(1,50)) #1~50以下任意の値を作る

# date = randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월" + str(date) + "일로 선정되었습니다.")

# sentence = "私は男です"
# print(sentence)
# sentence2 = "pythonは楽しいです"
# print(sentence2)
# sentence3 = """ 

# 私は男です

# pythonは楽しいです

# """
# print(sentence3) # """~""" 文字列だけでなく、行間も適用される


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


#リスト
# number = [10, 20, 30]
# print(number) #[10, 20, 30]

# # fruit = ["apple", "melon", "strawberry"]
# # print(fruit.index("strawberry")) #strawberryは、何番目に位置しているのか？2番目(0からカウンター)
# # fruit.append("grape") #fruit変数最後に"grape"を追加する
# # fruit.insert(1,"banana") #1番目に"banana"を入れる
# # print(fruit.pop()) #一番後ろの値を1個削除、grapeを削除
# # print(fruit) #['apple', 'banana', 'melon', 'strawberry']

# # print(fruit.pop()) #strawberry 削除
# # print(fruit) #['apple', 'banana', 'melon']

# # print(fruit.pop()) #melon削除
# # print(fruit) #['apple', 'banana']

# # fruit.append("banana")
# # print(fruit)
# # print(fruit.count("banana")) # banana 値はいくつあるか？

# # number = [6, 7, 2, 3, 1, 0, 4, 5]
# # number.sort() #小さい順で並べ替える, #[0, 1, 2, 3, 4, 5, 6, 7]
# # print(number)

# # number1 = [1, 3, 2, 4, 5, 7, 6, 8]
# # number1.reverse() #逆順で並べ替える
# # print(number1) # [8, 6, 7, 5, 4, 2, 3, 1]

# # number.clear() #全ての値をクリア
# # print(number) #[]

# # #色んな値と一緒に使える
# # number3 = [20, "banana", False]
# # print(number3) #[20, 'banana', False]

# # number4 = [1, 2, 3, 4, 5]
# # number5 = ["apple", "banana"]

# # number4.extend(number5)
# # print(number4) #[1, 2, 3, 4, 5, 'apple', 'banana']

# friend = {1:"baby", 2:"puppy",3:"angel"} #キー１，２，３に対して、value baby, puppy, angelを定義する
# print(friend[1]) #キー１は？baby
# print(friend.get(2)) #キー２は？puppy

# print(1 in friend) #キー1がfriendに入ってるか？True
# print(5 in friend) #キー5がfriendに入ってるか？False

# friend1 = {"1-a" : "hi", "2-a" : "hello"}
# print(friend1["1-a"]) #hi
# print(friend1["2-a"]) #hello

# friend1["1-a"] = "thanks" #friend1変数、キー1-aのvalueを　thanksへ変える
# friend1["3-a"] = "nice" #friend1変数に、キー3-1、value　niceを追加
# del friend1["3-a"] #friend1変数キー3-aを削除

# print(friend.keys()) #friendのキーのみ出力、dict_keys([1, 2, 3])
# print(friend1.values()) #friendのvalueのみ出力、dict_values(['thanks', 'hello'])

# print(friend.items()) #friendのキーとvalueを両方とも出力、dict_items([(1, 'baby'), (2, 'puppy'), (3, 'angel')])

# friend.clear() #friendをクリアする
# print(friend) #{}

# print(friend.get(4))
# print("hello") #friend変数キー4に何もなかった為、Noneと表示されるが、プログラムは終了されず、helloも表示される

# print(friend.get(5, "空き")) #キー5は何もなかった為、Noneではなく「空き」と表示させる
# print(friend[4])

# print("hello") #friend変数キー4に何もなかった為、エラーになり、プログラム終了、helloは表示されない。

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