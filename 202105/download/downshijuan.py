import urllib.request
import ssl,sys,time
from bs4 import BeautifulSoup

def getUrl(url):
    ssl._create_default_https_context = ssl._create_unverified_context #取消验证，用于绕过https
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36"}# 设置头部用于绕过反爬
    url = 'https://www.xkb1.com/plus/search.php?typeid=179&q=&starttime=-1&channeltype=0&orderby=sortrank&pagesize=100&kwtype=1&searchtype=titlekeyword&%CB%D1%CB%F7=%CB%D1%CB%F7'
    req = urllib.request.Request(url,headers=headers)
    webContent = urllib.request.urlopen(req).read()
    return webContent.decode('gb2312')


url = 'https://www.xkb1.com/plus/search.php?typeid=179&q=&starttime=-1&channeltype=0&orderby=sortrank&pagesize=100&kwtype=1&searchtype=titlekeyword&%CB%D1%CB%F7=%CB%D1%CB%F7'
webContent = getUrl(url)
# a = BeautifulSoup(webContent).findAll('a')
soup = BeautifulSoup(webContent, 'html.parser')
# print(soup)
data = soup.find_all('a')
for i in data:
    # print(type(i))
    if "ernianjishiti" in i['href'] :
        print("good:",i['href'],i.string)
        time.sleep(20)
        download  = getUrl(i['href'])
        soup = BeautifulSoup(download, 'html.parser')
        # print(soup)
        data1 = soup.find_all('a')
        print(data1)
        sys.exit()



