# 利用本地数据库，结合百度搜索，查找成语的含义
# 本地数据库找不到，就到百度引擎找,或必应引擎找
from func.searchengine.search import Biying_Chengyuhanyi,Baidu_Chengyuhanyi
from func.db.access import DbConnect
from func.globalValue import *

class Getwordmean(object):
    def __init__(self):
        self.dictdb  = DbConnect()
        self.engine = get_value('engine')
        if self.engine.lower() == 'baidu':
            self.search = Baidu_Chengyuhanyi()
        else:
            self.search = Biying_Chengyuhanyi()

    def mean(self,word):
        pinyin=None
        #先查本地数据库
        wordmean,pinyin = self.dictdb.search_word_mean(word)
        if wordmean:
            return wordmean,pinyin
        # 再查搜索引擎
        wordmean = self.search.getmean(word)
        if wordmean:
            self.dictdb.write_word_Mean(word,wordmean)
            print('从',self.engine , "引擎，补充成语\'%s\'的含义到数据库." % (word))
            return wordmean,'无'
        else:
            return None,None






