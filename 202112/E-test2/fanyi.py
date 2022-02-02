from func.globalValue import *
from func.listen_write import *
from func.init import getbookcontent,getConfig,selectbook,getTestQuestions,replaceall
from func.bing import Bing
import random,sys
#from func.google import bing

# 句子翻译
# 预读参数
getConfig()
# 初始化数据库
#db_init()
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
    random.shuffle(book_sentences)
    for sentence in book_sentences:
        i+=1
        print('\n第',i,end='题 : ')
        sentence = sentence.split('|')
        print(sentence)
        if len(sentence)==1:
            hanyu = bing.translate('en', 'zh', sentence[0])
        else:
            hanyu = sentence[1]
        print(hanyu)
        inputs = input('请输入汉译英：')
        answer = sentence[0]
        sentence = sentence[0].upper()
        inputs = inputs.upper()
        inputs = replaceall(inputs)

        sentenceduibi = replaceall(sentence)

        while sentenceduibi!=inputs:
            print('回答错误！\n')
            #print(sentenceduibi,inputs)
            if inputs=='I':
                print('正确答案：',answer)
            if i >10:
                print('答题结束！')
                sys.exit(0)
            print('\n第', i, end='题 : ')
            print(hanyu)
            inputs = replaceall(input('请再次输入汉译英：'))
            inputs = inputs.upper()

        print('回到正确！\n')
else:
    print('所选书里没有词句')

