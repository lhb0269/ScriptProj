import smtplib
from email.message import  EmailMessage
mail_server = smtplib.SMTP('localhost:8025')
#
# sender = 'lhb0269@naver.com'
# receiver = 'lhb0269@tukorea.ac.kr'
#
# message ="""\
# Subject: Test Mail
# this is auto mail by python
# """
id = 'pythontestlhb@gmail.com'
passwd = 'gksqlc9784'
msg = EmailMessage()
msg['Subject'] = 'Test Mail'
msg['From'] = 'lhb0269@naver.com'
msg['To'] = 'lhb0269@tukorea.ac.kr'
msg.set_content('이것은 파이썬으로 자동 발송된 메일입니다.')

with open('Lukaku.jpg','rb')as f:
    msg.add_attachment(f.read(),maintype ='image',subtype = 'jpeg',filename = 'Lukaku.jpg')

mail_server.send_message(msg)
mail_server.quit()