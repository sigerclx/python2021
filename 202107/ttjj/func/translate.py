import urllib.request
import urllib.parse

def translate(from_lan, to_lan, content ):
    url = "http://api.microsofttranslator.com/v2/ajax.svc/TranslateArray2?"
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
    strUrl = url + data.decode() + "&appId=%223DAEE5B978BA031557E739EE1E2A68CB1FAD5909%22"
    try:
        response = urllib.request.urlopen(strUrl)
        str_data = response.read().decode('utf-8')
        tmp, str_data = str_data.split('"TranslatedText":')
        translate_data = str_data[1:str_data.find('"', 1)]
    except Exception as err:
        print(err)
        return

    return translate_data