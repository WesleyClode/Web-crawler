# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 17:17:23 2019

@author: Administrator
"""


import re 
import collections
import pandas as pd
import numpy as np 
import jieba
import wordcloud 
from PIL import Image # 图像处理库
import matplotlib.pyplot as plt # 图像展示库

# 读取文件

#file = 'C:/Users/Administrator/Desktop/文件/code/小钢铁侠竞品&评价.xlsx'
NAME = '小钢铁侠竞品&评价'
file = 'C:/Users/Administrator/Desktop/文件/code/'+NAME+'.xlsx'

df = pd.read_excel(file,sheet_name='小钢铁侠评价',header = None)
#df = pd.read_excel(file,header = None)
length = df.shape[0]
_df = df[1:length]
string_data=''
for i in _df[2]:
    if i != '此用户没有填写评价。' or _df[2][1]:
        string_data += str(i)
        

# 文本预处理
pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"') # 定义正则表达式匹配模式
string_data = re.sub(pattern, '', string_data) # 将符合模式的字符去除

# 文本分词
seg_list_exact = jieba.cut(string_data, cut_all = False) # 精确模式分词
#seg_list_exact = jieba.cut_for_search(string_data) # 精确模式分词


object_list = []
remove_words = [u'的', u'，',u'和', u'是', u'随着', u'对于', u'对',u'等',u'能',u'都',u'。',u' ',u'、',u'中',u'在',u'了',u'！',u'很',u'也',u'吃',u'给',
                u'通常',u'如果',u'我们',u'需要','喝',u'宝宝',u'好',u'我',u'还',u'…',u'就',u'有',u'不',u'�',u'nannan',u'nan'] # 自定义去除词库

for word in seg_list_exact: # 循环读出每个分词
    if word not in remove_words: # 如果不在去除词库中
        object_list.append(word) # 分词追加到列表

# 词频统计
word_counts = collections.Counter(object_list) # 对分词做词频统计
word_counts_top10 = word_counts.most_common(20) # 获取前10最高频的词
print (word_counts_top10) # 输出检查

# 词频展示
#mask = np.array(Image.open('wordcloud.jpg')) # 定义词频背景
wc = wordcloud.WordCloud(
    font_path='C:/Windows/Fonts/simhei.ttf', # 设置字体格式
#    mask=mask, # 设置背景图
    max_words=20000, # 最多显示词数
    width=2000,
    height=1400,
    min_font_size=50,
    max_font_size=700
)

wc.generate_from_frequencies(word_counts) # 从字典生成词云
#image_colors = wordcloud.ImageColorGenerator(mask) # 从背景图建立颜色方案
#wc.recolor(color_func=image_colors) # 将词云颜色设置为背景图方案
plt.imshow(wc) # 显示词云
plt.axis('off') # 关闭坐标轴
plt.rcParams['savefig.dpi'] = 300 #图片像素
plt.rcParams['figure.dpi'] = 300 #分辨率
plt.savefig(('C:/Users/Administrator/Desktop/'+NAME+'.jpg'))
plt.show() # 显示图像
