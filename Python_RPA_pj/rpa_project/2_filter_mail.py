# 제목 : 파이썬 특강 신청합니다.
# 본문 : 닉네임/전화번호 뒤 4자리 (Random)
#         (예) 박예진/1234

import smtplib
from account import *
from imap_tools import MailBox
from email.message import EmailMessage

max_val = 3 # 최대 선정자 수
applicant_list = [] # 지원자 리스트

print("[1. 지원자 메일 조회]")
with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    index = 1 # 순번
    for msg in mailbox.fetch('(SENTSINCE 25-Sep-2022)'):
        if "Python 팬사인회" in msg.subject:
            nickname, phone = msg.text.strip().split("/")
            print("순번: {} 닉네임: {} 전화번호: {}".format(index, nickname, phone))
            applicant_list.append((msg, index, nickname, phone))
            index += 1
