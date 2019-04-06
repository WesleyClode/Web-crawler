# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 20:21:13 2019

@author: Administrator
"""

from copyheaders import headers_raw_to_dict
from bs4 import BeautifulSoup
import requests
import time
import re

headers = b"""
accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
accept-encoding:gzip, deflate, br
accept-language:zh-CN,zh;q=0.9
cache-control:max-age=0
cookie:_T_WM=7b01809efebbf4591817160024e1b6a6; WEIBOCN_WM=3333_2001; SCF=AteYQ3Fn2RHnmdtLq7-P7aC9_YRjVMYq1xxQNzuNXBhqmw4Z8DQJ3rPSMkWAtZuZSXpQxc9w_BI7FQldOaoGW6o.; SUB=_2A25xlxyODeRhGeNL61YW8yzIzTSIHXVTe6TGrDV6PUJbkdAKLWulkW1NSSa2EgDEwD6DyS0MdOhlDCS7DVAoMx1o; SUHB=0BLoPb1nuQTHiT; SSOLoginState=1553165534; MLOGIN=1; XSRF-TOKEN=58c003; M_WEIBOCN_PARAMS=featurecode%3Dnewtitle%26oid%3D4346211433851508%26luicode%3D10000011%26lfid%3D102803; WEIBOCN_FROM=1110106030
upgrade-insecure-requests:1
user-agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36
"""

# 将请求头字符串转化为字典
headers = headers_raw_to_dict(headers)


for i in range(2, 59):
    print('第' + str(i) + '页')
    time.sleep(5)

#    url = 'https://weibo.cn/comment/HjNyl82IU?uid=5852861043&rl=0&page=' + str(i)
    url ='https://weibo.cn/comment/Hjoazg9X6?ckAll=1&page=' + str(i)
    response = requests.get(url=url, headers=headers)
    html = response.text
#    print(html)
    soup = BeautifulSoup(html, 'html.parser')
    
    result = re.findall('id="C_.*?href="/.*?">(.*?)</a>', html)
    
    try:
        for j in range(len(result)):
            name = result[j]
            with open('阿卯卯3.4号评论.csv', 'a+') as f:
                f.write(name + '\n')
            f.close()
    except:
        continue     