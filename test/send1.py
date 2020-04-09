# ！/usr/bin/env python
# -*-coding:utf-8 -*-
import os
import time
import smtplib

from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_email(info, file_paths):
    # 发件人地址
    from_addr = 'shandongwangtian@126.com'
    # 邮箱密码
    password = 'sdwt123'
    # 收件人地址,可同时添加多个
    # openFile = open(r'F:\python_test\framfriend_Test_Project\test\mail_receiver.txt','r')
    # for line in openFile:
    #     msg1 = [i.strip() for i in line.split(',')]
    to_addrs = [
        'zlxin918@163.com',
        'chenbitty@163.com',
        'lcl7311@126.com',
        'dunianyu2008@163.com',
        'kingmeng230@163.com',
        'zhangshuyan0@163.com',
        'niethy@163.com',
        'rzf2111@vip.sina.com',
        'gebojun@126.com',
        'wulei246@163.com',
        'muziyatianli@163.com',
        'wyiju@hotmail.com ',
        'GXL1128@163.com',
        'qrsunguo@163.com',
        'chenhaibin508@163.com',
        'gyh5371@163.com',
        'kcf59502@163.com',
        'liucong33@126.com',
        'tianguangwen@126.com',
        'yxg816@163.com',
        'myzhangmei92@126.com',
        'zry6566@163.com',
        'zwj2626@sina.com',
        'zhaohuahu@126.com',
        'Huqingling2004@163.com',
        'qsdlibo@163.com',
        'mzj6613@163.com',
        'missyou_2006120@126.com',
        'qfzhm513@sina.com',
        'weishanzhou@163.com',
        'sdzhengshucun@163.com',
        'zhaokun73@sohu.com',
        'ynzxq@yahoo.com.cn',
        'zhumin@nju.edu.cn',
    ]
    # 邮箱服务器地址
    smtp_server = 'smtp.126.com'

    local_time = time.strftime('%Y-%m-%d %H:%M:%S')

    content = f'''                
        {info}
    '''
    # 设置邮件信息
    msg = MIMEMultipart()
    body = MIMEText(content.encode(), 'plain', 'utf-8')
    msg.attach(body)

    # 构造附件
    for file_name in file_paths:
        attachment = MIMEBase('application', 'octet-stream')  # 参数的意义未深究
        attachment.set_payload(open(file_name, 'rb').read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', 'attachment', filename=file_name)  # 前2个参数意义未深究
        msg.attach(attachment)

    msg['From'] = _format_addr('发件人名称 <%s>' % from_addr)
    msg['Bcc'] = _format_addr('收件人名称 <%s>' % to_addrs)
    #msg['To'] = _format_addr('收件人名称 <%s>' % to_addrs)
    msg['Subject'] = Header('关于举办“全国高校区块链原理、应用与开发高级研修班”的通知', 'utf-8').encode()

    # 发送邮件
    server = smtplib.SMTP_SSL(host=smtp_server, port=465)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addrs=to_addrs, msg=msg.as_string())

    server.quit()
if __name__ == '__main__':
    info = '''
        您好，我们是中国职业教育协会电商服务委员会，为响应政策号召，加快推动区块链技术和产业创新发展，本次我们邀请了区块链行业的一线资深专家，定于1月10日至12日，在济南举办全国高校区块链高级研修班，不知道您有没有意向参加？
具体的资料和报名回执表见附件。可电话咨询高老师17862905230（微信同号）， 邮箱：gf2502515613@dingtalk.com 董老师	13361000054(微信同号)，邮箱：dy1579382662@dingtalk.com
    '''
    file_paths = ['区块链原理、应用与开发高级研修班（1.10-1.12济南）(1).doc','区块链原理、应用与开发高级研修班（1.10-1.12济南）.pdf']
    send_email(info, file_paths)

