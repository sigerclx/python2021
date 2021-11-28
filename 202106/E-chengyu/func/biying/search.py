import json
import requests,time
from lxml import etree
import html,random
class Search(object):
    def __init__(self):

        # 用requests进行请求搜索,定义header
        self.headers = {
            "User-Agent":"Mozilla/4.1 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
            "Referer": "https://cn.bing.com/",
            "sec-ch-ua": '"Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91""'
        }

    def geturlcontent(self,searchword):
        # 获得url页面的txt
        initurl = r'https://cn.bing.com/search?q='+searchword
        self.randomHeaders()
        response = requests.get(initurl, headers=self.headers)
        self.htmltext = response.text
        return self.htmltext

    def randomHeaders(self):
        num =str(random.randint(10000, 90000))
        Referer = "https://www.baidu.com/" + num
        #print(Referer)
        self.headers['Referer'] = Referer
        self.headers['User-Agent'] = "Mozilla/4."+num+" (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537."+num
        # seconds = random.randint(3500, 5000)
        # time.sleep(seconds/1000.0)

    def gethtmlclass(self):
        # 将页面的txt转换为类，已备进行html标签化搜索
        self.htmlclass = etree.HTML(self.htmltext, etree.HTMLParser())
        return self.htmlclass

    def chengyuhanyi(self):
        hclass = self.htmlclass.xpath('//*[@class="rwrl rwrl_pri rwrl_padref"]')

        txt = self.xpathdecode(hclass)
        txt = txt.replace('<span>','').replace('</span>','').strip()
        return txt

    def xpathdecode(self,htmlclass):
        # 进行html搜索返回的是class，需要转换为txt显示,这里的txt里是可能含html标签的
        txt = etree.tostring(htmlclass[0]).decode('utf-8')

        return html.unescape(txt)


class Chengyuhanyi(Search):
    def __init__(self):
        Search.__init__(self)
        # 定位百度汉语的成语解释的div的class下面的span
        self.xpath1 = '//*[@class="rwrl rwrl_pri rwrl_padref"]'
        self.xpath2 = '//*[@class="rwrl rwrl_sec rwrl_padref"]'
        self.searchhouzhui = '的意思'

    def getmean(self,word):
        Search.geturlcontent(self,word+self.searchhouzhui)
        htmlclass= Search.gethtmlclass(self)
        hclass = htmlclass[0].xpath(self.xpath1)
        if not hclass:
            hclass = htmlclass[0].xpath(self.xpath2)
        #print(hclass,len(hclass))
        if hclass :
            txt = Search.xpathdecode(self, hclass)
            # --- 去除文本格式中所有的html标签 ---
            txt = etree.HTML(text=txt)
            txt =txt.xpath('string(.)').strip()
            #-----------------------------------
            return txt
        else:
            return


