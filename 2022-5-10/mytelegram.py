import requests


token = '5336659329:AAF-94FBfKrLZUxVjVSLZoIu0lMfWHr4hiY'
r = requests.get(f'https://api.telegram.org/bot{token}/getMe')

r.headers
r.headers['content-type']
r.json()

def download_file(file_id,file_name):
    params = {
        'file_id':file_id
    }
    r= requests.get(f'https://api.telegram.org/bot{token}/getFile', params=params)
    if r.ok:
        print(r.json())
        telegram_file_path = r.json()['result']['file_path']

    with open(file_name,'wb') as wf:
        print(f'writing {file_name} ....')
        r= requests.get(f'https://api.telegram.org/file/bot{token}/' + telegram_file_path)
        if r.ok:
            wf.write(r.content)
        print('....done')

def print_msg(msg):
    global sender_id
    sender_id = msg['from']['id']
    sender = msg['from']['first_name']
    if 'text' in msg:
        text = msg['text']
        print(f'{sender}({sender_id}): {text}')
    elif 'document' in msg:
        caption = msg['caption']
        file_name = msg['document']['file_name']
        print(f'{sender}({sender_id}) : {caption} file name({file_name})')

        file_id = msg['document']['file_id']
        file_unique_id = msg['document']['file_unique_id']

        download_file(file_id,file_name)
# get message to bot

sender_id = None # me
url = f'https://api.telegram.org/bot{token}/getUpdates'
r = requests.get(url)
r.json()
if r.ok:
    update_list = r.json()['result']
    for update in update_list:
        print_msg(update['message'])

# # send message to me
# url = f'https://api.telegram.org/bot{token}/sendMessage'
# params ={
#     'chat_id': sender_id,
#     'text':'안녕하세요. 저는 손흥민 봇입니다. 반갑습니다.'
# }
# r = requests.get(url,params=params)
#
url =f'https://api.telegram.org/bot{token}/sendDocument'
fname = 'asd.jpg'
with open(fname,'rb') as df:
    params={
        'chat_id':sender_id,
        'caption':'자료',
        'photo':'https://ksc.tukorea.ac.kr/sso/images/login/logo_new.png'
    }
    files={
        'document':df
    }
    r=requests.get(url,params=params,files=files)
    print(r)
