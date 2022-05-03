import smtplib
from email.message import  EmailMessage

id = 'pythontestlhb@gmail.com'
passwd = 'gksqlc9784'


mail_server = smtplib.SMTP('smtp.gmail.com',587)
mail_server.ehlo()
mail_server.starttls()
mail_server.login(id,passwd)
#
# sender = 'lhb0269@naver.com'
# receiver = 'lhb0269@tukorea.ac.kr'
#
# message ="""\
# Subject: Test Mail
# this is auto mail by python
# """

##교수님께 보내는 메일
msg = EmailMessage()
msg['Subject'] = '이한빛 등록 요청'
msg['From'] = 'pythontestlhb@gmail.com'
msg['To'] = 'daehyun.lee.python.test@gmail.com'
msg.set_content('안녕하세요 등록을 요청합니다.')

# with open('Lukaku.jpg','rb')as f:
#     msg.add_attachment(f.read(),maintype ='image',subtype = 'jpeg',filename = 'Lukaku.jpg')

mail_server.send_message(msg)
mail_server.quit()