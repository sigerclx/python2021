#from 下载小说.searchengine.search  import Search
from lxml import etree
import time,os,sys,requests
import urllib
# https://www.shuquge.com/ 下载的小说站
class Search(object):
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
        self.htmlclass = etree.HTML(txt, etree.HTMLParser())
        return self.htmlclass

    def xpathdecode(self,htmlclass):
        # 进行html搜索返回的是class，需要转换为txt显示,这里的txt里是可能含html标签的
        txt = etree.tostring(htmlclass).decode('utf-8')

        return html.unescape(txt)

def writetxt(strmsg,filename='log.txt'): #把strmsg写入错题本
    try:
        logFile = open(filename,'a',encoding='utf-8')
        logFile.write(strmsg+'\n')
    except Exception as err:
        pass
    finally:
        logFile.close()
    return

def downtxt(zhangname,url,xiaoshuoname='all.txt'):
    txtpage = Search("www.shuquge.com")
    txt =  txtpage.geturlcontent(url)
    #print(txt)
    htmlclass = webhtml.gethtmlclass(txt)
    # print(type(htmlclass))
    # 取div中class='listman',该标签内的所有内容
    xpath = '//div[@class="showtxt"]/text()'

    hclass = htmlclass.xpath(xpath)

    #print(len(hclass))
    writetxt('\n\n'+zhangname+'\n',xiaoshuoname+'.txt')
    for i in hclass[:-3]:
        #print('hreflink=',i)
        writetxt(i.replace('    ',''),xiaoshuoname+'.txt')

# 搜索小说
xiaoshuozhan = 'https://www.shuquge.com'
webhtml = Search("www.shuquge.com")
name=input('请输入小说名称:')
zhangjie = input('请输入其实章节:')
## 获取搜索结果页面，html是搜索结果页面
html = webhtml.posturl(name)
htmlclass = webhtml.gethtmlclass(html)
xpath = '//h4[@class="bookname"]/a'
hclass = htmlclass.xpath(xpath)
if hclass:
    print('搜索小说：',hclass[0].text)
    targetUrl =xiaoshuozhan + hclass[0].attrib['href']
    print(targetUrl)
    currentUrl = targetUrl.replace('index.html','')
else:
    print('找不到对应的小说')

# 下载小说
txt =  webhtml.geturlcontent(targetUrl)
htmlclass = webhtml.gethtmlclass(txt)

# 取div中class='listman'下第一个dl下第二个dt后面同级的所有标签里的所有a标签
xpath = '//div[@class="listmain"]/dl/dt[2]/following-sibling::*//a'

hclass = htmlclass.xpath(xpath)

#当前下载页面
zhangjie = int(zhangjie)
number = 0
for i in hclass:
    number+=1
    if number < zhangjie :
        continue
    hreflink = i.attrib['href']
    #print('hreflink=',hreflink,i.text)
    zhangname = '第 '+str(number)+' 章: '+i.text.split('、')[-1]
    print(zhangname)
    url = currentUrl+hreflink
    downtxt(zhangname,url,name)




