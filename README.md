# 添付ファイル付きのダイレクトメールを送信するPythonスクリプト集

Gmail用の作成しています。Googleアカウントの「セキュリティ」設定で「安全性の低いアプリのアクセスをオンにしてください。

tuple/ ・・・　タプル内に送信先と添付ファイルを指定
- sendmail.pyの「## 初期設定」の部分を書き換えてください。
- sendmail.pyの43~44行目の「message = message.replace("置き換え前の文字列", 置き換え後の文字列を格納した変数)」で名前や日時、場所をメッセージに差し込んでいます。
