import tkinter.messagebox as msg #tkinterのmessagebox関数を、msgで読み込む
from tkinter import * 
root = Tk()

def info(): #info : 案内　！
          msg.showinfo("お知らせ" , "問題ありません")

def warn(): #警告　！
          msg.showwarning("警告警告" , "警告ですよ")

def error(): #エラー　X　表示
          msg.showerror("エラー", "エラーですよ!")

def okcancel():
          msg.askokcancel("エラー","エラーですけど、取り消ししますか？")

def retrycancel():
          msg.askretrycancel("エラー","エラーですけど、再実行しますか？")

def yesno(): # ?で聞く
          msg.askyesno("yes or no ?", "yes ? no ? どっち？")

def yesnocancel(): # ?で聞く+取り消しもあり
          msg.askyesnocancel("yes or no ? + cancel ", "yes ? no ? どっち？ cancelもあり")


Button(root, command=info, text="お知らせ").pack()
Button(root, command=warn, text="警告警告").pack()
Button(root, command=error, text="エラー").pack()
Button(root, command=okcancel, text="エラー(質問型)").pack()
Button(root, command=retrycancel, text="エラー(再実行)").pack()
Button(root, command=yesno, text="yes no(選択)").pack()
Button(root, command=yesnocancel, text="yes no(選択) + 取り消し").pack()

root.mainloop()
