import requests,time
from lxml import etree
import html,random
class Search(object):
    def __init__(self):

        # 用requests进行请求搜索,定义header
        self.headers = {
            "User-Agent":"Mozilla/4.1 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
        }

    def set_referer(self,referer):
        self.headers["Referer"] = referer

    def geturlcontent(self,url,encoding='utf-8'):
        # 获得url页面的txt
        self.randomHeaders()
        response = requests.get(url, headers=self.headers)
        response.encoding = encoding
        self.htmltext = response.text
        return self.htmltext

    def randomHeaders(self):
        num =str(random.randint(10000, 90000))
        Referer = self.headers["Referer"] + num
        self.headers['Referer'] = Referer
        self.headers['User-Agent'] = "Mozilla/4."+num+" (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537."+num

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


class Ttjj_namelist(Search):
    def __init__(self):
        Search.__init__(self)
        self.url = 'http://fund.eastmoney.com/js/fundcode_search.js'
        Search.set_referer(self, 'http://fund.eastmoney.com/')

    def get_nolist(self):
        nolist = Search.geturlcontent(self,self.url).replace('var r = ','').replace(';', '')
        # nolist = nolist.replace('U+FEFF','')
        # 去除文件中的不可打印字符U+FEFF
        f = open(r'data\base\nolist.txt', 'w', encoding='UTF-8')
        f.write(nolist)
        f = open(r'data\base\nolist.txt', 'r', encoding='UTF-8-sig')
        txt = f.read()
        f.close()
        # 返回基金list数组
        return eval(txt)






