import json
#从config.json中获取配置信息JSON串
def getJson(key,file='config.json'):
    with open(file) as file:
        jsonStr = json.loads(file.read())
    return jsonStr[key]