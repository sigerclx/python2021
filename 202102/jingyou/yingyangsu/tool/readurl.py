import fileinput
def getUrl(danfangName):
    comm = "https://wx.drmom.cn/jywy-wx/supplementBaseInf/"
    str=[]
    for line in fileinput.input(r"./urls/"+danfangName+".txt"):
        str.append(comm+line.rstrip('\n'))
        #print(comm+line)
    return str
