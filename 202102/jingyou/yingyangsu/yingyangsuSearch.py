#获取单方精油信息
import tool.getJson,sys

## 设置令牌
tool.getJson.searchheader['token']="e9c580dc46e9b6f527109d2a71701528"
#print(tool.getJson.searchheader)
#sys.exit(0)
filters = ["searchBaseInfById","searchUseMethodById","searchConstituentById"]


import tool.readurl
danfangName = 'VM综合维生素'
urlS =tool.readurl.getUrl(danfangName)

for keyword in filters:
    #print("keyword",keyword)
    for s in urlS:
        #print("s=",s)
        if keyword in s and keyword==filters[0]: tool.getJson.produce1(s,danfangName)
        if keyword in s and keyword==filters[1]: tool.getJson.produce2(s,danfangName)
        if keyword in s and keyword==filters[2]: tool.getJson.produce3(s,danfangName)

print(danfangName,"抓取完成！")









