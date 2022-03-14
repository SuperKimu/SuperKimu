#Extensions にて、open in browser を　インストール
"""
vscの中のHTML拡張子ファイルをそのままブラウザーで開けるようになる
open in browser インストールすると、vscの中のHTMLファイル→右クリック
→Open In Default Browser と Open In Other Browser の選択オプションができる
"""

#HTTP METHOD
"""
HTTPプロトコルを通じて、サーバーに要請すれば,サーバーはその要請に合わせて応えてくれる。
要請に含まれることの中に、「HTTP METHOD」がある。
HTTP METHODにはいくつかあるが、代表的なものが、GET方式、POST方式。
GET方式= ある内容を誰もが見れるように、URLに書いて送る方式
POST方式= URLではなく、「HTTPのメッセージBODY」に隠して送る方法

EX)GET方式
https://www.amazon.co.jp/s?k=%E3%83%8E%E3%83%BC%E3%83%88%E3%83%91%E3%82%BD%E3%82%B3%E3%83%B3&page=2&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=2K11G65WUX4P8&qid=1647210815&sprefix=%E3%81%AE%E3%83%BC%E3%81%A8%E3%81%B1%E3%81%9D%E3%81%93%E3%82%93%2Caps%2C223&ref=sr_pg_3
※各変数と値は「？」と「&」で区切る
⇒この値を変更しながら、ページ変更が安易に可能
⇒GET方式は送るとき、データのサイズに制限あり、大きなデータは遅れない。
⇒WEBページ変更のたびに、URLも変更
☆よってWEBSCRAPINGが容易

EX)POST方式
GET方式よりはセキュリティが高く、データのサイズに制限がない。
⇒あるサイトへ会員登録をしたり、掲示板に口コミを書くときなど、使用される。
⇒WEBページは変更しつつあっても、URLはそのまま
"""