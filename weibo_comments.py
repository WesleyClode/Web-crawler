# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 15:47:53 2019

@author: Administrator
"""

#https://m.weibo.cn/api/comments/show?id=4362559412573445&page=1


from copyheaders import headers_raw_to_dict
import requests
import time
import json
import math


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


name = '#缺觉一代#人民日报'
num = 1
identity = '4362783694613882'




totalnum = 0
url ='https://m.weibo.cn/api/comments/show?id='+identity+'&page=1'
response = requests.get(url=url, headers=headers)
html = response.text
json_obj = json.loads(html)
total_number = json_obj["data"]["total_number"]
if total_number > 1000:
    page = 100
else:
    page = math.floor(total_number/10)


#
#with open('赞.txt', 'a+') as f:
#    for i in range(1, 65):
#        print('第' + str(i) + '页')
#        time.sleep(5)
#    
#    #    url = 'https://weibo.cn/comment/HjNyl82IU?uid=5852861043&rl=0&page=' + str(i)
#        url ='https://m.weibo.cn/api/attitudes/show?id='+identity+'&page=' + str(i)
#        response = requests.get(url=url, headers=headers)
#        html = response.text
#    #    print(html)
#        json_obj = json.loads(html)
#    #    for j in range(len(json_obj["data"]["data"])):
#    #    result = json_obj["data"]["data"][1]["user"]["id"]
#        try:
#            for j in range(len(json_obj["data"]["data"])):
#                name = str(json_obj["data"]["data"][j]["user"]["id"])
#                f.write(name + '\n')
#        except:
#            continue     
#f.close()




with open(name+str(num)+'.txt', 'a+') as f:
    for i in range(page):
        print('第' + str(i) + '页')
        time.sleep(5)
    
    #    url = 'https://weibo.cn/comment/HjNyl82IU?uid=5852861043&rl=0&page=' + str(i)
        url ='https://m.weibo.cn/api/comments/show?id='+identity+'&page=' + str(i)
        response = requests.get(url=url, headers=headers)
        html = response.text
    #    print(html)
        json_obj = json.loads(html)
    #    for j in range(len(json_obj["data"]["data"])):
    #    result = json_obj["data"]["data"][1]["user"]["id"]
        try:
            for j in range(len(json_obj["data"]["data"])):
                name = str(json_obj["data"]["data"][j]["user"]["id"])+'   '+str(json_obj["data"]["data"][j]["user"]["screen_name"])
                f.write(name + '\n')
        except:
            continue     
f.close()



with open(name+str(num)+'.txt', 'a+') as f:
    for i in range(page):
        print('第' + str(i) + '页')
        time.sleep(5)
    #    url = 'https://weibo.cn/comment/HjNyl82IU?uid=5852861043&rl=0&page=' + str(i)
        url ='https://m.weibo.cn/api/statuses/repostTimeline?id='+identity+'&page=' + str(i)
        response = requests.get(url=url, headers=headers)
        html = response.text
    #    print(html)
        json_obj = json.loads(html)
    #    for j in range(len(json_obj["data"]["data"])):
    #    result = json_obj["data"]["data"][1]["user"]["id"]
        try:
            for j in range(len(json_obj["data"]["data"])):
                name = str(json_obj["data"]["data"][j]["user"]["id"])+'   '+str(json_obj["data"]["data"][j]["user"]["screen_name"])
                f.write(name + '\n')
        except:
            continue     
f.close()