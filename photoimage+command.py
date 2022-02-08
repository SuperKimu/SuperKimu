from tkinter import * 

root = Tk()
root.title("hello")

photo = PhotoImage(file="e:/practice/heart.png") #jpgファイルは認識できない？、pngはできた
btn = Button(root, image=photo)
btn.pack()

def btncmd(): 
          print("ボタンがクリックされました。")

btn1 = Button(root, text="動くボタン", command=btncmd) #btncmd 関数を　実行する
btn1.pack()

root.mainloop()

