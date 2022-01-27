import os,sys
def current_folder(folder,includefile=True):
    folderlists =[]
    filelists = []
    #os.walk(folder, topdown=True)
    if includefile:
        for file in os.listdir(folder):
            file = os.path.join(folder,file)
            if os.path.isdir(file):
                folderlists.append(file)
            else:
                filelists.append(file)
        return folderlists,filelists
    else:
        for file in os.listdir(folder):
            file = os.path.join(folder, file)
            if os.path.isdir(file):
                folderlists.append(file)
        return folderlists

def min_day():
    sourcePath = r's:\训练数据\test'
    folders1,files = current_folder(sourcePath)
    if folders1:
        folders1.sort()
        folders2,files = current_folder(folders1[0])
        if folders2:
            folders2.sort()
            folders3, files = current_folder(folders2[0])
            if folders3:
                folders3.sort()
                return folders3[0]
            else:
                return folders2[0]
        else:
            return folders1[0]

minday = min_day()
minday =minday.replace(r's:\训练数据\test' + '\\', '')

print(min_day(),len(minday.split("\\")))

