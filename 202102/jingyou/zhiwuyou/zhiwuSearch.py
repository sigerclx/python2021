#获取单方精油信息
import tool.getJson,sys

## 设置令牌
tool.getJson.searchheader['token']="a661a5248d615ec4a524de5dd58d7946"
#print(tool.getJson.searchheader)
#sys.exit(0)
filters = ["searchBaseInfById","searchBotanyById","searchEfficacyById","searchAttrById","searchMoreById"]


import tool.readurl
danfangName = '玫瑰籽油'
urlS =tool.readurl.getUrl(danfangName)



for keyword in filters:
    #print("keyword",keyword)
    for s in urlS:
        #print("s=",s)
        if keyword in s and keyword==filters[0]: tool.getJson.produce1(s,danfangName)
        if keyword in s and keyword==filters[1]: tool.getJson.produce2(s,danfangName)
        if keyword in s and keyword==filters[2]: tool.getJson.produce3(s,danfangName)
        if keyword in s and keyword==filters[3]: tool.getJson.produce6(s,danfangName)
        if keyword in s and keyword == filters[4]: tool.getJson.produce8(s, danfangName)

print(danfangName,"抓取完成！")









