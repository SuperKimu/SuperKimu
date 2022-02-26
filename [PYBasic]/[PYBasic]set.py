#set
#重複されず、順序がない
hello = {1,2,3,3,3,4,4,5,5,5,5}
print(hello) #{1, 2, 3, 4, 5}

java = {"mimi","nana","momo"}
python = {"mimi","papa","hoho"}
print(java & python) #javaとpython　両方ともできる人(積集合), mimi
print(java.intersection(python)) #javaとpython 両方ともできる人(積集合), mimi

#javaかpythonができる人，和集合
print(java | python) #{'papa', 'hoho', 'momo', 'nana', 'mimi'}
print(java.union(python)) #{'papa', 'hoho', 'momo', 'nana', 'mimi'}

#javaはできるけど、pythonができない人、差集合
print(java - python) #{'momo', 'nana'}
print(java.difference(python)) #{'momo', 'nana'}

#pythonできる人が増えたら？
python.add("pipi")
print(python) #{'papa', 'hoho', 'mimi', 'pipi'}

#javaを忘れた！削除するには
java.remove("mimi")
print(java) #{'nana', 'momo'}


menu = {"coffe", "milk", "juice"}
print(menu, type(menu)) #{'milk', 'coffe', 'juice'} <class 'set'>

menu = list(menu)
print(menu, type(menu)) #['milk', 'coffe', 'juice'] <class 'list'> タイプをリストへ変更

menu = tuple(menu)
print(menu, type(menu)) #('coffe', 'milk', 'juice') <class 'tuple'> タイプをtupleへ変更

menu = set(menu)
print(menu, type(menu)) #('coffe', 'milk', 'juice') <class 'tuple'> タイプをsetへ変更

from random import *
member = range(1,21) #1~20の数字を入れる
print(type(member)) 
member = list(member) #range タイプを　リストへ変更
shuffle(member) #1~20までの数字を混ぜ並べる
print(member)

winners = sample(member,4) #member変数から、4つの値を抽出
print(winners)

print("♥♥♥♥♥♥当選者発表♥♥♥♥♥♥")
print("お茶当選者:{0}".format(winners[0]))
print("お菓子当選者:{0}".format(winners[1:]))
print("♥♥♥♥♥♥おめでとうございます♥♥♥♥♥♥")

"""
出力
♥♥♥♥♥♥当選者発表♥♥♥♥♥♥
お茶当選者:3
お菓子当選者:[2, 15, 5]
♥♥♥♥♥♥おめでとうございます♥♥♥♥♥♥
"""
