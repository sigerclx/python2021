import os,glob,shutil,sys

# 获取当前目录下的文件和目录，当前层，不含子目录。默认同时返回目录和文件列表
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
            if os.path.isfile(file):
                folderlists.append(file)
        return filelists

def Create_folder(dest_path):
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

# 获取目录文件列表,如果传递进来是一个文件也可以
def Get_file_list(source_path):
    files_list=[]
    if os.path.isfile(source_path):
        files_list.append(source_path)
        return files_list

    for i in glob.glob(source_path + '/**/*', recursive=True):
        if os.path.isfile(i):
            files_list.append(i)
    return files_list
sourcepath =  r'S:\数据收集\海尔冷柜-脚轮\B线\20220121采集\20'
destpath = r'S:\数据收集\海尔冷柜-脚轮\B线\20220221-1-数据整理'
folder , files = current_folder(sourcepath)
#print(files)
filelen = len(files)
print(filelen)
i = 0
for file in files:
    filename =  file.split('\\')[-1]
    xinghao = filename[:9]
    newpath  =  os.path.join(destpath,xinghao)
    Create_folder(newpath)
    print(xinghao)
    i += 1
    print(i,filelen,xinghao,file)
    shutil.copy2(file, newpath)
