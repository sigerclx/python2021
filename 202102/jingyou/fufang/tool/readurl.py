import fileinput
def getUrl(danfangName):
    comm = "https://wx.drmom.cn/jywy-wx/singleOilBaseInf/"
    str=[]
    for line in fileinput.input(r"./danfangurls/"+danfangName+".txt"):
        str.append(comm+line.rstrip('\n'))
        #print(comm+line)
    return str

def getfufangUrl(fufangName):
    comm = "https://wx.drmom.cn/jywy-wx/blendOilBaseInf/"
    str=[]
    for line in fileinput.input(r"./fufangurls/"+fufangName+".txt"):
        str.append(comm+line.rstrip('\n'))
        #print(comm+line)
    return str

