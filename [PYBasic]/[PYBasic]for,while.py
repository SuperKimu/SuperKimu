#for
print("待ち順番 : 0 ")
print("待ち順番 : 1 ")
print("待ち順番 : 2 ")
print("待ち順番 : 3 ")
print("待ち順番 : 4 ")
print("待ち順番 : 5 ")

for waiting_number in [0,1, 2, 3, 4, 5]: 
 print("待ち順番 : {0}".format(waiting_number))

for waiting_number in range(5):
    print("待ち順番 : {0}".format(waiting_number)) 

for waiting_number in range(1, 6):
    print("待ち順番 : {0}".format(waiting_number)) 


"""
上の4つは、全て同じ結果が出力される

待ち順番 : 0 
待ち順番 : 1 
待ち順番 : 2
待ち順番 : 3
待ち順番 : 4
待ち順番 : 5

"""

for guest in ["mimi", "momo", "meme", "mumu", "myamya", "myomyo"]: 
 print("{0}様 こんにちは".format(guest))

"""
出力
mimi様 こんにちは
momo様 こんにちは
meme様 こんにちは
mumu様 こんにちは
myamya様 こんにちは
myomyo様 こんにちは

"""

cafe = ["mama", "papa","koko"]
for guest in cafe:
          print("{0}様、コーヒーが用意できました。".format(guest))


#while
customer = "mimi"
index = 5
while index >= 1:
           print("{0}", )