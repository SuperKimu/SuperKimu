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
