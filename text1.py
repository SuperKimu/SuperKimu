from tkinter import * 

root = Tk()
root.title("hello")

txt = Text(root, width=30, height=5) #入力できる、Textボックスを作る。
txt.pack()


txt.insert(END, "文字を入力してください。")# 文字を入力してください。と事前に表示されるTextボックスを作る。

e = Entry(root, width=30) #enterで行間が変えられない
e.pack() 
e.insert(0,"一行だけ入力してください。") #entryにも文字を入れる。

def btncmd():
    print(txt.get("1.0", END)) #１番目LINEと0番目のコロン位置からの全ての値を持ってくる）
    print(e.get()) #entryの値もそのまま持ってくる

    txt.delete("1.0", END) #１番目LINEと0番目のコロン位置からの全ての値を削除して、入力された値を持ってくる。
    e.delete(0,END) #事前に入ってる文字を削除、入力された値のみ持ってくる。

btn = Button(root, text="クリック", command=btncmd)
btn.pack()

root.mainloop()