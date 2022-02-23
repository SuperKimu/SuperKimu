#github 初期設定方法
"""
1. https://git-scm.com/ で git bash インストール
2. git bash 実行
3. git config --global user.name "github 登録 名前 "
4. git config --global user.email "github 登録 e-mail"
5. git config --list
⇒e-mailと名前ちゃんと認識されてるか確認
"""

#継続アップデート方法
"""
git add .
git commit -m "   h i s t o r y n a m e "
git push origin master

"""

print("have a nice day!")

#遠隔レポジトリ関連
"""
git remote -v 
⇒現在紐づけされてる遠隔レポジトリ確認

git remote remove origin
⇒当該遠隔レポジトリとの紐づけを除去（削除）

git remote add origin " https://github ~~~~~ "
※git config --global user.email & --global user.name も要るかも？

"""

#branch関連
"""
git branch 
or git branch --list
⇒現在のbranch

git branch -D "branch name"
⇒当該branchの削除


"""