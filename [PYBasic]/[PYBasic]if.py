#if
weather = "晴れ"
if weather == "雨": #もし、weatherが雨だったら、
   print("傘をお持ちください")
elif weather == "黄砂": #ifでなく、黄砂だったら、
  print("マスクをお持ちください")
else: #ifでも、elifでもなかったら、
   print("何も要りません")

weather = input("今日の天気はいかがですか？") #使用者入力欄を設ける
if weather == "雨": #もし、weatherが雨だったら、
   print("傘をお持ちください")
elif weather == "黄砂": #ifでなく、黄砂だったら、
  print("マスクをお持ちください")
else: #ifでも、elifでもなかったら、
   print("何も要りません")

weather = input("今日の天気はいかがですか？") #使用者入力欄を設ける
if weather == "雨" or weather == "雪": #もし、weatherが雨か雪だったら
   print("傘をお持ちください。")
elif weather == "黄砂": #ifでなく、黄砂だったら、
  print("マスクをお持ちください。")
else: #ifでも、elifでもなかったら、
   print("何も要りません。")

temp = int(input("気温はいかがですか？")) #使用者入力欄の数字を整数に変換するとき、intを使う
if 30 <= temp: 
           print("とても暑いです。")
elif 10 <= temp and temp < 30 :
          print("ちょうどいいです。")
elif 0 <= temp < 10 :
          print("上着を準備してください。")
else:
          print("外出は控えてください。")