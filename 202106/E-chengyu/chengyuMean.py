from func.getWordMean import Getwordmean
from func.globalValue import *
from func.init import getconfig,selectbook,getbookcontent
from func.exam import Exam
import random
# mysearch = Search()
# mysearch.geturlcontent('山高水长的意思')
# #print(txt)
# mysearch.gethtmlclass()
# print(mysearch.chengyuhanyi())
if __name__ == '__main__':
    getconfig()
    book =selectbook()
    words = list(set(getbookcontent(book))) #去除重复的成语
    random.shuffle(words)

    dict = Getwordmean()
    exam = Exam()

    exam.title = '根据含义回答成语'
    exam.questionnum = get_value('questionnum')

    for word in words[0:exam.questionnum]:
        mean,pinyin = dict.mean(word)
        if mean:
            mean=mean.replace(word,'~')
            exam.answers.append(word)
            exam.answerpinyin.append(pinyin)
            exam.questions.append(mean)
        else:
            print(word,"查询不到")


    exam.startTest()



