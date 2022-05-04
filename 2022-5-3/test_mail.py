import smtplib
from email.message import  EmailMessage
id = 'pythonlhb@gmail.com'
pwd = 'gksqlc9784'


mail_server = smtplib.SMTP('smtp.gmail.com',587)
mail_server.ehlo()
mail_server.starttls()
mail_server.login(id,pwd)
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
msg['Subject'] = '안녕하세요 반갑습니다.'
msg['From'] = 'pythonlhb@gmail.com'
msg['To'] = 'daehyun.lee.python.test@gmail.com'
msg.set_content(f'안녕하세요 {}.')

# with open('Lukaku.jpg','rb')as f:
#     msg.add_attachment(f.read(),maintype ='image',subtype = 'jpeg',filename = 'Lukaku.jpg')

mail_server.send_message(msg)
mail_server.quit()