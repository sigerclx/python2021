# 从登录接口获取到sign（暂且当作token），并将sign作为参数用于学生金币充值接口

import requests
import json
import urllib3
urllib3.disable_warnings()

# 登录接口
url1 = "http://api.nnzhp.cn/api/user/login"
# 学生金币充值接口
url2 = "http://api.nnzhp.cn/api/user/gold_add"
param1 = {
    "username": "niuhanyang",
    "passwd": "aA123456"
}

session = requests.session()
response = session.post(url=url1, data=param1)
print(response.text)
response = json.loads(response.text)
# 从响应体中提取sign（类似于token值，后面用于其它接口的调用）
sign = response["login_info"]["sign"]
# 由于此案例要求传入cookie而非token值，所以只能打印出来，手动添加至下一个请求的header中
print(sign)

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0",
    "Cookie": "niuhanyang=754a2e97989e9ba3d5ab8dc6764f5b51"
}

# 假如此案例要求传入token值，则不需要先print打印，可直接向header请求头添加对象键值，如下：
# header['token'] = sign

param2 = {
    "stu_id": 123456,
    "gold": 10000
}

res = session.post(url=url2, headers=header, data=param2)
print(res.text)