from multiprocessing import Process
from searchengine.urldownload  import Htmlquery
from subprocess import Popen, PIPE
import os,sys
import shutil

class Procedure(object):
    def __init__(self,website="www.shuquge.com"):
        #self.inputname = novelname
        self.xiaoshuozhan = r'https://'+ website
        self.webhtml = Htmlquery(website)
        self.start = 1 #默认下载从第1章开始

    def search_novel(self):
        # 搜索小说
        name = input('请输入小说名称(eg:我在1982有个家/1480)：')
        name =r'我在1982有个家/200'
        userinput = name.split('/')

        if len(userinput)>1:
            self.name  = userinput[0]
            self.start = int(userinput[1])
            print(self.name,'下载从第',self.start,'章开始 ......')
        else:
            self.name = userinput[0]
            print(self.name, '下载从第 1 章开始 ......')

        ## 获取搜索结果页面，html是搜索结果页面
        html = self.webhtml.geturlcontent(r'https://www.0794.org/Search/'+self.name)
        #print(html)
        #print('----------------------------')
        htmlclass = self.webhtml.gethtmlclass(html)
        xpath = '//span[@class="s2"]/a'
        hclass = htmlclass.xpath(xpath)
        if hclass:
            print('搜索小说：', hclass[0].text)
            self.targetUrl = r'https:'+hclass[0].attrib['href']
            print(self.targetUrl)
            #self.currentUrl = self.targetUrl.replace('index.html', '')
            #sys.exit(0)
            return True
        else:
            print('找不到对应的小说')
            #sys.exit(0)
            return False

    def get_novel_list(self):
        # 下载小说章节目录
        zhangjie = self.start
        txt = self.webhtml.geturlcontent(self.targetUrl)
        #print(txt)

        htmlclass = self.webhtml.gethtmlclass(txt)


        # 取div中class='listman'下第一个dl下第二个dt后面同级的所有标签里的所有a标签
        xpath = '//div[@class="box_con"]/div/dl//a'

        hclass = htmlclass.xpath(xpath)
        print('hclass = ',len(hclass))
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

            #sys.exit(0)

            url = 'https:' + hreflink
            print(zhangjieNo, zhangname,url)
            line.append(zhangjieNo)
            line.append(zhangname)
            line.append(url)
            self.zhanglist.append(line)



    def mutiprocess_down(self,processNum=10):
        if os.path.exists('novels'):
            shutil.rmtree('novels')
        if os.path.exists(self.name + '.txt'):
            os.remove(self.name + '.txt')
        create_folder('novels')
        # 多进程
        zhanglength = len(self.zhanglist)
        shang = int(zhanglength / processNum)
        yushu = int(zhanglength % processNum)

        downloadProcesses = []

        # 开始创建进程
        for j in range(processNum):
            x = shang * j
            y = shang * j + shang
            # print('x,y,j', x, y, j)
            downloadProcess = Process(target=downmanyzhang, args=(self.zhanglist[x:y], str(j + 1),))
            downloadProcesses.append(downloadProcess)
            downloadProcess.start()

        if yushu != 0:
            lastdownloadProcess = Process(target=downmanyzhang,
                                          args=(self.zhanglist[processNum * shang:], str(processNum + 1),))
            downloadProcesses.append(lastdownloadProcess)
            lastdownloadProcess.start()
        # 等待所有进程结束
        for analyseProcess in downloadProcesses:
            analyseProcess.join()
        # print(r"del novels\0????.txt /q")
        # filename = os.path.join('novels',"*.txt")
        # os.remove(filename)

        os.system('echo off')
        os.system(r"type novels\0????.txt > " + self.name + '.txt')
        shutil.rmtree('novels')



def create_folder(dest_path):
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

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
    txtpage = Htmlquery("www.0794.org")

    txt = txtpage.geturlcontent(url)
    #print(txt)

    htmlclass = txtpage.gethtmlclass(txt)
    # print(type(htmlclass))
    # 取div中class='listman',该标签内的所有内容
    xpath = '//div[@id="content"]/text()'

    hclass = htmlclass.xpath(xpath)
    filename = os.path.join('novels', zhangNo + '.txt')

    # print(len(hclass))
    writetxt('\n\n' + zhangname + '\n', filename)
    for i in hclass[:-3]:
        # print('hreflink=',i)
        writetxt(i.replace('    ', ''), filename)

def downmanyzhang(zhanglist, processname):
    for zhang in zhanglist:
        # print('进程：', processname, ':', zhang[1] + " is start !")
        downtxt(zhang[1], zhang[2], zhang[0])
        print('进程：', processname, ':', zhang[1] + " is downloaded !")




