from bs4 import BeautifulSoup
import requests

with open('test.html') as f:
    soup = BeautifulSoup(f,'lxml')

for link in soup.find_all('a'):
    print(link['href'])



headers = {
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}
keyword = '신라면'
url = f'https://www.google.com/search?q={keyword}'
r = requests.get(url,headers=headers)
if r.ok:
    with open('google_shin_html','wb') as wf:
        wf.write(r.content)
        print(r.text)

soup = BeautifulSoup(r.text,'lxml')
elms = soup.select('div[id = "bres"] a b')
for e in elms:
    print(f'{keyword} {e.string}')