import time,sys,requests
from lxml import etree
#from lxml import html
import urllib
# 通用的下载基类
class Htmlquery(object):
    def __init__(self,engine):

        # 用requests进行请求搜索,定义header
        self.headers = {
            "User-Agent":"Mozilla/4.1 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
        }
        self.headers["Referer"] = engine

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

    def posturl(self,searchkey= '弃宇宙'):
        url = "https://www.shuquge.com/search.php"
        data = {"s": "6445266503022880974", "searchkey": ""}
        data['searchkey'] = searchkey
        attempts = 0
        time1 = 0
        success = False
        htmlbody = '获取失败'
        while attempts < 3600 and not success:
            try:
                res = requests.post(url=url, data=data,timeout=(5,10))
                res.encoding = 'utf-8'
                success = True
                htmlbody = res.text
            except Exception as err:
                attempts += 1
                time1 += 2
                success = False
                print('尝试次数：', attempts, err)
                print('休眠：', str(time1))

                time.sleep(time1)
                if attempts == 3600:
                    print('尝试次数过多：', attempts, '退出')
                    sys.exit(0)

        return htmlbody

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
        #etree = html.etree
        self.htmlclass = etree.HTML(txt, etree.HTMLParser())
        return self.htmlclass

    def xpathdecode(self,htmlclass):
        # 进行html搜索返回的是class，需要转换为txt显示,这里的txt里是可能含html标签的
        txt = etree.tostring(htmlclass).decode('utf-8')

        return html.unescape(txt)