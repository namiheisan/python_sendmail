#!/usr/bin/env python3

import email.mime.text
import email.mime.application
import email.mime.multipart
import smtplib
import os.path

## 初期設定
# 号数（go）
go = 1

# 送信先の数（count）、メールアドレス（to_email）、名前（dist_name）、添付ファイル（mail_file）
count = 2
to_email = ('xxxx@example.com', 'yyyy@example.com')
dist_name = ('高橋', '山田')
mail_file = ('./招待状_高橋様.png', './招待状_山田様.png')

# メッセージ
message_template = "./message.txt"
date = "8月5日（水） 18:00～"
place = "レストラン「Python」"

# 認証情報
account = "Gmailのアドレス（～@gmail.com）"
password = "Googleアカウントのパスワード"

# 送信元
from_email = account

# タイトル
subject = "【メールマガジン %s号】イベント開催" % go

## 送信処理
for i in range(count):
    #ヘッダー、メッセージ作成
    msg = email.mime.multipart.MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email[i]
    with open(message_template) as f:
        message = f.read()
    message = message.replace("#NAME#", dist_name[i])
    message = message.replace("#DATE#", date)
    message = message.replace("#PLACE#", place)
    msg.attach(email.mime.text.MIMEText(message))

    # ファイル添付生成
    tenpufilepath = mail_file[i]
    with open(tenpufilepath, "rb") as f:
        tenpufile = email.mime.application.MIMEApplication(f.read(), Name=os.path.basename(tenpufilepath))
    tenpufile['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(tenpufilepath)
    msg.attach(tenpufile)

    # メール送信
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(account, password)
    server.send_message(msg)
    server.quit()
