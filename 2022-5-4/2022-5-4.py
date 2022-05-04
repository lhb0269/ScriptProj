# import csv
#
# import imapclient
# from email.message import  EmailMessage
# import imaplib
# import email
# from email.policy import default
#
# imap_server = imapclient.IMAPClient('imap.gmail.com',ssl=True)
#
# id = 'pythonlhb@gmail.com'
# pwd = 'gksqlc9784'
#
# imap_server.login(id,pwd)
#
# imap_server.select_folder('INBOX',readonly=True)
#
# import imaplib
# imaplib._MAXLINE = 10000000
#
# message_id_list = imap_server.gmail_search('이한빛 재등록 요청')
#
# for id,raw_message in imap_server.fetch(message_id_list,'RFC822').items():
#     email_message = email.message_from_bytes(raw_message[b'RFC822'],policy=default)
#     subject = email_message['Subject']
#     name = subject.split()[0]
#     print(name,email_message['From'])
# # def print_message(msg):
# #     for part in msg.walk():
# #         if part.get_content_maintype() == 'multipart':
# #             continue
# #     if part.get_content_maintype() == 'text':
# #         bytes = part.get_payload(decode=True)
# #         encode = part.get_content_maintype_charset()
# #         print(str(bytes,encode))
# #     else:
# #         fname = part.get_filename()
# #         if fname:
# #             print(fname)
# #             with open(fname,'wb')as fp:
# #                 fp.write(part.get_payload(decode=True))

import smtplib
import csv
from email.message import  EmailMessage
id = 'pythonlhb@gmail.com'
pwd = 'gksqlc9784'


mail_server = smtplib.SMTP('smtp.gmail.com',587)
mail_server.ehlo()
mail_server.starttls()
mail_server.login(id,pwd)

msg = EmailMessage()

with open('_address.csv',newline='')as f:
    reader = csv.reader(f,skipinitialspace = True)
    data = list(reader)


msg['Subject'] = '안녕하세요 반갑습니다.'
msg['From'] = 'pythonlhb@gmail.com'
for mail in data:
    msg['To'] = f'{mail[1]}'
    msg.set_content(f'안녕하세요 {mail[0]}님.반갑습니다. 저는 이한빛이라고 합니다. 잘 부탁드립니다.')

    with open('asd.jpg','rb')as f:
        msg.add_attachment(f.read(),maintype ='image',subtype = 'jpeg',filename = 'asd.jpg')
    mail_server.send_message(msg)

    del msg['To']
    msg.clear_content()
mail_server.quit()