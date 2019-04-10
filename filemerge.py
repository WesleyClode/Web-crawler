# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 19:55:53 2019

@author: Administrator
"""
import pandas as pd
from pandas import ExcelWriter

print("请输入年月(举例：2018 02 01):")
n, y ,r = map(str, input().split())


date = n+'-'+y+'-'+r

cat_dir1 = 'C:/Users/Administrator/Desktop/数据需求样本/'
cat_dir2 = '/2流量地图/'
cat_dir3 = '/'+n+y+'/【生意参谋平台】无线商品二级流量来源详情-'+date+'_'+date
ban1, ban2, ban3, ban4 = ('A.1童年时光','A.2康一生','A.3Jarrow','A.4Erba Vita')
ban1_product1, ban1_product2, ban1_product3, ban1_product4 = ('钙镁锌','维C','小金豆','有机D3')
ban2_product1, ban2_product2 = ('褪黑素','鱼油')
ban3_product1, ban3_product2 = ('小精灵','月神')
ban4_product1 = '清肠片'
shop = (0,'童年时光海外旗舰店','康一生海外旗舰店','Jarrow海外旗舰店','Erba Vita海外旗舰店')

#流量地图选项卡
#ban1_address1-4
for i in range(1,5):
    exec ("ban1_address%s = cat_dir1 + ban1 +cat_dir2+ ban1_product%s +cat_dir3+'.xls'"%(i,i))
#ban2_address1-2
for i in range(1,3):
    exec ("ban2_address%s = cat_dir1 + ban2 +cat_dir2+ ban2_product%s +cat_dir3+'.xls'"%(i,i))
#ban3_address1-2
for i in range(1,3):
    exec ("ban3_address%s = cat_dir1 + ban3 +cat_dir2+ ban3_product%s +cat_dir3+'.xls'"%(i,i))
#ban4_address1
for i in range(1,2):
    exec ("ban4_address%s = cat_dir1 + ban4 +cat_dir2+ ban4_product%s +cat_dir3+'.xls'"%(i,i))
    
'''品牌地址'''    
product = [ban1_address1, ban1_address2, ban1_address3, ban1_address4, ban2_address1,\
           ban2_address2, ban3_address1, ban3_address2, ban4_address1]

for i in range(0, 9):
    exec ("file%s = product[%s]"%(i,i))


ban = ['钙镁锌','维C','小金豆','有机D3']+['褪黑素','鱼油']+['小精灵','月神']+['清肠片']

for i in range(0,9):
    exec ("df%s = pd.read_excel(file%s,header = None)"%(i,i))
    exec ("length%s = df%s.shape[0]"%(i,i))
    exec ("_Ban%s = pd.Series([ban[%s]]*length%s)"%(i,i,i))
    exec ("_Date%s = pd.Series([date]*length%s)"%(i,i))
    exec ("_df%s = df%s[6:length%s]"%(i,i,i))
    exec ("_df%s.insert(0,'日期', _Date%s)"%(i,i))
    exec ("_df%s.insert(0,'产品名称', _Ban%s)"%(i,i))


liuliang_df = _df0
for i in range(1,9):
    exec ("liuliang_df = liuliang_df.append(_df%s,sort=False)"%i)
liuliang_df.columns = ['产品名称', '日期','来源名称'	,'访客数','浏览量',	'支付金额',	\
          '浏览量占比'	,'店内跳转人数',	'跳出本店人数',	'收藏人数',	'加购人数',	'下单买家数',	\
          '下单转化率',	'支付件数'	,'支付买家数',	'支付转化率',	'直接支付买家数',	\
          '收藏商品-支付买家数',	'粉丝支付买家数'	,'加购商品-支付买家数']
    
'''日报数据'''
for i in range(1,5):
#    exec ("ribao_address%s = cat_dir1 + ban%s +'/3日报数据/日报数据.xlsx'"%(i,i))
    exec ("ribao_address%s = cat_dir1 + ban%s +'/3日报数据/日报数据'+'-'+date+'.xls'"%(i,i))

biaoqian = pd.read_excel(ribao_address1,header = None,index = None)
_biaoqian = biaoqian[7:8]
for i in range(1,5):
    exec ("ribao_df%s = pd.read_excel(ribao_address%s,header = None)"%(i,i))
#    exec ("_shop%s = pd.Series([shop[%s]])"%(i,i))
    exec ("_ribao_df%s = ribao_df%s[8:9]"%(i,i))
#    exec ("print(_shop%s)"%i)
    exec ("_ribao_df%s.insert(0,'品牌名称', shop[%s])"%(i,i))


ribao_df = None
ribao_df = _ribao_df1
for i in range(2,5):
    exec ("ribao_df = ribao_df.append(_ribao_df%s,sort=False)"%i)
    
num = _biaoqian[0:1].shape[1]
list0 = ["品牌名称"]
for i in range(0, num):
    list0.append(_biaoqian.iloc[0,i])
ribao_df.columns = list0



'''产品效果'''

pingpai = (0,'童年时光海外旗舰店','康一生海外旗舰店','Jarrow海外旗舰店','Erba Vita海外旗舰店')

for i in range(1,5):
    exec ("chanpin_address%s = cat_dir1 + ban%s +'/4商品效果/'+n+'/'+n+y+'/【生意参谋】商品效果-'+date+'-'+date+'.xls'"%(i,i))

biaoqian = pd.read_excel(chanpin_address1,header = None)
_biaoqian = biaoqian[3:4]

for i in range(1,5):
    exec ("chanpin_df%s = pd.read_excel(chanpin_address%s,header = None)"%(i,i))
    exec ("length%s = chanpin_df%s.shape[0]"%(i,i))
    exec ("_pingpai%s = pd.Series([pingpai[%s]]*length%s)"%(i,i,i))
    exec ("_Date%s = pd.Series([date]*length%s)"%(i,i))
    exec ("_chanpin_df%s = chanpin_df%s[4:length%s]"%(i,i,i))
    exec ("_chanpin_df%s.insert(0,'日期', _Date%s)"%(i,i))
    exec ("_chanpin_df%s.insert(0,'品牌名称', _pingpai%s)"%(i,i))

chanpin_df = None
chanpin_df = _chanpin_df1
for i in range(2,5):
    exec ("chanpin_df = chanpin_df.append(_chanpin_df%s,sort=False)"%i)
    
num = _biaoqian[0:1].shape[1]
list1 = ['品牌名称','日期']
for i in range(0, num):
    list1.append(_biaoqian.iloc[0,i])
chanpin_df.columns = list1






with ExcelWriter(date+'产品数据'+'.xlsx') as writer:
    liuliang_df.to_excel(writer, sheet_name='流量地图',index = None)
    chanpin_df.to_excel(writer, sheet_name='产品效果',index = None)
    ribao_df.to_excel(writer, sheet_name='日报数据',index = None)
    
    
    
#num = ribao_df[0:1].shape[1]
#list0 = []
#for i in range(0, num):
#    list0.append(ribao_df[0:1][i][0])
#    
    
    
    
    
    
    
#with open( 'all.txt', 'a+') as f:
#    
#    
#
#
#for i in range(1,13):
#    exec ("result = np.concatenate((result, file%s))"%i)
#      
#uniques = np.unique(result)
##uniques = (uniques).encode("utf8")  
#
##f = open(cat_dir + "小皮.txt",'w'):
#with open(cat_dir + '小皮all.txt', 'a+') as f:
#    for i in range(len(uniques)):
#         f.write(uniques[i][-10:]+'\n')
#f.close()
#
#        