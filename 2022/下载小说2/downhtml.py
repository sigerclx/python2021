from searchengine.search  import Search
import time
import urllib

def writelog(strmsg,filename='info.txt'): #把strmsg写入日志
    try:
        logFile = open(filename,'a', encoding='utf-8')
        logFile.write(str(strmsg)+'\n')
    except Exception as err:
        logFile.write('log write err:'+str(err)+'\n')
        pass
    finally:
        logFile.close()
    return




def writehtml(url):
    #global webhtml
    webhtml = Search()
    webhtml.setengine("drive.my-elibrary.com", "drive.my-elibrary.com")
    txt =  webhtml.geturlcontent(url)

    htmlclass  = webhtml.gethtmlclass(txt)
    #print(type(htmlclass))

    xpath ='//div[@style="min-width: 600px"]/a'

    hclass = htmlclass.xpath(xpath)
    #restxt = webhtml.xpathdecode(hclass)
    print('-'*30,len(hclass),'-'*30)
    filelist = []
    directorylist = []
    for i in hclass:
        hreflink = i.attrib['href']
        #print('hreflink=',hreflink)
        herf1 = hreflink.split(r"/")
        if herf1[-1]!='..':
            #print('herf1=',herf1)
            url = 'https://drive.my-elibrary.com' + urllib.parse.unquote(hreflink)
            if herf1[-1]:
                filelist.append(url)
            else:
                directorylist.append(url)


    for k in filelist:
        herf2 = k.split(r"/")
        print('文件：',herf2[-1],'        路径：',k)
        writelog(herf2[-1])


    for j in directorylist:
        herf2 = j.split(r"/")
        print('目录：',j)
        writelog('\n-----------------------------------------------------------')
        writelog('目录：' + j+'\n')
        writehtml(j)






writehtml("https://drive.my-elibrary.com/")
