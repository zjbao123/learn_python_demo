# -*- coding: UTF-8 -*-

' a  auto e-mail demo,you should comple some info about your information,then enjoy it !'
__author__ = 'zjbao123'

import mimetypes
import smtplib
from email import encoders
from email import MIMEMultipart
from email.header import Header
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText

import time

from_addr = '****@163.com'
to_addr = '****@163.com'
password = '****'
smtp_server = 'smtp.163.com'
file_name = 'test.txt'
header_info = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + u' 定时任务'
msg_info = u'每日报送任务'


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))


def send_mail(from_addr, to_addr, password, smtp_server, file_name, header_info, msg_info):
    # 邮件对象
    msg = MIMEMultipart.MIMEMultipart()
    msg['From'] = _format_addr(u'Python定时发送 <%s>' % from_addr)
    msg['To'] = _format_addr(u'你好呀 <%s>' % to_addr)
    msg['Subject'] = Header(header_info, 'utf-8').encode()
    msg.attach(MIMEText(msg_info, 'plain', 'utf-8'))

    # 增加附件
    if len(file_name) > 2:
        with open(file_name, 'rb') as f:
            # 设置附件的MIME和文件名，这里是png类型:
            mime = MIMEBase(mimetypes.guess_type(file_name)[0].split('/')[0],
                            mimetypes.guess_type(file_name)[0].split('/')[1], filename='test.txt')
            # 加上必要的头信息:
            mime.add_header('Content-Disposition', 'attachment', filename='test.txt')
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            # 把附件的内容读进来:
            mime.set_payload(f.read())
            # 用Base64编码:
            encoders.encode_base64(mime)
            # 添加到MIMEMultipart:
            msg.attach(mime)

    # 发送邮件
    server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


if __name__ == "__main__":
    try:
        send_mail(from_addr, to_addr, password, smtp_server, file_name, header_info, msg_info)
        print '发送成功'
    except Exception, e:
        print str(e)
