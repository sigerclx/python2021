# 利用金山词霸的api解析单词含义和美式，英式发音，音标等
import requests
import os
import json
import pprint


def createUrl(word):
    url_1 = r'http://dict-co.iciba.com/api/dictionary.php?w='
    url_2 = r'&type=json&key=6FDE7DE576DE770A91C94917D29BF37C'
    # print(url_1+word+url_2)
    if word.strip() == '':
        return ''
    return (url_1 + word + url_2)


def analysisJinShanJson(meanJson):
    meanlist = {}

    symbols = meanJson['symbols'][0]
    # print("symbols="+str(symbols))
    try:
        parts = symbols['parts']
    except Exception as err:
        return

    mean = []
    line = {}
    # 获取各类词形的含义
    for u in parts:
        line.setdefault(u['part'], u['means'])
        mean.append(line)
        line = {}

    meanlist.setdefault('mean', mean)
    meanlist.setdefault('us', symbols['ph_am'])  # 美式音标
    meanlist.setdefault('us_mp3', symbols['ph_am_mp3'])  # 美式MP3下载地址
    meanlist.setdefault('en', symbols['ph_en'])  # 英式音标
    meanlist.setdefault('en_mp3', symbols['ph_en_mp3'])  # 英式MP3下载地址

    return meanlist


def getwordMean(word):
    timeOut = 10

    word = word.lower()
    try:
        url = createUrl(word).strip()
        if url == '':
            return
        res = requests.get(url, timeout=timeOut)
        # print(res)
    except Exception as err:
        print(str(err))
        return

    try:
        wordMean = res.json()
        wordMean = analysisJinShanJson(wordMean)
    except Exception as err:
        print(str(err))
        return

    return wordMean


# mean = getwordMean('her')
#
# if mean:
#     print(mean)
# else:
#     print('no mean')


