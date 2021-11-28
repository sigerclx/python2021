from func.getweb.search import Web
import json

class Wanip(Web):
    def __init__(self):
        Web.__init__(self)
        #self.url = 'http://httpbin.org/ip'  # origin
        #self.url = 'https://jsonip.com/'    # ip
        self.url = 'https://api.ipify.org/?format=json' # ip


        Web.set_referer(self, 'www.oktime.com')

    def getip(self):
        iptxt = Web.geturlcontent(self,self.url)
        if iptxt:
            ipdict = json.loads(iptxt)
            return ipdict['ip']
        else:
            # 如果获取ip太频繁，就会出错
            return False