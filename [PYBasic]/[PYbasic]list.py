#リスト
number = [10, 20, 30]
print(number) #[10, 20, 30]

fruit = ["apple", "melon", "strawberry"]
print(fruit.index("strawberry")) #strawberryは、何番目に位置しているのか？2番目(0からカウンター)
fruit.append("grape") #fruit変数最後に"grape"を追加する
fruit.insert(1,"banana") #1番目に"banana"を入れる
print(fruit.pop()) #一番後ろの値を1個削除、grapeを削除
print(fruit) #['apple', 'banana', 'melon', 'strawberry']

print(fruit.pop()) #strawberry 削除
print(fruit) #['apple', 'banana', 'melon']

print(fruit.pop()) #melon削除
print(fruit) #['apple', 'banana']

fruit.append("banana")
print(fruit)
print(fruit.count("banana")) # banana 値はいくつあるか？

number = [6, 7, 2, 3, 1, 0, 4, 5]
number.sort() #小さい順で並べ替える, #[0, 1, 2, 3, 4, 5, 6, 7]
print(number)

number1 = [1, 3, 2, 4, 5, 7, 6, 8]
number1.reverse() #逆順で並べ替える
print(number1) # [8, 6, 7, 5, 4, 2, 3, 1]

number.clear() #全ての値をクリア
print(number) #[]

#色んな値と一緒に使える
number3 = [20, "banana", False]
print(number3) #[20, 'banana', False]

number4 = [1, 2, 3, 4, 5]
number5 = ["apple", "banana"]

number4.extend(number5)
print(number4) #[1, 2, 3, 4, 5, 'apple', 'banana']

friend = {1:"baby", 2:"puppy",3:"angel"} #キー１，２，３に対して、value baby, puppy, angelを定義する
print(friend[1]) #キー１は？baby
print(friend.get(2)) #キー２は？puppy

print(1 in friend) #キー1がfriendに入ってるか？True
print(5 in friend) #キー5がfriendに入ってるか？False

friend1 = {"1-a" : "hi", "2-a" : "hello"}
print(friend1["1-a"]) #hi
print(friend1["2-a"]) #hello

friend1["1-a"] = "thanks" #friend1変数、キー1-aのvalueを　thanksへ変える
friend1["3-a"] = "nice" #friend1変数に、キー3-1、value　niceを追加
del friend1["3-a"] #friend1変数キー3-aを削除

print(friend.keys()) #friendのキーのみ出力、dict_keys([1, 2, 3])
print(friend1.values()) #friendのvalueのみ出力、dict_values(['thanks', 'hello'])

print(friend.items()) #friendのキーとvalueを両方とも出力、dict_items([(1, 'baby'), (2, 'puppy'), (3, 'angel')])

friend.clear() #friendをクリアする
print(friend) #{}

print(friend.get(4))
print("hello") #friend変数キー4に何もなかった為、Noneと表示されるが、プログラムは終了されず、helloも表示される

print(friend.get(5, "空き")) #キー5は何もなかった為、Noneではなく「空き」と表示させる

print("hello") #friend変数キー4に何もなかった為、エラーになり、プログラム終了、helloは表示されない。

me = "121212-1234567"
#順番数えるとき、1ではなくて0を起算点に

print(me[5]) #2、左から5番目の値を表示
print(me[0:5]) #12121、左から0～4番目まで値を表示
print(me[1:3]) #21、左から1～2番目までの値を表示
print(me[0:6]) #121212、左から0～5番目まで値を表示
print(me[:6]) #121212、0は省ける
print(me[7:14]) #1234567、左から7～13番目まで値を表示
print(me[7:]) #1234567、0は省ける
print(me[-7:]) #1234567、-符号を使い、右からでも表示可能


print("a" + "b") #ab
print("a", "b") #a b

print("私たちは%d歳です。" %30) #dは整数
print("%sは30歳です。" %"私たち") #sは文字列、""で囲む
print("私は%s歳です。" %30)
print("%cは30歳です。"%"私") #cは文字、""で囲むのは、sと一緒だが、一文字しかできない
print("私は%s色と%s色が好きです。" %("赤","白"))

print("私は{}歳です。".format(30)) #{}にformatの値を入れる

print("私は{}色と{}色が好きです。".format("赤","白"))
print("私は{0}色と{1}色が好きです。".format("赤","白"))
print("私は{1}色と{0}色が好きです。".format("赤","白"))

print("私は{age}歳で、{color}色が好きです。".format(age = 30 , color = "赤"))

age=30
color="赤"
print(f"私は{age}歳で、{color}色が好きです。")

#\n : 行間を変える
print("おはようございます\nこんにちは\nこんばんは")
print('私は"男"です')

#\ : ""か''をそのまま表示
print("私は\"男\"です")
print("私は\'男\'です")

#\\ : 文字列の中で\を表示するとき使う
#E:\practice が　出力したい場合
print("E:\\practice")

# \r : マウスカーソルを一番前へ移動する（文字列が上書きされながら書き換える）
print("black sky\rgreen")
print("red sky\rpink")

# \b : バックスペース、\b前の一文字削除
print("blacks\bsky")

# \t : Tab、キーボードのTabと同じ効果
print("blue\tsky")

site = "http://youtube.com"
site = "http://yahoo.com"
url = site.replace("http://","")
#siteの変数に入ってる文字列で、"http://"を""へ変換（空白にする）
url = url[:url.index(".")] 
#url変数の中の文字列で、最初から、"."の直前まで、スライスする
password = url[:3] + str(len(url)) + str(url.count("n")) + "!"
print(password)
print("{0}のパスワードは{1}です。".format(site, password))

