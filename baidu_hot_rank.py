from bs4 import BeautifulSoup
import requests
import time
import re
import os

requests.packages.urllib3.disable_warnings()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}
base_url = "https://top.baidu.com/board?tab=realtime"
response  = requests.get(base_url,headers=headers,verify=False)
html = response.text
soup = BeautifulSoup(html)
a_list = soup.findAll('a',class_='title_dIF3B')
filename = time.strftime("%Y-%m-%d_%H", time.localtime())
filedir = time.strftime("%Y-%m-%d", time.localtime())

# 过滤
re_url = '.*(https.*?)"'
re_content = '.*sis">(.*?)<'


if not os.path.exists('./data/{}'.format(filedir)):
     os.makedirs('./data/{}'.format(filedir))


with open('./data/{}/{}.md'.format(filedir, filename),'w+') as f:
    for idx,obj in enumerate(a_list):
        content = re.match(re_content,str(obj),re.I).group(1).strip()
        url = re.match(re_url,str(obj),re.I).group(1)
        str_news = str(idx+1)+".["+content+"]("+url+")"+"\n"
        f.write(str_news)

