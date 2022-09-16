import urllib.request
from bs4 import BeautifulSoup
import os
import requests
openUrl = 'https://www.g456p.com'

opener = urllib.request.build_opener()
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0(Windows NT 6.1; WOW64) AppleWebKit/5377.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

file_path = 'yellow'


def getHtmlText(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            r.encoding = r.apparent_encoding
            return r.text
    except requests.exceptions.RequestException:
        return None

#


def getItem(url):
    arr = []
    bs_obj = BeautifulSoup(url, 'html.parser')
    tag = bs_obj.find_all(name='a')
    for item in tag:
        value = item.get('href')
        if value[0:4] == '/pic':
            print(openUrl+value)
        # print(item.get_text() + ':' + value)
        # text = item.get_text()
        # 这里只是找到 html 结尾的链接 防止出错
        # arr.append(openUrl+value)
        # if value[0:6] == '/view/':
            arr.append(openUrl+value)
    return arr


def getOption(url):
    arr = []
    bs_obj = BeautifulSoup(url, 'html.parser')
    tag = bs_obj.find_all(name='option')
    for item in tag:
        value = item.get('value')
        if value[0:4] == '/pic':
            print(openUrl+value)
        # print(item.get_text() + ':' + value)
        # text = item.get_text()
        # 这里只是找到 html 结尾的链接 防止出错
        # arr.append(openUrl+value)
        # if value[0:6] == '/view/':
            arr.append(openUrl+value)
    return arr
# 通过网页解析 将img 标签的图片存到对应的文件夹下


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


text = getHtmlText(openUrl)
arr2 = getItem(text)
formatArr2 = list(set(arr2))
# for i in range(len(formatArr2)):
#     midUrl = getHtmlText(arr2[i])
#     if not os.path.exists(file_path):
#         os.makedirs(file_path)
#     getImage(midUrl, file_path)

# 打印链接：
for i in range(len(formatArr2)):
    midUrl = getHtmlText(formatArr2[i])
    midArr = getOption(midUrl)
    for j in range(len(midArr)):
        print(midArr[j])
