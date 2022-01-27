from func.globalValue import *
from func.listen_write import *
from func.init import getbookcontent,db_init,getConfig,selectbook,getTestQuestions,replaceall
from func.bing import Bing
#from func.google import bing

# 句子翻译
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
bing = Bing()
i = 0
inputs=''
if book_sentences:
    for sentence in book_sentences:
        i+=1
        print('\n第',i,end='题 : ')
        sentence = sentence.split('|')
        if len(sentence)==1:
            hanyu = bing.translate('en', 'zh', sentence[0])
        else:
            hanyu = sentence[1]
        print(hanyu)
        inputs = input('请输入汉译英：')
        sentence = sentence[0].upper()
        inputs = inputs.upper()
        sentence = replaceall(sentence)
        inputs = replaceall(inputs)
        while sentence!=inputs:
            print('回答错误！\n')
            print('\n第', i, end='题 : ')
            print(hanyu)
            inputs = input('请再次输入汉译英：')
            inputs = inputs.upper()
            if inputs=='I':
                print(sentence)
        print('回到正确！\n')
else:
    print('所选书里没有词句')

