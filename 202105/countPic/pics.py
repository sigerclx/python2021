import os,math,shutil
'''
为了上传图片到百度云，因为百度云每次上传有500张的限制，所以做了下面小程序
功能：把dirpath文件夹里的所有图片，分成everyfolderNumber数量的批次，分批平均移动到destpath文件夹下按数字建立的文件夹里
'''

# 建立空文件夹
def initfolder(path,nums):
    newpaths =[]
    path = path.strip()
    for i in range(nums):
        newpath = path+'\\'+str(i)
        newpaths.append(newpath)
        if not os.path.exists(newpath):
            os.makedirs(newpath)
    return newpaths


destpath = r"d:\pic1"
dirpath = r"Y:\个人文件夹\照片2"
f=open("dir.txt","w",encoding='utf-8')
allpic_files = []
for root,dirs,files in os.walk(dirpath):
    for file in files:
        allpic_files.append(os.path.join(root,file))
        #f.writelines(os.path.join(root,file)+"\n")

f.close()

allpic =  len(allpic_files)
everyfolderNumber = 490  # 每个文件夹里放入多少图片
folderNumber = math.ceil(allpic / everyfolderNumber)


print(allpic_files)
print(allpic,folderNumber)

newpaths = initfolder(destpath,folderNumber)


i=0

for file in allpic_files:
    destnum = int(i/ everyfolderNumber)
    dest  = os.path.join(destpath, str(destnum))
    print(i,file,dest)
    shutil.copy2(file,dest)
    i += 1







#shutil.move(r"C:\Users\Jacky\Pictures\ocr1.jpg", r"C:\Users\Jacky\Pictures\1")




