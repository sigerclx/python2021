# https://www.126shu.org/
from searchengine.search  import Search,Downbook
from downloadfile import downloadfile,os
import requests,time,sys
from requests import RequestException
# 注意 本程序的 request 和 urllib3 版本不能太高

page = 454

def downloadPage(url):
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


    xpath ='//div[@class="l"]//span[@class="s2"]/a'
    #xpath ='//div[@style="min-width: 600px"]/a'

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



for i in range(80,page):

    url = "https://www.126shu.org/novel-list-1-" +str(i)+".html"
    print('准备下载 , 第 ',i,' 页',url)
    downloadPage(url)





