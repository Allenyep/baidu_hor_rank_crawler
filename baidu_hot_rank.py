from bs4 import BeautifulSoup
import requests
import time
import re
import os

requests.packages.urllib3.disable_warnings()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}
tab_list = ['realtime','novel','movie','teleplay','cartoon','variety','documentary','star','car','game']
tab_dict = {
    'realtime': '热搜',
    'novel':'小说',
    'movie':'电影',
    'teleplay':'电视剧',
    'cartoon':'动漫',
    'variety':'综艺',
    'documentary':'纪录片',
    'car':'汽车',
    'game':'游戏'
}
base_url = "https://top.baidu.com/board?tab="

filename = time.strftime("%Y-%m-%d_%H", time.localtime())
filedir = time.strftime("%Y-%m-%d", time.localtime())
# 过滤
re_url = '.*(https.*?)"'
re_content = '.*sis">(.*?)<'

if not os.path.exists('./data/{}'.format(filedir)):
     os.makedirs('./data/{}'.format(filedir))

for i in tab_list:
    response  = requests.get(base_url + i,headers=headers,verify=False, timeout=(50, 30))
    soup = BeautifulSoup(response.text)
    a_list = soup.findAll('a',class_='title_dIF3B')
    with open('./data/{}/{}.md'.format(filedir, filename),'a') as f:
        f.write("\n" + tab_dict[i] + "\n")
        for idx,obj in enumerate(a_list):
            content = re.match(re_content,str(obj),re.I).group(1).strip()
            url = re.match(re_url,str(obj),re.I).group(1)
            str_news = str(idx+1)+".["+content+"]("+url+")"+"\n"
            f.write(str_news)

