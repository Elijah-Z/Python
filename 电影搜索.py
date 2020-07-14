import requests
import re
import sys
import io
import webbrowser
import random
from lxml import etree


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106'
                         'Safari/537.36 Edg/83.0.478.54'}
# 改变标准输出的默认编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')


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
            if num > date_num or num < 1:
                print('编号有误')
                continue
            else:
                get_web_index(movie[num - 1], search)
                break


def get_web_index(content, search):
    url = f'http://www.dianyinggou.com/Mov/movie_zy/{content}'
    html = requests.get(url, headers=headers).text
    href = etree.HTML(html).xpath('//div[@class="movieZy"]/a/@href')
    source = etree.HTML(html).xpath('//ul/li[2]/text()')
    if search == 2:
        rd = random.randint(1, len(href))
        webbrowser.open(href[rd])
        print(f'正在播放:{content} --- {source[rd - 1]}')
    else:
        print(f'获取到"{content}"有{len(href)}个播放源:')
        print('--------------------')
        print('编号 --- 播放源')
        for i in range(len(source)):
            print(f'({i+1}) --- {source[i]}')
        print('--------------------')
        print('持续检索,返回查找键入0')
        while True:
            num = int(input('请输入播放源编号:'))
            if num > len(source) or num < 1 and num != 0:
                print('编号有误')
                continue
            elif num == 0:
                print('')
                break
            else:
                webbrowser.open(href[num - 1])
                print(f'正在播放:{content} --- {source[num - 1]}')
                continue


def main():
    while True:
        search = int(input('精确查找(1)/快速检索(2):'))
        if search == 1:
            print('精确查找')
            break
        elif search == 2:
            print('快速检索')
            break
        else:
            print('输入有误,请键入1/2')
            continue
    while True:
        content = input('请输入影视名称:')
        if content == 'exit' or content == 'quit':
            exit()
        elif content == 'back':
            main()
        else:
            get_search(content, search)


if __name__ == '__main__':
    main()

