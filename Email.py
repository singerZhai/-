# coding:utf-8
import os, sys
import smtplib
import time
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

reportPath = os.path.join(os.getcwd(), 'Report')  # 测试报告的路径


class SendMail(object):
    def __init__(self, receiver=None):
        """接收邮件的人：list or tuple"""
        if receiver is None:
            self.sendTo = ['singer_zhai@163.com']  # 收件人这个参数，可以是list，或者tulp，以便发送给多人
        else:
            self.sendTo = receiver

    @staticmethod
    def get_report():  # 该函数的作用是为了在测试报告的路径下找到最新的测试报告
        dirs = os.listdir(reportPath)
        dirs.sort()
        new_report_name = dirs[-1]
        # print('The new report name: {0}'.format(new_report_name))
        return new_report_name  # 返回的是测试报告的名字

    def take_messages(self):  # 该函数的目的是为了 准备发送邮件的的消息内容
        new_report_name = self.get_report()
        self.msg = MIMEMultipart()
        self.msg['Subject'] = 'TestReport'  # 邮件的标题
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        with open(os.path.join(reportPath, new_report_name), 'rb') as f:
            mail_body = f.read()  # 读取测试报告的内容
        html = MIMEText(mail_body, _subtype='html', _charset='utf-8')  # 将测试报告的内容放在 邮件的正文当中
        self.msg.attach(html)  # 将html附加在msg里

        # html附件    下面是将测试报告放在附件中发送
        att1 = MIMEText(mail_body, 'base64', 'gb2312')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="TestReport.html"'  # 这里的filename可以任意写，写什么名字，附件的名字就是什么
        self.msg.attach(att1)

    def send(self):
        self.take_messages()
        self.msg['from'] = 'singer_zhai@163.com'  # 发送邮件的人
        self.msg['to'] = 'singer_zhai@163.com'     # 收件人和发送人必须这里定义一下，执行才不会报错。
        smtp = smtplib.SMTP()
        smtp.connect('smtp.163.com')
        smtp.login('singer_zhai@163.com', 'ZHD951029')  # 登录的用户名和密码（注意密码是设置客户端授权码，因为使用用户密码不稳听，有时无法认证成功，导致登录不上，故无法发送邮件。）
        smtp.sendmail(self.msg['from'], self.msg['to'], self.msg.as_string())  # 发送邮件
        smtp.close()
        print('sendmail success')


if __name__ == '__main__':
    sendMail = SendMail()
    sendMail.send()
