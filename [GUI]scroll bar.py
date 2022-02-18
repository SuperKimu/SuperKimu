from tkinter import * 
root = Tk()

frame = Frame(root)
frame.pack()


#listboxとscrollbarをframeに入れる
scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y") #位置を,y軸に全て広げる

listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand= scrollbar.set)
#yscrollcommand =scrollbar.set →scroll bar を作る

for i in range(1, 32): # 1~31まで,listboxに入れる
          listbox.insert(END, str(i) + "日")
listbox.pack(side="left")#位置を左
scrollbar.config(command=listbox.yview)
#scrollbarの動きに併せて、listboxも動く
root.mainloop()
