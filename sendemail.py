#!/usr/bin/python
#-*- encoding: utf-8 -*-

#ps:这是一个自动发送邮件系统
#author:sqf
#create time :2017年4月22日14:15:22
#用法: python sendemail + "标题" + "邮件内容"

import os, sys
import smtplib
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

global title
global body

mailInfo = {
	"from": "1049245996@qq.com", #发送方
	"to": "18722358342@163.com", #接受方
	"hostname": "smtp.qq.com",  #qq邮箱代理
	"username": "1049245996@qq.com", #用户名
	"password": "cqhfkdhpjekvbfjb", #QQ邮箱授权码，具体是开通STMP服务，发送短信即可获得授权码
	"mailencoding": "utf-8"
}

if __name__ == '__main__':

	count = len(sys.argv)	
	if count!=3:
		print("using:python sendemail + title + body")
		exit(1)

	title=sys.argv[1] #邮件标题
	body=sys.argv[2] #邮件正文

	smtp = SMTP_SSL(mailInfo["hostname"])
	smtp.set_debuglevel(1)
	smtp.ehlo(mailInfo["hostname"])
	smtp.login(mailInfo["username"],mailInfo["password"])

	msg = MIMEText(body,'html',mailInfo["mailencoding"])
	msg["Subject"] = Header(title,mailInfo["mailencoding"])
	msg["from"] = mailInfo["from"]
	msg["to"] = mailInfo["to"]
	smtp.sendmail(mailInfo["from"], mailInfo["to"], msg.as_string())

smtp.quit()
