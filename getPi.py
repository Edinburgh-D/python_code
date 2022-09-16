# coding UTF-8
import urllib.request
from bs4 import BeautifulSoup
import os
import requests
# 网站
# url = "https://www.xituge.cc/57485.html"
url = "https://www.d234r.com/pic/meitui/"
# print(res.text)
# 构造请求为浏览器访问防止无法访问
opener = urllib.request.build_opener()
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0(Windows NT 6.1; WOW64) AppleWebKit/5377.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)
# 相对路径  文件夹名称
file_path = 'bigImage'

# 获取目标网站的html 代码信息
def getHtmlText(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            r.encoding = r.apparent_encoding
            return r.text
    except requests.exceptions.RequestException:
        return None

# 通过解析 html 找到所有含有超链接的标签  拿到超链接 全部放入数组里
def getItem(url):
    arr = []
    bs_obj = BeautifulSoup(url, 'html.parser')
    tag = bs_obj.find_all('a')
    for item in tag:
        value = item.get('href')
        # 这里只是找到 html 结尾的链接 防止出错
        if value[-4:] == 'html':
            arr.append(value)
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
                    #存到对应路径下
                urllib.request.urlretrieve(value, filename=fileName)
# 这里是看到网页的链接如果要分页的话直接在url 后面加数字 所有就遍历了数字 2-10
for i in  range(2,10):
    tegUrl = url + str(i)
    text = getHtmlText(tegUrl)
    arr2 = getItem(text)
    #这里为为了去重
    formatArr2 = list(set(arr2))
#开始获取了
    for i in range(len(formatArr2)):
        midUrl = getHtmlText(arr2[i])

        if not os.path.exists(file_path):
            os.makedirs(file_path)

        getImage(midUrl, file_path)
