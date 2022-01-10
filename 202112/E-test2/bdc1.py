from func.globalValue import *
from func.listen_write import *
from func.init import getbookcontent,db_init,getConfig,selectbook,getTestQuestions,replaceall
from func.bing import Bing
from func.google import Google

# 预读参数
getConfig()
# 初始化数据库
db_init()
# 用户选择
choice = selectbook()
# 获取书单词，短语，句子list
book_words,book_phrases,book_sentences = getbookcontent(choice)

#print(book_words)
#print(book_phrases)
#print(book_sentences)


#bing =  Bing()
bing = Google()
i = 0
inputs=''
if book_sentences:
    for sentence in book_sentences:
        i+=1
        print('\n第',i,end='题 : ')
        print(bing.translate('en', 'zh', sentence))
        inputs = input('请输入汉译英：')
        sentence = sentence.upper()
        inputs = inputs.upper()
        sentence = replaceall(sentence)
        inputs = replaceall(inputs)
        if sentence==inputs:
            print('回答正确!\n')
        else:
            print('回答错误！\n')
else:
    print('所选书里没有词句')

