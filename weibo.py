# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 18:20:47 2019

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
    
#    评论信息
    result_1 = soup.find_all(class_='ctt')
    
#    点赞数
    result_2 = soup.find_all(class_='cc')
    
#    评论时间
    result_3 = soup.find_all(class_='ct')
    
#    获取用户名
    result_4 = re.findall('id="C_.*?href="/.*?">(.*?)</a>', html)
    
    try:
        for j in range(len(result_1)):
            # 获取点赞数
            res = re.findall('(\d+)', result_2[j * 2].get_text())
            if len(res) >= 0:
                praise = res[0]
                name = result_4[j]
                text = result_1[j].get_text().replace(',', '，')
                date = result_3[j].get_text().split(' ')[0]
                # print(praise)
                if '@' in text:
                    if ':' in text:
                        # 去除@及用户信息  example:  回复@女开开开心心:是不是之前领取过了？只能领一次哦
                        comment = text.split(':')[-1]
#                        print(name, comment, praise, date)
                        print(name)
                        # 写入csv
                        with open('list.csv', 'a+') as f:
#                            f.write(name + ',' + comment + ',' + praise + ',' + date + '\n')
                            f.write(name + '\n')
                        f.close()
                    else:
                        # 无评论信息时
#                        print(name, '无', praise, date)
                        print(name)
                        with open('list.csv', 'a+') as f:
#                            f.write(name + ',' + '无' + ',' + praise + ',' + date + '\n')
                            f.write(name + '\n')
                        f.close()
                else:
                    # 只有评论信息
#                    print(name, text, praise, date)
                    print(name)
                    # 写入csv
                    with open('list.csv', 'a+') as f:
#                        f.write(name + ',' + text + ',' + praise + ',' + date + '\n')
                        f.write(name + '\n')
                    f.close()
            else:
                pass
    # 出现字符编码报错
    except:
        continue    
