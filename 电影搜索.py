import requests
import re
import sys
import io
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
    print(f'获取到{num}条数据')
    if num > 28:
        if type(num/28) != int:
            num = num//28+1
    elif num == 0:
        print(f'未找到"{content}"的相关数据')
        return 0
    else:
        num = 1
    return num


def get_search(content):
    num = get_search_num(content)
    if num == 0:
        exit()
    movie = list()
    for i in range(num):
        url = f'http://www.dianyinggou.com/so/{content}/page_{i+1}.html'
        html = requests.get(url, headers=headers).text
        title = etree.HTML(html).xpath('//div[@class="movies"]/a/@title')
        if title:
            movie.extend(title)
        else:
            print(f'获取"{content}"地址失败')
    play(movie)


def play(movie):
    print('--------------------')
    print('编号 --- 名称')
    for i in range(len(movie)):
        print(f'({i+1}) --- {movie[i]}')
    print('--------------------')
    while True:
        num = int(input('请输入编号:'))
        if num < len(movie)+1:
            break
        else:
            print('编号有误')
    get_web_index(movie[num-1])


def get_web_index(content):
    url = f'http://www.dianyinggou.com/Mov/movie_zy/{content}'
    html = requests.get(url, headers=headers).text
    href = etree.HTML(html).xpath('//div[@class="movieZy"]/a/@href')
    print(f'{content}有{len(href)}个播放源:')
    for i in href:
        print(i)



if __name__ == '__main__':
    content = input('请输入电影名称:')
    print('正在查询...')
    get_search(content)