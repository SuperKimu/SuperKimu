#BMI = 肥満度
#体重kg / 身長×身長

#適正体重
#身長×身長 ×　22

name = input("お名前はなんですか？")
weight = int(input("{}様の体重は何KGですか？".format(name)))
print("{0}KGですね。畏まりました。".format(weight))
height = int(input("それでは、{}様の身長は何CMですか？".format(name)))
print("{0}CMですね。畏まりました。".format(height))

loading = """

現在、BMIを計算してます・・・


少々お待ちください。

"""
print(loading)
bmi = round((weight / (height * height)) *10000)
if 19 > bmi:
          print("あなたのBMIは{0}です。痩せてますね!".format(bmi))
elif 19 <= bmi < 25:
          print("あなたのBMIは{0}です。標準です!".format(bmi))
elif 25 <= bmi < 30:
          print("あなたのBMIは{}です。やや太っており、少し運動しましょう".format(bmi))
elif 30 <= bmi < 40:
          print("あなたのBMIは{}です。ダイエットしましょう!".format(bmi))

from tkinter import *
win = tkinter.Tk();
win.mainloop();