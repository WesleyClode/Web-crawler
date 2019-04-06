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
    chanpin.append(df[1][i])

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
    for j in chanpin:
        url_temp= url+str(j)
        html = getHtml(url_temp, loadmore = False, waittime = 1)
        result = BeautifulSoup(html,features="lxml").text
        collection.append(re.findall(r"月销量(.+?)\n",result))
    for i in range(1,df[1].size):
        df[3][i] = collection[i-1] 
    
    with ExcelWriter(date+'产品数据'+'.xlsx') as writer:
        liuliang_df.to_excel(writer, sheet_name='流量地图',index = None)
    
