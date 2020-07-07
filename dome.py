import os
import requests
import smtplib
import socket
import uuid
from email.mime.text import MIMEText
from lxml import etree


def get_web_ip(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 '
                             'Safari/537.36 Edg/83.0.478.54'}
    return requests.get(url, headers=headers).text


def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0, 11, 2)])


def mail():
    message = MIMEText(open(path, 'r').read(), 'plain', 'utf-8')
    os.remove(path)
    message['From'] = "{}".format('s1241340102@163.com')
    message['To'] = ",".join(['1241340102@qq.com'])
    message['Subject'] = 'From IP Address'

    try:
        smtpObj = smtplib.SMTP_SSL("smtp.163.com", 465)  # 启用SSL发信, 端口465
        smtpObj.login('s1241340102@163.com', 'LFOYJCTNXQWUMGRH')
        smtpObj.sendmail('s1241340102@163.com', ['1241340102@qq.com'], message.as_string())
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)


if __name__ == '__main__':
    path = 'C:/temp.txt'
    url = 'https://ip.cn/'
    html = etree.HTML(get_web_ip(url))
    pc_host = socket.getfqdn(socket.gethostname())
    pc_addr = socket.gethostbyname(pc_host)
    title = ["Internet Address:", "Location:", "GeoIP:", "Computer Name:", "LAN Address:", "MAC Address:"]
    information = html.xpath('//div[@class="well"]/p/code/text()')
    information.extend([pc_host, pc_addr, get_mac_address()])
    for i, j in zip(title, information):
        open(path, 'a').write('{}\n'.format(str(i) + "\t" + str(j)))
    mail()