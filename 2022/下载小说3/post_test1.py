import requests,time,sys
from 下载小说.searchengine.search  import Search
def posturl(searchkey):
    #searchkey = '弃宇宙'
    url = "https://www.shuquge.com/search.php"
    data = {"s":"6445266503022880974","searchkey":""}
    data['searchkey'] =searchkey
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
# post测试例子

webhtml = Search("www.shuquge.com")
html = webhtml.posturl('弃宇宙')
htmlclass = webhtml.gethtmlclass(html)

xpath = '//h4[@class="bookname"]/a'

hclass = htmlclass.xpath(xpath)
print(hclass[0].attrib['href'],hclass[0].text)

