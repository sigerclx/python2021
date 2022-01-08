import win32com.client
import os,configparser

speak = win32com.client.Dispatch('SAPI.SPVOICE')

#speak.Speak("take bus")

from func.getWordMean import *

# aa={"mean": [{"adj.": ["令人惊异的"]}, {"vt.": ["使大为吃惊，使惊奇( amaze的现在分词)", "使惊异：感到非常好奇"]}, {"n.": ["吃惊", "好奇"]}], "us": "ə\'meɪzɪŋ", "us_mp3": "", "en": "əˈmeɪzɪŋ", "en_mp3": "http://res.iciba.com/resource/amp3/oxford/0/78/aa/78aae685459cfa9e787d0331c40e97ee.mp3"}
# cc=str('{#mean#: [{#adj.#: [#令人惊异的#]}, {#vt.#: [#使大为吃惊，使惊奇( amaze的现在分词)#, #使惊异：感到非常好奇#]}, {#n.#: [#吃惊#, #好奇#]}], #us#: "ə#meɪzɪŋ", #us_mp3#: ##, #en#: #əˈmeɪzɪŋ#, #en_mp3#: #http://res.iciba.com/resource/amp3/oxford/0/78/aa/78aae685459cfa9e787d0331c40e97ee.mp3#}')
# cc = cc.replace('#','\'')
# bb= eval(cc)
# print(bb)

aa= {'mean': [{'v.': ['绘画( draw的过去式 )', '拖', '拉', '拔出']}], 'us': 'dru','us_mp3': 'http://res.iciba.com/resource/amp3/1/0/b2/dd/b2dd08a69dcdac5a20a7b90b5c4b759f.mp3', 'en': 'dru:','en_mp3': 'http://res.iciba.com/resource/amp3/0/0/b2/dd/b2dd08a69dcdac5a20a7b90b5c4b759f.mp3'}

print(eval(aa))
