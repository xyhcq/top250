# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import time
import sys

def getHTMLText(url,k):
    # 获取网页源代码
    try:
        if(k==0):
            kw={}
        else:
            kw={'start':k,'filter':''}
        # 保存获取的网页
        read = requests.get(url,params=kw,headers={'User-Agent': 'Mozilla/4.0'})
        read.raise_for_status()
        read.encoding = read.apparent_encoding
        return read.text
    except:
        print("获取失败!")

def getData(html):
    # 分析代码信息，提取数据
    soup = BeautifulSoup(html, "html.parser")

    # 找到第一个class属性值为grid_view的ol标签
    movieList=soup.find('ol',attrs={'class':'grid_view'})


    # 找到所有的li标签
    for movieLi in movieList.find_all('li'):    
        # 找到第一个class属性值为hd的div标签
        movieHd=movieLi.find('div',attrs={'class':'hd'})
        # 找到第一个class属性值为title的span标签 #也可使用.string方法

        # 获取电影名字
        if swName == 1:
            movieName=movieHd.find('span',attrs={'class':'title'}).getText()
            if showInfo==1:
                print movieName
            else:pass
            # 写入文件
            if writeFile == 1:
                f.write('电影名:'+movieName.encode('utf-8')+'    ')
            else:pass
        else:pass

        # 获取电影链接
        if swUrl == 1:
            movieUrl=movieHd.find('a class="" href="')
            if showInfo==1:
                print movieUrl
            else:pass
            # 写入文件
            if writeFile == 1:
                f.write('链接:'+str(movieUrl)+'    ')
            else:pass
        else:pass

        # 获取电影导演/演员
        if swStaff == 1:
            movieBd = movieLi.find('div', attrs={'class': 'bd'})
            movieSF=movieBd.find('p',attrs={'class':''}).getText()
            if showInfo==1:
                print movieSF
            else:pass
            # 写入文件
            if writeFile == 1:
                f.write('Staff:'+movieSF.encode('utf-8')+'    ')
            else:pass
        else:pass

        # 获取电影的评分
        if swScore == 1:
            movieScore=movieLi.find('span',attrs={'class':'rating_num'}).getText()
            if showInfo==1:
                print movieScore
            else:pass
            # 写入文件
            if writeFile == 1:
                f.write('评分:'+movieScore.encode('utf-8')+'    ')
            else:pass
        else:pass

        #获取电影的评论数
        if swEvalNum == 1:
            movieEval=movieLi.find('div',attrs={'class':'star'})
            movieEvalNum=re.findall(r'\d+',str(movieEval))[-1]
            if showInfo==1:
                print movieEvalNum
            else:pass
            # 写入文件
            if writeFile == 1:
                f.write('评论数:'+movieEvalNum.encode('utf-8')+'    ')
            else:pass
        else:pass

        # 获取电影短评
        if swQuote == 1:
            movieQuote = movieLi.find('span', attrs={'class': 'inq'})
            # 有的电影没有短评，为防止报错，加次
            if(movieQuote):
                if showInfo==1:
                    print movieQuote.getText()
                else:pass
                # 写入文件
                if writeFile == 1:
                    f.write('短评:'+movieQuote.getText().encode('utf-8')+'\n')
                else:pass
            else:
                # 写入文件
                if writeFile == 1:
                    f.write('短评:'+"这个电影没有短评"+'\n')
                else:pass
        else:pass
        #print '================================================================='
        
# 本次抓取的网址
basicUrl='https://movie.douban.com/top250'
k=0
i=1

# 一些自定义功能开关，1开启，0关闭
# 控制台输出抓取结果
showInfo = 1
# 写入文件开关
writeFile = 1
# 电影名开关
swName = 1
# 链接开关
swUrl = 1
# 导演/演员
swStaff = 1
# 评分
swScore = 1
# 评论数
swEvalNum =1 
# 短评
swQuote = 1

# 打开文件
f=open("top250.txt","w")
f.write('豆瓣top250信息爬取，by forward团队'+'\n'+'爬取结果：'+'\n')

showInfo=raw_input('是否需要在窗口显示结果，是为1，否为0，默认值为1：')
if showInfo != '1':
    showInfo=0
else :
    showInfo =1
    

writeFile=raw_input('是否需要将结果输出到文件，是为1，否为0，默认值为1：')
if writeFile != '1':
    writeFile=0
else :
    writeFile=1

swName=raw_input('是否需要抓取电影名，是为1，否为0，默认值为1：')
if swName != '1':
    swName=0
else:
    swName=1

swUrl=raw_input('是否需要抓取电影链接，是为1，否为0，默认值为1：')
if swUrl != '1':
    swUrl=0
else:
    swUrl=1

swStaff=raw_input('是否需要抓取职员，是为1，否为0，默认值为1：')
if swStaff != '1':
    swStaff=0
else:
    swStaff=1

swScore=raw_input('是否需要抓取评分，是为1，否为0，默认值为1：')
if swScore != '1':
    swScore=0
else:
    swScore=1

swEvalNum=raw_input('是否需要抓取评论数，是为1，否为0，默认值为1：')
if swEvalNum != '1':
    swEvalNum=0
else:
    swEvalNum=1

swQuote=raw_input('是否需要抓取短评，是为1，否为0，默认值为1：')
if swQuote != '1':
    swQuote=0
else:
    swQuote=1

print '===============================魔法开始==============================='

while k<=225:
    html=getHTMLText(basicUrl,k)
    time.sleep(2)
    k+=25
    getData(html)
    print '-------第'+str(i)+'轮完成!-------'
    i+=1
f.write('\n'+'爬取完成！')
# 关闭文件，否则容易写入不全    
f.close()
print '完成！'
