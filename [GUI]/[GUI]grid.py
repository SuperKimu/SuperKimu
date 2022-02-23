#grid 格子

from tkinter import * 
root = Tk()
root.geometry("800x600")

# btn1 = Button(root, text="btn1")
# btn2 = Button(root, text="btn2")
# # btn1.pack(side="left")
# # btn2.pack(side="left")
# btn1.pack()
# btn2.pack()
###gridを使い、格子を作るときは、packは不要

# btn1.grid(row=0, column=0)
# btn2.grid(row=1, column=1)

###grid rowとcolumnで、位置を設定

btn1 = Button(root, text="btn1", padx=10, pady=10)
btn2 = Button(root, text="btn2")
btn3 = Button(root, text="btn3")
btn4 = Button(root, text="btn4")
#padx, pady ＝　ウィジェットのの左右と上下を広げる。文字の大きさはそのまま
#width, height= で大きさを固定することもできる

btn1.grid(row=0, column=0, sticky=N+E+W+S)
btn2.grid(row=0, column=1, sticky=N+E+W+S)
btn3.grid(row=0, column=2, sticky=N+E+W+S)
btn4.grid(row=0, column=3, sticky=N+E+W+S)

btn5 = Button(root, text="btn5", padx=10, pady=10)
btn6 = Button(root, text="btn6")
btn7 = Button(root, text="btn7")
btn8 = Button(root, text="btn8")

btn5.grid(row=1, column=0, sticky=N+E+W+S)
btn6.grid(row=1, column=1, sticky=N+E+W+S)
btn7.grid(row=1, column=2, sticky=N+E+W+S)
btn8.grid(row=1, column=3, sticky=N+E+W+S)

btn9 = Button(root, text="btn9")
btn10 = Button(root, text="btn10")
btn11 = Button(root, text="btn11")
# btn12 = Button(root, text="btn12")

btn9.grid(row=2, column=0, sticky=N+E+W+S)
btn10.grid(row=2, column=1, sticky=N+E+W+S)
btn11.grid(row=2, column=2, sticky=N+E+W+S)
# btn12.grid(row=2, column=3)

btn13 = Button(root, text="btn13")
btn14 = Button(root, text="btn14")
btn15 = Button(root, text="btn15")
btn16 = Button(root, text="btn16")

btn13.grid(row=3, column=0, sticky=N+E+W+S)
btn14.grid(row=3, column=1, sticky=N+E+W+S)
btn15.grid(row=3, column=2, sticky=N+E+W+S)
btn16.grid(row=2, column=3, rowspan=2, sticky=N+E+W+S)
#rowspan : ウィジェットのcolumn軸を広げる

btn17 = Button(root, text="btn17")
# btn18 = Button(root, text="btn18")
btn19 = Button(root, text="btn19")
btn20 = Button(root, text="btn20")

btn17.grid(row=4, column=0, columnspan=2, sticky=N+E+W+S)
#columnspan : ウィジェットのrow軸を広げる
# btn18.grid(row=4, column=1, sticky=N+E+W+S)
btn19.grid(row=4, column=2, sticky=N+E+W+S)
btn20.grid(row=4, column=3, sticky=N+E+W+S)
#sticky=N+E+W+S ウィジェットを東西南北で広げるとこもあで広げる



root.mainloop()
