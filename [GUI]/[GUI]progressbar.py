import time
#progressbar
import tkinter.ttk as ttk #progressbarもこちらの関数必要
from tkinter import * 
root = Tk()

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") #いつ終わるかわからないので、indeterminate
# progressbar.start(10) #()に速度、1はめっちゃ早い スタートさせる
# progressbar.pack()

# progressbar2 = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar2.start(10)
# #modeにdeterminateも使える
# progressbar2.pack()

# def btncmd():
#           progressbar.stop() #停止させる
#           progressbar2.stop()
# btn = Button(root, text = "中止", command = btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
 for i in range (1, 101): # 1 ~ 100 を代入
          time.sleep(0.01) #0.01秒待機

          p_var2.set(i) #progress barの値を設定
          progressbar2.update() #UIのアップデート、視覚化
          print(p_var2.get())
          
btn = Button(root, text = "スタート", command = btncmd2)
btn.pack()

root.mainloop()
