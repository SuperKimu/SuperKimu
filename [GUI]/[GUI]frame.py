from tkinter import * 
root = Tk()
root.geometry("640x480")

Label(root, text="メニューを選んでください").pack(side="top")
Button(root, text="注文する").pack(side="bottom")



frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True) #side =　位置設定、　fill = both 、上下画面も囲む、　
#expand=True 画面左右も囲む


Button(frame_burger,text="ハンバーガー").pack()
Button(frame_burger,text="チキン").pack()
Button(frame_burger,text="ピザ").pack()

frame_drink = LabelFrame(root, text="飲料")
frame_drink.pack(side="right", fill="both",expand=True)
Button(frame_drink, text="コーラー").pack()
Button(frame_drink, text="オレンジ").pack()


root.mainloop()
