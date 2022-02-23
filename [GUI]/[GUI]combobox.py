import tkinter.ttk as ttk #combobox関数を使うには、こちらも必要

from tkinter import * 
root = Tk()

values = [str(i) + "日" for i in range(1,32)] #  str：数字の値の為、for i in range (1,32) : 1~31の数字
combobox = ttk.Combobox(root, height=5, values=values) 
combobox.set("今日は何日ですか？") #最初、設定された文字列
combobox.pack()

combobox2 = ttk.Combobox(root, height=10, values=values, state="readonly")  #state = readonly、入力できなくする
combobox2.set("今日は何日ですか？") #最初、設定された文字列
combobox2.pack()

def btncmd():
          print(combobox.get()) #選択された値を出力
          print(combobox2.get())
btn = Button(root, text = "クリック", command = btncmd)
btn.pack()


root.mainloop()
