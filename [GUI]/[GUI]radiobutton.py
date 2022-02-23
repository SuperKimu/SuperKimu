from tkinter import * 
root = Tk()

lable1 = Label(root, text = "メニューを選んでください").pack()

burger_var = IntVar() #ここにint型で値を保存

#Radiobutton = いくつかのボタンの中で、一つだけ選べる
btn_burger1 = Radiobutton(root, text="ハンバーガー", value=1, variable=burger_var)
btn_burger2 = Radiobutton(root, text="チーズバーガー", value=2, variable=burger_var)
btn_burger2.select() #burger2を基本設定された状態でプログラム実行
btn_burger3 = Radiobutton(root, text="チキンバーガー", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

lable1 = Label(root, text = "飲料を選んでください").pack()

drink_var = StringVar() #文字列で値の保存の為
btn_drink1 = Radiobutton(root, text="コーラー", value="コーラー", variable=drink_var)
btn_drink2 = Radiobutton(root, text="ウーロン茶", value="ウーロン茶", variable=drink_var)
btn_drink2.select()
btn_drink3 = Radiobutton(root, text="お水", value="お水", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd():
          print(burger_var.get()) #選択されたradiobuttonの値を出力
          print(drink_var.get())
btn = Button(root, text = "注文", command = btncmd)
btn.pack()


root.mainloop()
