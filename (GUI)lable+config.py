from tkinter import * 

root = Tk()
root.title("hello")

label1 = Label(root, text="hello皆様!") #hello皆様をlabelで表示
label1.pack()

photo = PhotoImage(file="heart.png") #file経路イメージが
label2 = Label(root, image=photo) #Labelで表示される
label2.pack() #label2実行

def change(): 
          label1.config(text="またお会いしましょう") #label1のtextを、またお会いしましょうへ変更

          global photo2 #全域関数宣言しないと、下のイメージが変わらない
          photo2 = PhotoImage(file="star.png")
          label2.config(image=photo2)
btn = Button(root, text = "クリック", command=change) 
btn.pack()

    
root.mainloop()
