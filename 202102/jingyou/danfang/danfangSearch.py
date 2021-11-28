#获取单方精油信息
import tool.getJson,sys

## 设置令牌
tool.getJson.searchheader['token']="5a0eb466710fe3adaecf5849f9971d86"
#print(tool.getJson.searchheader)
#sys.exit(0)
filters = ["searchBaseInfById","searchBotanyById","searchSingleOilBaseInfSpiritualHealingById","searchSingleOilBaseInfSafetyById","searchUseMethod","searchSingleOilBaseInfAttrById","searchBlendOil","searchSingleOilBaseInfMoreById"]

import tool.readurl
danfangName = '栀子花'
urlS =tool.readurl.getUrl(danfangName)



for keyword in filters:
    #print("keyword",keyword)
    for s in urlS:
        #print("s=",s)
        if keyword in s and keyword==filters[0]: tool.getJson.produce1(s,danfangName)
        if keyword in s and keyword==filters[1]: tool.getJson.produce2(s,danfangName)
        if keyword in s and keyword==filters[2]: tool.getJson.produce3(s,danfangName)
        if keyword in s and keyword==filters[3]: tool.getJson.produce4(s,danfangName)
        if keyword in s and keyword==filters[4]: tool.getJson.produce5(s,danfangName)
        if keyword in s and keyword==filters[5]: tool.getJson.produce6(s,danfangName)
        if keyword in s and keyword==filters[6]: tool.getJson.produce7(s,danfangName)
        if keyword in s and keyword == filters[7]: tool.getJson.produce8(s,danfangName)

print(danfangName,"抓取完成！")









