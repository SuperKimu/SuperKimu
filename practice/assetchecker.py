#現在のbitcoin、ethereum、rippleの資産合計を円にして、GUIで表す

#現在日付と時間
import datetime
now = datetime.datetime.today()
thistime = "本日は" + str(now.month) + "月" + str(now.day) + "日で、現在時刻は" + str(now.hour) + "時"  + str(now.minute) + "分です。"
print(thistime)

#2022.2.23　
bit = 0.02507351
xrp = 10
ethereum = 0.05506036
