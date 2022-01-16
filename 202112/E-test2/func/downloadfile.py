#下载文件，并生成
import requests,os

def downloadfile(url,filename):
    #print(filename,url)
    res=''
    try:
        #res =requests.get(url,headers=headers)
        res =requests.get(url)
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

    #downloadSite = r'http://media.shanbay.com/audio/us/'
    downloadSite =r'http://dict.youdao.com/dictvoice?audio='

    #word =word.lower()+'.mp3'
    word = word.lower()
    if not downloadfile(downloadSite+word,os.path.join(mp3path,word)):
        print(word,r"downloadfile.py 不能下载 not exist in http://dict.youdao.com/dictvoice?audio=，或者单词拼写错误")
    else:
        print(word,'downloaded !')

#
# 1.
# 习惯说明：
#
# 所有api中，除部分特别说明， % s
# 直接替换为单词
#
# 2.
# 有道词典单词发音：
#
# http: // dict.youdao.com / dictvoice?audio = % s
#
# 3.
# 有道词典获取释义（支持单词和句子翻译）：
#
# http: // fanyi.youdao.com / openapi.do?keyfrom = appname & key = key & type = data & doctype = json & version = 1.2 & q = % s
# 需要申请key，直通车，文档说明api版本为1
# .1，实际可支持1
# .2，返回可选xml、json、jsonp，带读音、不带例句
#
# 4.
# 金山词霸api：
#
# http: // dict - co.iciba.com / api / dictionary.php?w = % s & key = key
# 需要申请key，直通车，仅返回xml格式，带例句。
#
#
# 5.
# 扇贝单词发音：
#
# 1.
# 美式：http: // media.shanbay.com / audio / us / % s.mp3
# 2.
# 英式：http: // media.shanbay.com / audio / uk / % s.mp3



