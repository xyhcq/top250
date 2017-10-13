# -*- coding:utf-8 -*-
import re
#from bs4 import BeautifulSoup

def getHtml():
    # 用于获取豆瓣top250网站信息
    pass

def getData():
    # 解析html,存储获取到的信息
    # 用于分析获取到的信息

    #电影标题
    title = []
    #电影评论数
    rating_num = []
    range_num = []
    #演员
    actor = []
    data = {}
    pass

def getInfo():
    # 用于处理获取到的信息，如存到列表中
    # 重点来了，我们不会正则表达式，但是必须用。现在正在学习！！！
    pass

def writeMovie():
    # 用于将结果写入到文件中
    f=open("top250.txt","w")
    f.write("test")
    f.close()

getHtml()
getData()
getInfo()
writeMovie()


