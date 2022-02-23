from tkinter import * 
root = Tk()

chkvar = IntVar() #　chkvarにint型で値を保存する
chkbox =Checkbutton(root, text="今日はみません", variable=chkvar)
# chkbox.select() #自動選択
# chkbox.deselect() #自動選択解除
chkbox.pack()


chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text = "一週間みません", variable=chkvar2)
chkbox2.pack()

def btncmd():
          print(chkvar.get()) # 0 :　チェック解除、1 : チェック
          print(chkvar2.get()) 
btn = Button(root, text = "クリック", command = btncmd)
btn.pack()


root.mainloop()
