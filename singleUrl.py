import urllib.request
from bs4 import BeautifulSoup
import os
import requests


testUrl = 'https://www.g456p.com'
appendUrl = '/pic/toupai/'

opener = urllib.request.build_opener()
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0(Windows NT 6.1; WOW64) AppleWebKit/5377.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

file_path = 'img/total'


def getHtmlText(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            r.encoding = r.apparent_encoding
            return r.text
    except requests.exceptions.RequestException:
        return None


def getItem(url):
    arr = []
    bs_obj = BeautifulSoup(url, 'html.parser')
    tag = bs_obj.find_all(name='a')
    for item in tag:
        value = item.get('href')
        if value[-4:] == 'html':
            # print(testUrl+value)
            # print(item.get_text() + ':' + value)
        # text = item.get_text()
        # 这里只是找到 html 结尾的链接 防止出错
        # arr.append(openUrl+value)
        # if value[0:6] == '/view/':
            # print(item.get_text())
            arr.append(testUrl+value)
    return arr


def getImage(text, path):
    bs_obj = BeautifulSoup(text, 'html.parser')
    tag = bs_obj.find_all('img')
    for item in tag:
        value = item.get('src')
        if value:
            # 这是为了找到jpg 结尾的
            if value[-3:] == 'jpg':
                # 给文件起名字
                fileName = '{}{}{}{}'.format(
                    path, os.sep, value[-15:], '.jpg')
                # 存到对应路径下
                urllib.request.urlretrieve(value, filename=fileName)


for i in range(3, 10):
    print(testUrl+appendUrl+'index_'+str(i)+'.html')
    text = getHtmlText(testUrl+appendUrl+'index_'+str(i)+'.html')
    # arr = []
    arr = getItem(text)
    # formatArr2 = []
    formatArr2 = list(set(arr))
    for j in range(len(formatArr2)):
      
        midUrl = getHtmlText(formatArr2[j])
        arr2 = getItem(midUrl)
        formatArr3 = list(set(arr2))
        for k in range(len(formatArr3)):
            print(formatArr3[k])
            midUrl2 = getHtmlText(formatArr3[k])
            # if not os.path.exists(file_path):
            #     os.makedirs(file_path)
            # getImage(midUrl2,file_path)
    #     print(formatArr2[j])
        # getImage(midUrl, file_path)
# text = getHtmlText(testUrl+appendUrl)


# for i in range(len(formatArr2)):
    # print(formatArr2[i])
    # midUrl = getHtmlText(formatArr2[i])
    # if not os.path.exists(file_path):
    #     os.makedirs(file_path)
    # getImage(midUrl, file_path)


