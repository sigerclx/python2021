import urllib.request
import urllib.parse

class Bing(object):
    def __init__(self):
        self.url = "http://api.microsofttranslator.com/v2/ajax.svc/TranslateArray2?"

    def translate(self, from_lan, to_lan,content,):
        data = {}
        data['from'] = '"' + from_lan + '"'
        data['to'] = '"' + to_lan + '"'
        data['texts'] = '["'
        data['texts'] += content
        data['texts'] += '"]'
        data['options'] = "{}"
        data['oncomplete'] = 'onComplete_3'
        data['onerror'] = 'onError_3'
        data['_'] = '1430745999189'
        data = urllib.parse.urlencode(data).encode('utf-8')
        strUrl = self.url + data.decode() + "&appId=%223DAEE5B978BA031557E739EE1E2A68CB1FAD5909%22"
        response = urllib.request.urlopen(strUrl)
        str_data = response.read().decode('utf-8')
        tmp, str_data = str_data.split('"TranslatedText":')
        translate_data = str_data[1:str_data.find('"', 1)]
        return translate_data


if __name__ == '__main__':

    content='Time goes by so fast, people go in and out of your life. You must never miss the opportunity to tell these people how much they mean to you.'
    bing=Bing()
    #print(bing.translate('zh', 'en','时间越来越快，人们进出你的生活。你绝不能错过机会告诉这些人对他们对你有多重要。'))
    #print(bing.translate('zh', 'en', '时间过得如此之快，人们在你的生活中进进出出。你绝不能错过告诉这些人他们对你有多重要的机会。'))
    print(bing.translate('en', 'zh', content))