# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 09:48:10 2019

@author: Administrator
"""
import requests
from html.parser import HTMLParser
import person
from bs4 import BeautifulSoup
import json
#import re

#获取的cookie值存放在这
myHeader = {"Cookie":"SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWBe.NWUYeIon4BFH.V2I0Y5JpX5oz75NHD95QfSK5XS0eEShqRWs4Dqc_xi--NiKnRi-zpi--fiK.7iKn0i--NiKnRi-zpi--fiK.7iKn0i--Ri-2fi-isi--Ni-iWi-2Ei--ciKLsi-isi--NiKnEiK.Ei--RiKLFiKyF; ALF=1555757534; SUB=_2A25xlxyODeRhGeNL61YW8yzIzTSIHXVTe6TGrDV8PUJbkNBeLRnzkW1NSSa2Ep-X4g0BKdn0pymulkCvQVQz4OAX; _s_tentry=-; Apache=8517431715680.317.1553221045678; SINAGLOBAL=8517431715680.317.1553221045678; ULV=1553221045696:1:1:1:8517431715680.317.1553221045678:; webim_unReadCount=%7B%22time%22%3A1553221209862%2C%22dm_pub_total%22%3A1%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A3%2C%22msgbox%22%3A0%7D"}
#myHeader = {"Cookie":"SINAGLOBAL=1151648924265.729.1510207774298; YF-V5-G0=a9b587b1791ab233f24db4e09dad383c; login_sid_t=663888f6033b6f4a8f5fa48b26d9eb17; YF-Ugrow-G0=ea90f703b7694b74b62d38420b5273df; _s_tentry=passport.weibo.com; Apache=9283625770163.1.1512087277478; ULV=1512087277483:2:1:1:9283625770163.1.1512087277478:1510207774304; SSOLoginState=1512087292; wvr=6; YF-Page-G0=451b3eb7a5a4008f8b81de1fcc8cf90e; cross_origin_proto=SSL; WBStorage=82ca67f06fa80da0|undefined; crossidccode=CODE-gz-1ElEPq-16RrfZ-qpysbLqGTWJetzH095150; SCF=AnQFFpBKBne2YCQtu52G1zEuEpkY1WI_QdgCdIs-ANt1_wzGQ0_VgvzYW7PLnswMwwJgI9T3YeRDGsWhfOwoLBs.; SUB=_2A253IOm1DeThGeNG6lsU-CjOzTWIHXVUVFx9rDV8PUNbmtBeLWTSkW9NS2IjRFgpnHs1R3f_H3nB67BbC--9b_Hb; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5fUsSPaZjP3cB4EXR8M3gT5JpX5KzhUgL.Fo-ReK.f1hqESo.2dJLoIEXLxK.L1hzLBKeLxK-LBo.LBoBLxKML1-zL1-zLxK-LBKBL12qLxK-L1K-L122t; SUHB=0wnlry4ys0tunb; ALF=1543884132; wb_cusLike_5819586269=N; UOR=,,login.sina.com.cn"}
#要爬去的账号的粉丝列表页面的地址<br>

r = requests.get('https://weibo.com/p/1003061305807567/follow?relate=fans&from=100306&wvr=6&mod=headfans&current=fans#place',headers=myHeader)
f = open("test.txt", "w", encoding="UTF-8")
parser = HTMLParser()#解析HTML
parser.feed(r.text)
htmlStr = r.text
 
# 通过script来切割后边的几个通过js来显示的json数组，通过观看源代码
fansStr = htmlStr.split("</script>")
#因为在测试的时候，发现微博每一次返回的dom的顺序不一样，粉丝列表的dom和一个其他内容的dom的位置一直交替，所以在这加了一个判断
tmpJson = fansStr[-2][17:-1] if fansStr[-2][17:-1].__len__()>fansStr[-3][17:-1].__len__() else fansStr[-3][17:-1]
dict = json.loads(tmpJson)
 
soup = BeautifulSoup(dict['html'],  features="lxml")
 
soup.prettify()
f.write(soup.prettify())
i = 0
for divTag in soup.find_all('div'):
    if divTag['class'] == ["follow_inner"]:
        followTag = divTag
        i = i+1
#        print(followTag)
#print(i)
 
if locals().get("followTag"):
    for personTag in followTag.find_all('dl'):
        p = person.person(personTag)
        print(p.__dict__)
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        