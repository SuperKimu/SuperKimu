python = "Python is Beautiful"

index = python.index("t") 
print(index) #2、python関数で、tは何番目に位置しているのか？
index = python.index("t", index + 1) 
print(index) #14、次のTは何番目に位置しているのか？

print(python.find("t")) #2、python関数で、tは何番目に位置しているのか？
print(python.find("q")) #-1、求めている値がなかったら、-1表示
# print(python.index("q")) #エラー、求めている値がなかったら、エラー表示
#プログラムが終了になり、次のコードからは実行しない
print("hello")

print(python.count("t")) #2、tの値がいくつあるのか