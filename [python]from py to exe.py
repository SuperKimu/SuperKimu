#pythonのpy拡張子をexe実行ファイルへ変換する方法
#⇒pythonのpipを使い、pyinstallerライブラリを使う！


#手順
"""
1 pip install pyinstaller で pyinstaller インストール
2 pyinstaller "ファイル名前.py"
→ 変換したいファイル名頭の1,2文字だけ入力し、Tabキー押したら、その1,2文字から始まる
ファイルを自動的に見つけてくれる

#3 "dist"と"build"のフォルダ、そして、入力した"ファイル名.spec"のファイルが作られる
#4 "dist"フォルダクリック→マウス右→ Reveal in file explorer → フォルダ → 中にexeファイルがある
"""
#しかし、上のやり方だと、ファイルもフォルダもめっちゃくちゃ多い。純粋に一つのexeファイルが作りたかったら・・
#ターミナルモードです！
"""
1 pyinstaller -F "ファイル名前.py"
2 "dist"フォルダができる→ マウス右Reveal in file explorer → dist → ファイル名.exeファイルがある

"""


#windowsモードのpyファイルを、exeファイル1つにまとめる
"""
1 pyinstaller -w "ファイル名前.py"
2 "dist"フォルダができる→ マウス右Reveal in file explorer → dist → ファイル名.exeファイルがある
3 pyinstaller -w -F "ファイル名前.py" 
※ターミナルモードの、1つのexeにまとまったファイルを作る
"""

#ターミナルモードも、windowsモードも、小文字大文字区別注意！

print("pyinstaller TEST")