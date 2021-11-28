import json
import requests,time,sys
from lxml import etree
import html,random
class Search(object):
    def __init__(self):

        # 用requests进行请求搜索,定义header
        self.headers = {
            "User-Agent":"Mozilla/4.1 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
            "Referer": "https://drive.my-elibrary.com"
        }

    def setengine(self,engine,enginekey):
        self.headers["Referer"] = engine
        self.search =enginekey # r'https://cn.bing.com/search?q='

    def geturlcontent(self, url):
        # 获得url页面的txt
        #self.randomHeaders()
        attempts=0
        time1 =0
        success =False
        s = requests.session()
        s.keep_alive = False
        #s.adapters(max_retries=3)
        self.htmltext = '获取失败'
        while attempts <3600 and not success:
            try:
                response = s.get(url, headers=self.headers,timeout=(5,10))
                success = True
                self.htmltext = str(response.content, 'utf-8')

            except Exception as err:
                attempts +=1
                time1 +=2
                success = False
                print('尝试次数：', attempts,err)
                print('休眠：', str(time1))

                time.sleep(time1)
                if attempts ==3600 :
                    print('尝试次数过多：',attempts,'退出')
                    sys.exit(0)

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
        txt = etree.tostring(htmlclass[0]).decode('utf-8')

        return html.unescape(txt)


class Waiyansheweixin(Search):
    def __init__(self):
        Search.__init__(self)
        # 定位百度汉语的成语解释的div的class下面的span
        self.xpath2 = '//td[@style="margin: 0px;padding: 5px 10px;word-break: break-all;border-color: rgb(221, 221, 221);border-style: solid;border-width: 1px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"]/section/a/span/text()'
        self.xpath1 = '//td[@style="margin: 0px;padding: 5px 10px;word-break: break-all;border-color: rgb(221, 221, 221);border-style: solid;border-width: 1px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"]/section/a/@href'

        Search.setengine(self,r"http://mp.weixin.qq.com",r"http://mp.weixin.qq.com")


    def getTargetclass(self):
        txt = Search.geturlcontent(self,'https://mp.weixin.qq.com/s/Wj1RowB1H0TQwQ0JQY4IjA')

        htmlclass= Search.gethtmlclass(self,txt)
        xpath1 = '//div[@class="rich_media_content "]//section[2]/section/*'
        hclass = htmlclass.xpath(xpath1)
        restxt = Search.xpathdecode(self,hclass)
        print(len(restxt),restxt)
        if hclass :
            print(len(hclass))
        else:
            print('no')

    def getclass(self):
        txt = Search.geturlcontent(self,'https://mp.weixin.qq.com/s/Wj1RowB1H0TQwQ0JQY4IjA')
        htmlclass= Search.gethtmlclass(self,txt)
        hclass = htmlclass[0].xpath(self.xpath1)
        print(hclass)
        hclass1 = htmlclass[0].xpath(self.xpath2)
        print(hclass1)
        #restxt = Search.xpathdecode(self,hclass)
        #print(len(restxt),restxt)
        if hclass :
            print(len(hclass))
        else:
            print('no')




