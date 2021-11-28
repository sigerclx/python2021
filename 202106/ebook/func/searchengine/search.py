import json
import requests,time
from lxml import etree
import html,random
class Search(object):
    def __init__(self):

        # 用requests进行请求搜索,定义header
        self.headers = {
            "User-Agent":"Mozilla/4.1 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
            "Referer": "https://cn.bing.com/"
        }

    def setengine(self,engine,enginekey):
        self.headers["Referer"] = engine
        self.search =enginekey # r'https://cn.bing.com/search?q='

    def geturlcontent(self, url):
        # 获得url页面的txt
        self.randomHeaders()
        response = requests.get(url, headers=self.headers)
        self.htmltext = response.text
        return self.htmltext

    def searchword(self, searchword):
        # 获得url页面的txt
        initurl = self.search + searchword
        self.randomHeaders()
        response = requests.get(initurl, headers=self.headers)
        self.htmltext = response.text
        return self.htmltext

    def randomHeaders(self):
        num =str(random.randint(10000, 90000))
        Referer = self.headers["Referer"] + num
        #print(Referer)
        self.headers['Referer'] = Referer
        self.headers['User-Agent'] = "Mozilla/4."+num+" (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537."+num
        # seconds = random.randint(3500, 5000)
        # time.sleep(seconds/1000.0)

    def gethtmlclass(self,txt):
        # 将页面的txt转换为类，已备进行html标签化搜索
        self.htmlclass = etree.HTML(txt, etree.HTMLParser())
        return self.htmlclass

    def xpathdecode(self,htmlclass):
        # 进行html搜索返回的是class，需要转换为txt显示,这里的txt里是可能含html标签的
        txt = etree.tostring(htmlclass).decode('utf-8')

        return html.unescape(txt)


class Wys(Search):
    def __init__(self):
        Search.__init__(self)
        # 定位百度汉语的成语解释的div的class下面的span
        Search.setengine(self,r"https://mp.weixin.qq.com/",r"https://mp.weixin.qq.com/")

    def getmoudle(self,url,startnum):

        txt = Search.geturlcontent(self,url)
        htmlclass1= Search.gethtmlclass(self,txt)
        #print(txt)
        # 搜索MP3
        mp3url = 'https://res.wx.qq.com/voice/getvoice?mediaid='
        xpath = '//*[@class="js_editor_audio audio_iframe js_uneditable custom_select_card"]/@name'
        hclass1 = htmlclass1.xpath(xpath)
        mp3num =len(hclass1)
        #print(hclass)

        xpath = '//*[@class="js_editor_audio audio_iframe js_uneditable custom_select_card"]/@voice_encode_fileid'
        hclass2 = htmlclass1.xpath(xpath)
        #print(hclass)
        for k in range(mp3num):
            url = mp3url +  hclass2[k]
            self.downloadfile(url, hclass1[k])

        #下载课文
        xpath = '//*[@class="rich_pages" and @data-s="300,640"]/@data-src'
        hclass = htmlclass1.xpath(xpath)
        imgs = len(hclass)
        for i in range(0,imgs-1):
            print(hclass[i])
            filename = str(i+startnum)+'.jpg'
            self.downloadfile(hclass[i],filename)





    def downloadfile(self,url, filename):
        # print(filename,url)
        res = ''
        try:
            # res =requests.get(url,headers=headers)
            res = requests.get(url)
            if not res:
                return
        except Exception as err:
            print("downloadfile 发现错误了：" + str(err))
            return

        downloadFile = open(filename.lower(), 'wb')
        for chunk in res.iter_content(20000):
            downloadFile.write(chunk)
        downloadFile.close()
        print(filename,' is downloaded !')



