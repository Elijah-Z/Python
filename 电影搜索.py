# encoding:utf-8
import requests
import re
import sys
import io
import webbrowser
import random
from lxml import etree

analy = {
        '思古解析': 'http://api.bbbbbb.me/jx/?url=',
        '视频解析': 'http://jx.598110.com/?url=',
        'vip视频解析': 'http://api.sumingys.com/index.php?url=',
        '那片云解析': 'http://api.nepian.com/ckparse/?url=',
        '石头云': 'http://jiexi.071811.cc/jx.php?url=',
        '人人解析': 'https://vip.mpos.ren/v/?url=',
        'wlzhan解析': 'http://api.wlzhan.com/sudu/?url=',
        '金桥解析': 'http://jqaaa.com/jx.php?url=',
        'Lequgirl': 'http://api.lequgirl.com/?url=',
        '通用视频': 'http://jx.598110.com/index.php?url=',
        '百域阁': 'http://app.baiyug.cn:2019/vip/index.php?url=',
        '会员K云': 'http://17kyun.com/api.php?url=',
        '高端解析': 'http://api.hlglwl.com/jx.php?url=',
        '鑫梦解析': 'http://api.52xmw.com/?url=',
        '618G解析': 'https://jx.618g.com/?url=',
        'OK视频': 'http://okjx.cc/?url='
    }
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106'
                         'Safari/537.36 Edg/83.0.478.54'}
# 改变标准输出的默认编码
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')


def get_redirect_url(url):
    response = requests.get(url, headers=headers)
    return response.url


def get_search_num(content):
    numurl = f'http://www.dianyinggou.com/so/{content}'
    html = requests.get(numurl, headers=headers).text
    num = int(re.findall('共找到(.*?)条', html)[0])
    data_num = num
    if num > 28:
        if type(num/28) != int:
            num = num//28+1
    elif num == 0:
        print(f'未找到"{content}"的相关数据')
        return 0, 0
    else:
        num = 1
    return num, data_num


def get_search(content, search):
    num, data_num = get_search_num(content)
    if num != 0:
        movie = list()
        for i in range(num):
            url = f'http://www.dianyinggou.com/so/{content}/page_{i+1}.html'
            html = requests.get(url, headers=headers).text
            title = etree.HTML(html).xpath('//div[@class="movies"]/a/@title')
            movie.extend(title)
        play(movie, data_num, search)


def play(movie, date_num, search):
    if search == 2:
        get_web_index(movie[random.randint(1, date_num) - 1], search)
    else:
        print(f'获取到{date_num}条数据')
        print('--------------------')
        print('编号 --- 名称')
        for i in range(len(movie)):
            print(f'({i+1}) --- {movie[i]}')
        print('--------------------')
        while True:
            num = int(input('请输入编号:'))
            if num > date_num or num < 1 and num != 0:
                print('输入有误,请键入编号')
                continue
            elif num == 0:
                main()
            else:
                get_web_index(movie[int(num) - 1], search)
                break


def get_web_index(content, search):
    url = f'http://www.dianyinggou.com/Mov/movie_zy/{content}'
    html = requests.get(url, headers=headers).text
    href = etree.HTML(html).xpath('//div[@class="movieZy"]/a/@href')
    source = etree.HTML(html).xpath('//ul/li[2]/text()')
    rd = random.randint(1, len(href))
    if search == 2:
        if source[rd - 1] == '爱奇艺' or source[rd - 1] == '腾讯视频':
            index = random.randint(0, len(list(analy.values())) - 1)
            name = list(analy.keys())[index]
            print(f'正在播放:<<{content}>> --- {source[rd - 1]} --- {name}')
            webbrowser.open(list(analy.values())[index] + get_redirect_url(href[rd - 1]))
        else:
            print(f'正在播放:<<{content}>> --- {source[rd - 1]}')
            webbrowser.open(href[rd - 1])
    else:
        print(f'获取到"{content}"有{len(href)}个播放源:')
        print('--------------------')
        print('编号 --- 播放源')
        for i in range(len(source)):
            print(f'({i+1}) --- {source[i]}')
        print('--------------------')
        while True:
            num = int(input('请输入播放源编号:'))
            if num > len(source) or num < 1 and num != 0:
                print('输入有误,请键入播放源编号')
                continue
            elif num == 0:
                break
            else:
                if source[num - 1] == '爱奇艺' or source[num - 1] == '腾讯视频':
                    index = random.randint(0, len(list(analy.values())) - 1)
                    name = list(analy.keys())[index]
                    print(f'正在播放:<<{content}>> --- {source[num - 1]} --- {name}')
                    webbrowser.open(list(analy.values())[index] + get_redirect_url(href[num - 1]))
                else:
                    print(f'正在播放:<<{content}>> --- {source[num - 1]}')
                    webbrowser.open(href[num - 1])
                continue


def go(search):
    while True:
        content = input('请输入影视名称:')
        if content == '0':
            main()
        else:
            get_search(content, search)


def main():
    print('--- 全网影视查询 ---')
    while True:
        search = input('(1) --- 精确查找\n(2) --- 快速播放\n(3) --- 帮助\n选择查找模式:')
        if search == '1':
            print('精确查找')
            break
        elif search == '2':
            print('快速播放')
            break
        elif search == '0':
            exit()
        elif search == '3':
            print('--------------------')
            print('1. 精确查找:')
            print('\t输入名称 -> 选择影视 -> 选择线路 -> 播放')
            print('2. 快速播放:')
            print('\t输入名称 -> 播放')
            print('\n注:爱奇艺或腾讯视频会经过vip解析播放')
            print('--------------------')
        else:
            print('输入有误,请键入编号')
    go(int(search))



if __name__ == '__main__':
    main()

