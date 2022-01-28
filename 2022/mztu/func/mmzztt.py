import requests,datetime
import pandas as pd
class Ttjj(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.1 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
            "Referer": "https://mmzztt.com/"
        }
        # 显示所有列
        pd.set_option('display.max_columns', None)
        # 显示所有行
        pd.set_option('display.max_rows', None)
        # 设置value的显示长度为100，默认为50
        pd.set_option('display.max_columns', 500)
        pd.set_option('max_colwidth', 500)
        pd.set_option('display.width', 1500)
        #pd.set_option('display.line_width', None)

    def today(self):
        return datetime.datetime.now().strftime("%Y-%m-%d")

    def top(self,url):
        response = requests.get(url, headers=self.headers)
        response.encoding = 'utf-8'
        htmltext = response.text
        return htmltext



