print(abs(-10)) #10，絶対値
print(pow(5,3)) #5^3,125
print(max(3,18)) #18,最大値
print(min(3,18)) #3,最小値
print(round(3.12345)) #3,四捨五入　
print(round(3.51)) #4

from math import * #math　ライブラリの　全てを　利用する
print(floor(5.88)) #5、切り捨て
print(ceil(4.12345)) #5、切り上げ
print(sqrt(25)) #5,ルート


from random import *
print(random()) #0.0～1.0未満　任意の値を生産
print(random()*10) 
print(int(random()*10)) #小数点以下切り捨てて任意の値を生産
print(int ( random() * 10) + 1 )
print(int(random()*50)+1) #1~50以下任意の値を作る
print(randrange(1,51)) #1~51未満任意の値を作る
print(randint(1,50)) #1~50以下任意の値を作る

date = randint(4,28)
print("オフラインスタディーの日付は" + str(date) + "日になりました。")

