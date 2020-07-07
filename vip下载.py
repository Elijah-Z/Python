
from multiprocessing import Pool
import requests
 
 
 
 
class Vip(object):
 
    #构造urls
    def get_urls(self):
        url_list = []
        for i in range(1, 1600):
            i = str(i).rjust(7, '0')
            url = 'https://bilibili.com-h-bilibili.com/20191010/10062_29a5a26c/1000k/hls/deab96f2be{}.ts'.format(str(i))
            url_list.append(url)
            #print(url)
        return url_list
 
    #保存到本地
    def save(self,url,content):
        url = str(url).split('/')[-1]
        with open(r'C:\\Users\\Sparrow\\Desktop'+url, 'wb')as f:
            f.write(content)
 
    #下载并保存
    def load_video(self, url):
        response = requests.get(url)
        response.encoding = response.apparent_encoding
        print('正在下载:', url)
        self.save(url, response.content)
 
 
    #多线程下载
    def mutiply_load(self):
        print('开始下载')
        urls = self.get_urls()
        pool = Pool()
        response = pool.map(self.load_video, urls)
        pool.close()
        pool.join()
 
if __name__ == '__main__':
    vip = Vip()
    vip.mutiply_load()
    print('下载完成')