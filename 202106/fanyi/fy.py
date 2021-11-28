import urllib.request
import urllib.parse
import json


def translation(word):

            url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
            data = {}
            data['i'] = word
            data['from'] = 'AUTO'
            data['to'] = 'AUTO'
            data['smartresult'] = 'dict'
            data['client'] = 'fanyideskweb'
            data['salt'] = '15790094838498'
            data['sign'] = '9ab763875001c1949ae49d3c230ba19f'
            data['ts'] = '1579009483849'
            data['bv'] = '5a84f6fbcebd913f0a4e81b6ee54608'
            data['doctype'] = 'json'
            data['version'] = '10.2'
            data['keyfrom'] = 'fanyi.web'
            data['action'] = 'FY_BY_CLICKBUTTION'
            data = urllib.parse.urlencode(data).encode('utf-8')
            response = urllib.request.urlopen(url, data)
            html = response.read().decode('utf-8')
            # print(json.loads(html))
            target = json.loads(html)
            return target['translateResult'][0][0]['tgt']



if __name__ == '__main__':
    an = translation('Time goes by so fast, people go in and out of your life. You must never miss the opportunity to tell these people how much they mean to you.')
    print(an)