
import requests
import base64
def ocr(img_path:str)->list:
    '''
    根据图片路径，将图片转为文字，返回识别到的字符串列表
    '''
    # 请求头
    headers = {
        'Host': 'www.paddlepaddle.org.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Origin': 'https://www.paddlepaddle.org.cn',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.paddlepaddle.org.cn/hub/scene/ocr',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    }
    # 打开图片并对其使用 base64 编码
    with open(img_path,'rb') as f:
        img = base64.b64encode(f.read())
    # 设定请求体
    data = '{"image":"%s"}'%str(img)[2:]
    # 开始调用 ocr 的 api
    response = requests.post('https://www.paddlepaddle.org.cn/paddlehub-api/image_classification/chinese_ocr_db_crnn_mobile', headers=headers, data=data)
    # 设置一个空的列表，后面用来存储识别到的字符串
    ocr_text = []
    result = response.json()['result']
    # 将识别的字符串添加到列表里面
    for r in result:
        lines = r['data']
        for line in lines:
            ocr_text.append(line['text'])
    # 返回字符串列表
    return ocr_text
'''
img_path 里面填图片路径,这里分两种情况讨论:
第一种:假设你的代码跟图片是在同一个文件夹，那么只需要填文件名,例如 test1.jpg (test1.jpg 是图片文件名)
第二种:假设你的图片全路径是 D:/img/test1.jpg ,那么你需要填 D:/img/test1.jpg
'''
img_path = 'ocr1.jpg'
# content 是识别后得到的结果
content = "".join(ocr(img_path))
# 输出结果
print(content)
