# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:07:32 2019

@author: Administrator
"""

def getCookie(get_cookie_url):
　　'''
　　@功能：获取cookie，并存储在cookieJar进行管理
　　'''
　　cj = cookielib.CookieJar()
　　opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
　　urllib2.install_opener(opener)
　　resp = urllib2.urlopen(get_cookie_url)