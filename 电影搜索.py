import requests
from lxml import etree


def get_search(conntent):
    url = f'http://www.dianyinggou.com/so/{content}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 '
                             'Safari/537.36 Edg/83.0.478.54'}
    html = requests.get(url, headers=headers).text
    return etree.HTML(html).xpath('//div[@class="soResultTip"]/text()')[0]


if __name__ == '__main__':
    content = "æ÷÷–»À"
    print(get_search(content))