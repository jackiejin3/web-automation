#coding=utf-8
import yagmail
from HTMLTestRunner import HTMLTestRunner
import time
import os
import unittest

def send_mail(report):
    yag = yagmail.SMTP(user="hefeng@kedacom.com", password="c92wwx8K", host="10.5.0.50")
    subject = "主题，自动化测试报告"
    contents = "正文，请查看附件"
    yag.send("16621129674@163.com", subject, contents, report)
    print("mail has send out!")

if __name__ == '__main__':
    #获取当前日期和时间
    now_time = time.strftime("%Y%m%d%H%M%S")
    report_html = os.path.dirname(os.path.abspath(".")) + '/test_report/' + now_time + '.html'

    suit = unittest.defaultTestLoader.discover("./", pattern="baidu_search1.py")
    fp = open(report_html, "wb")
    runner = HTMLTestRunner(stream=fp, title="百度测试报告", description="运行环境：win10, Chrome浏览器")
    runner.run(suit)
    fp.close()

    send_mail(report_html)
