#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 19:01
# @Author  : Wei Lu
# @File    : 51kanong-spider.py
import requests
from lxml import etree
from fake_useragent import UserAgent

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import datetime
headers  = {
    'User-Agent':UserAgent().random
}


def load_data_dean():
    url = 'https://www.51kanong.com/plugin.php?id=xiaoyu_mi&t=l'
    response=requests.get(url=url,headers=headers).text
    html=etree.HTML(response)
    post_name1=html.xpath('//a[@class="t_name"]/text()')
    post_time1=html.xpath('//span[@class="time txt"]/text()')
    return post_name1,post_time1


def load_data_forum():
    post_time2=[]
    post_name2=[]
    for i in range(1,21):
        url = 'https://www.51kanong.com/forum.php?mod=forumdisplay&fid=140&orderby=lastpost&orderby=lastpost&filter=lastpost&page=' + str(i)
        response = requests.get(url=url, headers=headers).text
        html = etree.HTML(response)
        post_name2 += (html.xpath('//a[@class="deanforumtitname"]/text()'))
        post_time2 += (html.xpath('//div[@class="deanforump5"]/a/text()'))
    return post_name2,post_time2

def load_data_tech():
    url = 'https://www.51kanong.com/forum.php?mod=forumdisplay&fid=120&filter=lastpost&orderby=lastpost'
    response = requests.get(url=url, headers=headers).text
    html = etree.HTML(response)
    post_name3=html.xpath('//a[@class="deanforumtitname"]/text()')
    post_time3=html.xpath('//div[@class="deanforump5"]/a/text()')
    return post_name3,post_time3

def data_all():
    post_name=load_data_dean()[0]+load_data_forum()[0]+load_data_tech()[0]
    post_time=load_data_dean()[1]+load_data_forum()[1]+load_data_tech()[1]


def send_mail(post_name,post_time):
    mail_host = "smtp.quantum1tech.com"
    mail_user = "jiank@quantum1tech.com"
    mail_pass = "Hello1234"

    sender = 'jiank@quantum1tech.com'
    receivers = ['xiongge@quantum1tech.com']

    message = MIMEText('卡农论坛预警，论坛上有人在搜：'+ post_name + post_time, 'plain', 'utf-8')
    message['From'] = Header("卡农论坛预警！", 'utf-8')
    message['To'] = Header("卡农论坛预警！", 'utf-8')

    subject = '卡农论坛预警！'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

if __name__ == '__main__':
    check_list = ['花分期', '花猪', '51花', '小白钱包', '花无极', '微现金']
    white_list = ['趣花分期']
    post_name = load_data_dean()[0] + load_data_forum()[0] + load_data_tech()[0]
    post_time = load_data_dean()[1] + load_data_forum()[1] + load_data_tech()[1]
    for i in range(len(post_name)):
        for j in check_list:
            for k in white_list:
                if((datetime.datetime.now() - datetime.datetime.strptime(post_time[i], "%Y-%m-%d %H:%M")).seconds) <=3600 and (j in post_name[i]) and (k not in post_name[i]):
                    print(post_name[i])
                    print(post_time[i])
                    send_mail(post_name[i],post_time[i])


