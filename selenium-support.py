# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 15:04:11 2019

@author: Administrator
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time
import pandas as pd
from pandas import ExcelWriter


cat_dir = 'C:/Users/Administrator/Desktop/竞品ID.xlsx'
df = pd.read_excel(cat_dir,header = None)
chanpin = []
for i in range(1,df[1].size):
    chanpin.append([df[1][i],df[2][i]])

url = 'https://detail.tmall.hk/hk/item.htm?id='

def getHtml(url, loadmore = False, waittime = 1):
    # browser = webdriver.Firefox()
    browser = webdriver.Chrome('chromedriver')
    browser.get(url)
    time.sleep(waittime)
    html = browser.page_source
    browser.quit()
    return html

    

if __name__ == "__main__":
    collection = []
    for product in chanpin:
        url_temp= url+str(product[0])
        html = getHtml(url_temp, loadmore = False, waittime = 1)
        result = BeautifulSoup(html,features="lxml").text
        if product[1] == '天猫':
            collection.append(re.findall(r"月销量(.+?)\n",result))
        else:
            collection.append(re.findall(r"\n(.+?)\n交易成功",result))

        
    
    for i in range(1,df[1].size):
        df[1][i] = str(df[1][i])
        df[3][i] = str(collection[i-1][0])
    
    with ExcelWriter('竞品销量.xlsx') as writer:
        df.to_excel(writer, sheet_name='sheet2',index = None,header = None)
    
