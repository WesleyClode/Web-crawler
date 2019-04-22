# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 15:47:53 2019

@author: Administrator
"""


from copyheaders import headers_raw_to_dict
import requests
import time
import json
import math
import traceback

def get_page(identity, headers):
    url ='https://m.weibo.cn/api/comments/show?id='+identity+'&page=1'
    response = requests.get(url=url, headers=headers)
    html = response.text
    json_obj = json.loads(html)
    total_number = json_obj["data"]["total_number"]
    if total_number > 1000:
        page = 100
    else:
        page = math.floor(total_number/10)
    return page

def get_attitudes_page(identity,headers):
    url ='https://m.weibo.cn/api/attitudes/show?id='+identity+'&page=1'
    response = requests.get(url=url, headers=headers)
    html = response.text
    json_obj = json.loads(html)
    return json_obj["data"]["max"]



def get_attitudes(identity, page, headers):
    result = ""
    for i in range(page):
        print('第' + str(i) + '页')
        time.sleep(5)
        url ='https://m.weibo.cn/api/attitudes/show?id='+identity+'&page=' + str(i)
        response = requests.get(url=url, headers=headers)
        html = response.text
        json_obj = json.loads(html)
        try:
            for j in range(len(json_obj["data"]["data"])):
                content = str(json_obj["data"]["data"][j]["user"]["id"])
                result = result + content +'\n'
        except:
            continue
    return result


def get_comments(identity, page, headers):
    result = ""
    for i in range(page):
        print('第' + str(i) + '页')
        time.sleep(5)
        url ='https://m.weibo.cn/api/comments/show?id='+identity+'&page=' + str(i)
        response = requests.get(url=url, headers=headers)
        html = response.text
        json_obj = json.loads(html)
        try:
            for j in range(len(json_obj["data"]["data"])):
                content = str(json_obj["data"]["data"][j]["user"]["id"])+'   '+str(json_obj["data"]["data"][j]["user"]["screen_name"])
                result = result + content +'\n'
        except:
            continue
    return result    
    


def get_statuses(identity, page, headers):
    result = ""
    for i in range(page):
        print('第' + str(i) + '页')
        time.sleep(5)
        url ='https://m.weibo.cn/api/statuses/repostTimeline?id='+identity+'&page=' + str(i)
        response = requests.get(url=url, headers=headers)
        html = response.text
        json_obj = json.loads(html)
        try:
            for j in range(len(json_obj["data"]["data"])):
                content = str(json_obj["data"]["data"][j]["user"]["id"])+'   '+str(json_obj["data"]["data"][j]["user"]["screen_name"])
                result = result + content +'\n'
        except:
            continue
    return result  
    

def write_file(file_name, data, part):
    with open(file_name + part +'.txt', 'a+') as f:
        f.write(data)
    f.close()
    


def main():
    try:
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
        file_name = '#缺觉一代#中国日报'
        identity = '4362932219289158'
        page1 = get_page(identity, headers)
        page2 = get_attitudes_page(identity, headers)
        
        attitudes = get_attitudes(identity, page2, headers)
        write_file(file_name, attitudes, '赞')
        
        comments = get_comments(identity, page1, headers)
        write_file(file_name, comments, '评论')
        
        get_statuses(identity, page1, headers)
        write_file(file_name, comments, '转发')
        
    except Exception as e:
        print("Error: ", e)
        traceback.print_exc()


if __name__ == "__main__":
    main()

