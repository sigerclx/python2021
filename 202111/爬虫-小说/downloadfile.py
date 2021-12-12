#下载文件，并生成
import requests,os,time
from searchengine.search  import Search,Downbook


def downloadfile(url,filename):
    strlist =(')','?','!','(','+','-',':',',')
    for s in strlist:
        filename = str.replace(filename,s,'')

    gettxt = Downbook()
    gettxt.setengine('down.bqg99.org','down.bqg99.org')
    try:
        #res =requests.get(url,headers=headers)
        res =gettxt.geturlcontent1(url)
        if not res:
            return
    except Exception as err:
        print("downloadfile 发现错误了："+str(err))
        return

    downloadFile = open(filename.lower(),'wb')
    for chunk in res.iter_content(20000):
        downloadFile.write(chunk)
    downloadFile.close()

    return 'ok'


def downloadmp3(word):
    mp3path = r'us_words/'

    downloadSite = r'http://media.shanbay.com/audio/us/'

    word =word.lower()+'.mp3'
    if not downloadfile(downloadSite+word,os.path.join(mp3path,word)):
        print(word,r"downloadfile.py 不能下载 not exist in http://media.shanbay.com/audio/us/，或者单词拼写错误")
    else:
        print(word,'downloaded !')


