import requests
import time

token = '5197089316:AAFsvX63Cs4Tw60IZK8Be1lVK7bym6sdi4I'
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
number = 0
def print_msg(msg):
    global sender_id
    global number
    sender_id = msg['from']['id']
    sender = msg['from']['first_name']
    if 'text' in msg:
        text = msg['text']
        print(f'{sender}({sender_id}): {text}')
        number = eval(text)
        print(number)
    elif 'photo' in msg:
        caption = msg['caption']
        file_name = msg['photo']['file_name']
        print(f'{sender}({sender_id}) : {caption} file name({file_name})')
        file_id = msg['photo']['file_id']
        file_unique_id = msg['photo']['file_unique_id']

        download_file(file_id,file_name)
# get message to bot
while(True):
    sender_id = None # me
    url = f'https://api.telegram.org/bot{token}/getUpdates'
    r = requests.get(url)
    r.json()
    alist=[]
    if len(r.json()['result']):
        update_list = r.json()['result']
        for update in update_list:
            alist.append(update)
            print_msg(update['message'])
        last_update_id = alist[-1]['update_id']
        params = {
            'offset': last_update_id + 1
        }
        r = requests.get(url, params=params)
        r.json()
        if r.ok:
            update_list = r.json()['result']
            for update in update_list:
                print_msg(update['message'])
        # send message to me
        url = f'https://api.telegram.org/bot{token}/sendMessage'
        params ={
            'chat_id': sender_id,
            'text':number
        }
        r = requests.get(url,params=params)
        time.sleep(2)
#
# url =f'https://api.telegram.org/bot{token}/sendDocument'
# fname = 'asd.jpg'
# with open(fname,'rb') as df:
#     params={
#         'chat_id':sender_id,
#         'caption':'자료',
#     }
#     files={
#         'document':df
#     }
#     r = requests.get(url,params=params,files=files)
#     print(r)
# 파일읽기
# url = f'https://api.telegram.org/bot{token}/getUpdates'
# params ={
#     'offset' : 357419078
# }
# r = requests.get(url,params=params)
# r.json()
# 
# params = {
#     'file_id':'BQACAgUAAxkBAAMHYnsH66SGqdYIyIetCG_T87QaVSEAAvAEAAIuWdlXEiEkUu9BDjAkBA'
# }
# url = f'https://api.telegram.org/bot{token}/getFile'
# r = requests.get(url,params=params)
