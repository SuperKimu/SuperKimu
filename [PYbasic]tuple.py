# tuple
# tupleはリストと違って、内容変更と追加はできない。しかし、速度がリストより速い。

menu = ("うどん","そば")
print(menu[0]) #うどん
print(menu[1]) #そば
# menu.add("ラーメン")　はできない。

name = "bbobbi"
age = 30
hobby = "eat"
print(name, age, hobby) #bobbi 30 eat

name1, age1, hobby1 = "bbobbi1", 31, "eat"
print(name1,age1,hobby1) #bobbi1 31 eat
