# [신청 메일 양식]
# 제목 : 파이썬 특강 신청합니다.
# 본문 : 닉네임/전화번호 뒤 4자리(Random)
#         (예) 박예진/1234

import smtplib
from random import *
from account import *
from email.message import EmailMessage

nicknames = ["짱구", "유리", "철수", "맹구", "훈이"]

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for nickname in nicknames:
        msg = EmailMessage()
        msg["Subject"] = "Python 팬사인회 신청합니다."
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = "qkrdpwls1007@gmail.com"

        #content = nickname + "/" + str(randint(1000, 9999))
        content = "/".join([nickname, str(randint(1000, 9999))])
        msg.set_content(content)
        smtp.send_message(msg)
        print("'" + nickname + "'님이 박예진님 계정으로 메일 발송 완료")