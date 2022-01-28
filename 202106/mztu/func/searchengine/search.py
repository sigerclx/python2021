import requests,os
from lxml import etree
import html,random,time,sys
class Search(object):
    def __init__(self):

        # 用requests进行请求搜索,定义header
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4324.104 Safari/537.36",
            "cookie":"Hm_lvt_768a5f0e1e2da152800f053cec2f560a = 1625309322, 1625317074;Hm_lpvt_768a5f0e1e2da152800f053cec2f560a = 1625317084"
        }
        requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数

    def setengine(self,engine,enginekey):
        self.headers["Referer"] = engine
        self.search =enginekey # r'https://cn.bing.com/search?q='

    def geturlcontent(self,url,encoding='utf-8'):
        # 获得url页面的txt
        #self.randomHeaders()
        self.headers["Referer"] = r'https://p.iimzt.com'
        attempts = 0
        time1 = 0
        success = False
        s = requests.session()
        s.keep_alive = False
        # s.adapters(max_retries=3)
        self.htmltext = '获取失败'
        while attempts < 3600 and not success:
            try:
                response = s.get(url, headers=self.headers, timeout=(5, 10))
                success = True
                self.htmltext = str(response.content, 'utf-8')

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

        return self.htmltext

    def randomHeaders(self):
        num =str(random.randint(10000, 90000))
        #Referer = self.headers["Referer"] + num
        #print(Referer)
        #self.headers['Referer'] = Referer
        #self.headers['User-Agent'] = "Mozilla/4."+num+" (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537."+num
        self.headers['Referrer Policy'] = "strict-origin-when-cross-origin"

        # seconds = random.randint(3500, 5000)
        # time.sleep(seconds/1000.0)

    def gethtmlclass(self,txt=""):
        # 将页面的txt转换为类，已备进行html标签化搜索
        if txt:
            self.htmlclass = etree.HTML(txt, etree.HTMLParser())
        else:
            self.htmlclass = etree.HTML(self.htmltext, etree.HTMLParser())
        return self.htmlclass

    def xpathdecode(self,htmlclass):
        # 进行html搜索返回的是class，需要转换为txt显示,这里的txt里是可能含html标签的
        txt = etree.tostring(htmlclass[0]).decode('utf-8')
        return html.unescape(txt)

    def removehtmltag(self,htmltxt):
        # --- 去除文本格式中所有的html标签 ---
        txt = etree.HTML(text=htmltxt)
        txt = txt.xpath('string(.)').strip()
        # -----------------------------------
        return  txt


class Mzt(Search):
    def __init__(self):
        Search.__init__(self)
        #self.url = 'https://mmzztt.com/photo/31198'
        self.xpath1 = "//table[@class='dbtable']"

        #txt = Search.geturlcontent(self, url, encoding='utf-8')

    def xpathdecode(self,htmlclass):
        # 进行html搜索返回的是class，需要转换为txt显示,这里的txt里是可能含html标签的
        txt = etree.tostring(htmlclass[0]).decode('utf-8')
        return html.unescape(txt)

    def getphotosurl(self,url):
        txt = Search.geturlcontent(self, url, encoding='utf-8')
        htmlclass = Search.gethtmlclass(self,txt)
        #xpath ="//div[@class='uk-grid uk-grid-match uk-child-width-1-3@m uk-child-width-1-2@s g-list']//a/@href"
        xpath = "//h2[@class='uk-card-title uk-margin-small-top uk-margin-remove-bottom']//a/@href"
        jpgurl = htmlclass.xpath(xpath)
        xpath1 = "//div[@class='uk-card-badge uk-label u-label']/text()"
        jpgnum = htmlclass.xpath(xpath1)
        return jpgurl,jpgnum

    def getJpgurl(self,url):
        txt = Search.geturlcontent(self, url,encoding='utf-8')
        htmlclass = Search.gethtmlclass(self,txt)
        xpath = "//img[@referrerpolicy='origin']/@src"
        jpgurl = htmlclass.xpath(xpath)
        return jpgurl[0]

    def download(self,imgUrl,filename):
        self.headers["Referer"] =r'https://p.iimzt.com'
        s = requests.session()
        s.keep_alive = False  # 关闭多余连接
        # 下载并写入本地文件，同时把下载地址和图片地址写入日志
        if os.path.exists(filename):
            return 0
        try:
            res = requests.get(imgUrl, headers=self.headers,timeout=3)
            #print(len(res.text))
            #print(res.text)
            if len(res.text)<1000:
                return 0
            downloadFile = open(filename, 'wb')
            for chunk in res.iter_content(100000):
                downloadFile.write(chunk)
            downloadFile.close()
            print(filename,'成功保存图片')
            return 1
        except:
            print(filename,'下载失败')
            return 0

    def create_folder(dest_path):
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)



