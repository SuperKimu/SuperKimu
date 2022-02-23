from tkinter import * 
root = Tk()

def create_new_file():
          print("新しいファイルを作ります。")

menu = Menu(root)


menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator() #太い線で区切るとき、separator
menu_file.add_command(label="Save All", state="disable") #state="disable" 活性化させない
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit) #command=root.quit、終了


menu_file2 = Menu(menu, tearoff=0)
menu_file2.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)
menu.add_cascade(label="Edit", menu=menu_file2)

#radioボタンでメニューの追加

menu_file3 = Menu(menu, tearoff=0)
menu_file3.add_radiobutton(label="hello")
menu_file3.add_radiobutton(label="hi")
menu_file3.add_radiobutton(label="good")
menu.add_cascade(label="radiobutton", menu=menu_file3)

#checkbutton
menu_file4 = Menu(menu, tearoff=0)
menu_file4.add_checkbutton(label="checkbutton!")
menu.add_cascade(label="checkbutton", menu=menu_file4)

root.config(menu=menu)
root.mainloop()
