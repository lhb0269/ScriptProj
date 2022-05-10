import json
import requests

params = {
    'city':'Seoul',
    'name':'Suji',
}
r = requests.get('https://httpbin.org/get',params=params)

def print_dict(d):
    for k,v in d.items():
        print(k,': ',v)

r = requests.get('https://httpbin.org')
r.status_code
r.headers
r.Headers['content-type']

r.text
r.encoding
r.url
r.content

json_data_string = '[1,"Suji",true,false,3.14]'
data_list = json.loads(json_data_string)

data_list.append('Rose')
json.dumps(data_list)

suji_data = {
    'city':'Seoul',
    'name':'Suji',
    'age':22
}