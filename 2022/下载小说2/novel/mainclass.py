from searchengine.urldownload  import Htmlquery
from multiprocessing import Process
from searchengine.urldownload  import Htmlquery
import os

class Procedure(object):
    def __init__(self):
        self.xiaoshuozhan = 'https://www.shuquge.com'
        self.webhtml = Htmlquery("www.shuquge.com")


    def search_novel(self):
        # 搜索小说
        self.name = input('请输入小说名称:')
        ## 获取搜索结果页面，html是搜索结果页面
        html = self.webhtml.posturl(self.name)
        htmlclass = self.webhtml.gethtmlclass(html)
        xpath = '//h4[@class="bookname"]/a'
        hclass = htmlclass.xpath(xpath)
        if hclass:
            print('搜索小说：', hclass[0].text)
            self.targetUrl = self.xiaoshuozhan + hclass[0].attrib['href']
            print(self.targetUrl)
            self.currentUrl = self.targetUrl.replace('index.html', '')
            return True
        else:
            print('找不到对应的小说')
            return False

    def get_novel_list(self):
        # 下载小说章节目录
        zhangjie = input('请输入起始章节:')
        txt = self.webhtml.geturlcontent(self.targetUrl)
        htmlclass = self.webhtml.gethtmlclass(txt)

        # 取div中class='listman'下第一个dl下第二个dt后面同级的所有标签里的所有a标签
        xpath = '//div[@class="listmain"]/dl/dt[2]/following-sibling::*//a'

        hclass = htmlclass.xpath(xpath)

        # 当前下载页面
        zhangjie = int(zhangjie)
        number = 0
        self.zhanglist = []
        for i in hclass:
            line = []
            number += 1
            if number < zhangjie:
                continue
            hreflink = i.attrib['href']
            # print('hreflink=',hreflink,i.text)
            zhangjieNo = str(number).zfill(5)
            zhangname = '第 ' + str(number) + ' 章: ' + i.text.split('、')[-1]
            print(zhangjieNo, zhangname)
            url = self.currentUrl + hreflink
            line.append(zhangjieNo)
            line.append(zhangname)
            line.append(url)
            self.zhanglist.append(line)

def writetxt(strmsg, filename='log.txt'):  # 把strmsg写入错题本
    try:
        logFile = open(filename, 'a', encoding='utf-8')
        logFile.write(strmsg + '\n')
    except Exception as err:
        pass
    finally:
        logFile.close()
    return

def downtxt(zhangname, url, zhangNo):
    # print(zhangname,url)
    txtpage = Htmlquery("www.shuquge.com")

    txt = txtpage.geturlcontent(url)
    # print(txt)
    htmlclass = txtpage.gethtmlclass(txt)
    # print(type(htmlclass))
    # 取div中class='listman',该标签内的所有内容
    xpath = '//div[@class="showtxt"]/text()'

    hclass = htmlclass.xpath(xpath)

    # print(len(hclass))
    writetxt('\n\n' + zhangname + '\n', zhangNo + '.txt')
    for i in hclass[:-3]:
        # print('hreflink=',i)
        writetxt(i.replace('    ', ''), zhangNo + '.txt')

def downmanyzhang(zhanglist,processname):
    for zhang in zhanglist:
        #print('进程：', processname, ':', zhang[1] + " is start !")
        downtxt(zhang[1], zhang[2], zhang[0])
        print('进程：', processname, ':', zhang[1] + " is downloaded !")

def mutiprocess_down(zhanglist,name ,processNum=10):
    # 多进程
    zhanglength = len(zhanglist)
    shang = int(zhanglength / processNum)
    yushu = int(zhanglength % processNum)

    downloadProcesses = []

    # 开始创建进程
    for j in range(processNum):
        x = shang * j
        y = shang * j + shang
        print('x,y,j', x, y, j)
        downloadProcess = Process(target=downmanyzhang, args=(zhanglist[x:y], str(j + 1),))
        downloadProcesses.append(downloadProcess)
        downloadProcess.start()

    if yushu != 0:
        lastdownloadProcess = Process(target=downmanyzhang,
                                      args=(zhanglist[processNum * shang:], str(processNum + 1),))
        downloadProcesses.append(lastdownloadProcess)
        lastdownloadProcess.start()
    # 等待所有进程结束
    for analyseProcess in downloadProcesses:
        analyseProcess.join()

    os.system("type 0????.txt > " + name + '.txt')
    os.system("del 0????.txt")

