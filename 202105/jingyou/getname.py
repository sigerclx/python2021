import os,time,glob

def getfiles(path):
    allpic_files=[]
    for i in glob.glob(path + '/**/*', recursive=True):
        if os.path.isfile(i):
            allpic_files.append(i)
    return allpic_files

path = r'配方\单方'
allfiles = getfiles(path)

allnames =[]

f1 = open('单方.txt', mode='w', encoding='utf-8')
for i in allfiles:
    file = open(i, mode='r', encoding='utf-8')
    line = file.readline()
    if line:
        line= line.replace('英文名','').split('：')
        print(line[0],line[1])
        f1.writelines('单方,'+ line[0]+','+line[1].replace(' 拉丁名','')+'\n')
    file.close()
f1.close()


path = r'配方\复方'
allfiles = getfiles(path)

allnames =[]

f1 = open('复方.txt', mode='w', encoding='utf-8')
for i in allfiles:
    file = open(i, mode='r', encoding='utf-8')
    line = file.readline()
    if line:
        line= line.replace('英文名','').replace('\n','').split('：')
        print(line[0],line[1])
        f1.writelines('复方,'+ line[0]+','+line[1]+'\n')
    file.close()
f1.close()


path = r'配方\营养素'
allfiles = getfiles(path)
allnames =[]

f1 = open('营养素.txt', mode='w', encoding='utf-8')
for i in allfiles:
    file = open(i, mode='r', encoding='utf-8')
    line = file.readline()
    if line:
        line= line.replace('英文名','').replace('\n','').split('：')
        print(line[0],line[1])
        f1.writelines('营养素,'+ line[0]+','+line[1]+'\n')
    file.close()
f1.close()

path = r'配方\植物油'
allfiles = getfiles(path)
allnames =[]

f1 = open('植物油.txt', mode='w', encoding='utf-8')
for i in allfiles:
    file = open(i, mode='r', encoding='utf-8')
    line = file.readline()
    if line:
        line= line.replace('英文名','').replace('\n','').split('：')
        print(line[0],line[1])
        f1.writelines('植物油,'+ line[0]+','+line[1].replace(' 拉丁名','')+'\n')
    file.close()
f1.close()
