#!/usr/bin/env python #coding=utf-8

##########################
# 
# 此脚本可下载乐视视频
# using py youku.py 下载目录 视频名字(必须是电视剧)
#
#########################


from bs4 import BeautifulSoup
import urllib,sys
import re
import os
from urllib2 import urlopen
import chardet
import sys
import re
reload(sys)
sys.setdefaultencoding('utf8') #设置整个文件为UTF-8的编码

base_curl="" #全局变量
path=''
dictv = {}
i=0



#检索每一集url
def opencurl( strobj ):
	arrycurl=[]
	mpHtml = urllib.urlopen( strobj ).read()
	soup = BeautifulSoup(mpHtml,"html5lib")
	curl = soup.find_all('div',class_='item')
	for line in curl:
		if line.a:
			obj = 'http:'+line.a.get('href')
			arrycurl.append(obj)

	print '共找到'+str(len(arrycurl))+'集'
	cmd  = raw_input("\n是否要下载[Y/N]:") #等待用户输入
	if cmd=='Y' or cmd == 'y' :
		print 'yes'
		for curl in arrycurl:
			objcurl(curl) #开始下载每一集
	else:
		print 'no'
	
def objcurl(strobj):#把每一集下载到指定目录
	flag = os.system('python3 /home/pi/Git/you-get/you-get' + ' ' + '-o '+path+ ' ' + strobj )
	if flag != 0:
		print '========================='
		print 'errr' +' ' +strobj
		print '========================='
#main
#检测输入参数
if len(sys.argv)!=3:
	print 'useage:py youkufid.py + path + 剧名'
	exit (0)
else:
	path='/media/pi/sqf_500g/'+sys.argv[1]
#	path=sys.argv[1]
	base_curl='http://so.le.com/s?wd='+sys.argv[2]
        print 'sqf==='+path
if not os.path.exists(path): # 判断目录是否存在
	os.makedirs(path)  # 创建多级目录


try:
        m = 0
        begin = 0
        end = 0
        n=0
        pattern = re.compile(r'keyWord')
	mpHtml = urllib.urlopen(base_curl).read()
	soup = BeautifulSoup(mpHtml,"html5lib")
	curl = soup.find_all('div',class_='So-detail Tv-so')
        for line in curl: #找到电视剧名，开始与结束的位置
            curl_id = line.get('data-info').split(',')
            for i in range(len(curl_id)):
                if curl_id[i].find('keyWord:')>-1:
                    m=m+1
                    name=str(m)+'_'+curl_id[i].split(':')[1]
                    print name
                if curl_id[i].find('vidEpisode:') > -1: #找到开始的
                    begin=i

                if curl_id[i].find('previewEpisode') > -1: #找到结尾
                    end = i

            n=0
            for i in range(begin,end):
                if curl_id[i].find('-') > -1:
                    objname=name+'_'+str(n)
                    objcur=curl_id[i].split('-')[1]
                    dictv[objname]=objcur
                    n=n+1
except AttributeError:
	print '没有找到该剧的资源!!!!'
	exit(-1)

a = raw_input("请输入你要下载的电视剧号:")
if str(a)=='N' or str(a)=='n':
    exit(0)

for key in dictv:
    if key.split('_')[0]==a:
        print key
        curl='http://www.le.com/ptv/vplay/'+dictv[key].replace('\'','')+'.html'
        objcurl(curl) 
