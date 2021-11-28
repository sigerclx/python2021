#获取复方精油信息
import tool.getfufangJson,sys

## 设置令牌
tool.getfufangJson.searchheader['token']="a661a5248d615ec4a524de5dd58d7946"
#print(tool.getJson.searchheader)
#sys.exit(0)

filters = ["searchBaseInfById","searchOtherById","searchSpiritualHealingById","searchSafetyById","searchUseMethod","searchAllOilConstituentById"]


import tool.readurl
fufangName = '全神贯注'
urlS =tool.readurl.getfufangUrl(fufangName)

for keyword in filters:
    #print("keyword",keyword)
    for s in urlS:
        #print("s=",s)
        if keyword in s and keyword==filters[0]: tool.getfufangJson.produce1(s,fufangName)
        if keyword in s and keyword==filters[1]: tool.getfufangJson.produce2(s,fufangName)
        if keyword in s and keyword==filters[2]: tool.getfufangJson.produce3(s,fufangName)
        if keyword in s and keyword==filters[3]: tool.getfufangJson.produce4(s,fufangName)
        if keyword in s and keyword==filters[4]: tool.getfufangJson.produce5(s,fufangName)
        if keyword in s and keyword==filters[5]: tool.getfufangJson.produce6(s,fufangName)

print(fufangName,"抓取完成！")