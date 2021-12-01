# https://www.126shu.org/
from searchengine.search  import Search,Downbook
from downloadfile import downloadfile,os
import requests,time,sys
from requests import RequestException
# 注意 本程序的 request 和 urllib3 版本不能太高

page = 92

def downloadPage(url):
    # 下载txt小说的接口
    txturl = 'https://down.bqg99.org/modules/article/txtarticle.php?id='
    webhtml = Downbook()
    #print(getPage.geturlcontent(url))

    txt =  webhtml.geturlcontent(url)
    # f =open('web.txt',encoding='utf-8')
    # txt=f.read()
    # f.close()

    #print(txt)

    htmlclass  = webhtml.gethtmlclass(txt)

    #print(len(htmlclass))

    #找到下载链接起始的特征
    xpath ='//div[@class="l"]//span[@class="s2"]/a'
    #xpath ='//div[@style="min-width: 600px"]/a'

    # 获取链接的class
    hclass = htmlclass.xpath(xpath)
    #restxt = webhtml.xpathdecode(hclass)
    print('-'*30,len(hclass),'-'*30)

    bookstores = []
    for i in hclass:
        booklists = []
        hreflink = i.attrib['href']
        hreftitle = i.attrib['title']
        bookno = hreflink.split(r"/")[-1]
        bookno = bookno[:-5]

        booklists.append(hreftitle)
        booklists.append(str(bookno))
        bookstores.append(booklists)


    #print(bookstores)
    #sys.exit(0)
    number = 0
    for book in bookstores:
        number += 1
        downloadurl = txturl + book[1]
        bookname =book[0]+'_'+book[1]+'.txt'
        path = os.path.join('novelsbook',bookname)
        print('下载：第 ' + str(number) + ' novelsbook', book[1], book[0])
        downloadfile(downloadurl,path)



for i in range(1,page):

    url = "https://www.126shu.org/novel-list-2-" +str(i)+".html"
    print('准备下载 , 第 ',i,' 页',url)
    downloadPage(url)





