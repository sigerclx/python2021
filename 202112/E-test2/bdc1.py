from func.globalValue import *
from func.listen_write import *
from func.init import getbookcontent,db_init,getConfig,selectbook,getTestQuestions

# 预读参数
getConfig()
# 初始化数据库
db_init()
# 用户选择
choice = selectbook()
# 获取书单词，短语，句子list
book_words,book_phrases,book_sentences = getbookcontent(choice)

print(book_words)
print(book_phrases)
print(book_sentences)
# 获取测试题的list
words = getTestQuestions(book_words)
# 开始测试听写
listenWrite(words,Get_value('questionnum'))
Set_value('conn',None)

