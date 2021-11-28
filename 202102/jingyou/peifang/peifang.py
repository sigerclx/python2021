#获取复方精油信息
import tool.getJson,sys,os,time

## 设置令牌
tool.getJson.searchheader['token']="e9c580dc46e9b6f527109d2a71701528"

Name ="慢性浅表性胃炎"
tool.getJson.start(Name)
print(Name,"抓取完成！")

# 目录下所有配方
"""
for name in tool.getJson.file_name(r"urls/"):
    tool.getJson.peifangList=[]
    Name = str.replace(name,".txt","")
    tool.getJson.start(Name)
    print(Name,"抓取完成！")
    time.sleep(0.8)
"""
