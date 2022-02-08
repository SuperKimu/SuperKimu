#関数
def open_account(): #open_account関数を作る
          print("ありがとうございます!")

open_account() #ここまで入れないと、関数で定義された値が出力されない。

def person():
          print("男女併せて{}名です。".format(man + girl))
man = 2
girl = 3
person()


def deposit(balance, money): #deposit 入金、balance　残高、money　入金
    print("入金完了しました。残高は{0}円です。".format(balance + money))
    return balance + money 

balance = 0
balance = deposit(balance, 1000)
print(balance) #入金完了しました。残高は1000円です。
balance = deposit(balance, 2000)
balance = deposit(balance, 2000)
balance = deposit(balance, 2000)
balance = deposit(balance, 2000)
balance = deposit(balance, 2000)
balance = deposit(balance, 2000)
balance = deposit(balance, 2000)
balance = deposit(balance, 2000)
balance = deposit(balance, 2000)

"""
入金完了しました。残高は1000円です。
1000
入金完了しました。残高は3000円です。
入金完了しました。残高は5000円です。
入金完了しました。残高は7000円です。
入金完了しました。残高は9000円です。
入金完了しました。残高は11000円です。
入金完了しました。残高は13000円です。
入金完了しました。残高は15000円です。
入金完了しました。残高は17000円です。
入金完了しました。残高は19000円です。
"""

def withdraw(balance, money): #withdraw、引き出し
 if balance >= money:
    print("引き出しが完了しました。残高は{}円です。".format(balance - money))
    return balance - money
 else:     
    print("残高が不足してます。残高は{}円です".format(balance))
    return balance

print(balance)
balance = withdraw(balance, 1000)
balance = withdraw(balance, 1000)
balance = withdraw(balance, 1000)
balance = withdraw(balance, 1000)
balance = withdraw(balance, 1000)
balance = withdraw(balance, 1000)
balance = withdraw(balance, 1000)
balance = withdraw(balance, 1000)
balance = withdraw(balance, 10000)
balance = withdraw(balance, 500)
balance = withdraw(balance, 600)

"""
19000
引き出しが完了しました。残高は18000円です。
引き出しが完了しました。残高は17000円です。
引き出しが完了しました。残高は16000円です。
引き出しが完了しました。残高は15000円です。
引き出しが完了しました。残高は14000円です。
引き出しが完了しました。残高は13000円です。
引き出しが完了しました。残高は12000円です。
引き出しが完了しました。残高は11000円です。
引き出しが完了しました。残高は1000円です。
引き出しが完了しました。残高は500円です。
残高が不足してます。残高は500円です
"""

