from tkinter import * 

root = Tk()

listbox = Listbox(root, selectmode="extended", height=0) #selectmode 選択モード、extendedは
#複数選択可能、一つだけ選択なら、single、height0はリスト全部を見せる、3だったら、3番目まで見せる
listbox.insert(0, "りんご") #0番目
listbox.insert(1, "いちご") #1番目
listbox.insert(2, "バナナ") #2番目
listbox.insert(END, "パインアップル") #一番後ろ
listbox.insert(END, "キウイ") #一番後ろ
listbox.pack()

def btncmd():
          # listbox.delete(END) #リストの一番後ろを削除、0は0番目削除
          # print("リストには", listbox.size(), "個あります。")   #リストの項目個数
          # print("1番から3番目までの項目：", listbox.get(0, 2)) 
          print("選択された項目：",listbox.curselection()) 

btn = Button(root, text="クリック", command=btncmd)
btn.pack()

root.mainloop()