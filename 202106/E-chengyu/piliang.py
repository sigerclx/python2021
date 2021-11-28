from func.getWordMean import Getwordmean
from func.globalValue import *
from func.init import getconfig,selectbook,getbookcontent

if __name__ == '__main__':
    getconfig()
    book =selectbook()
    words = getbookcontent(book)

    dict = Getwordmean()
    for i in words:
        mean = dict.mean(i)
        print(mean)