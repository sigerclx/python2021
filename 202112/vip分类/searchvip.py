import os,glob,shutil,sys
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

files = Get_file_list(r's:\训练数据\VIP\2021\12')
filelen = len(files)
print(filelen)
i = 0
for file in files:
    i += 1
    if '-0.' in file:
        print(filelen, i, file)
        shutil.move(file, r'S:\训练数据\VIP\2021-12分解\0')
    if '-1.' in file:
        print(filelen, i, file)
        shutil.move(file, r'S:\训练数据\VIP\2021-12分解\1')
    if '-2.' in file:
        print(filelen, i, file)
        shutil.move(file, r'S:\训练数据\VIP\2021-12分解\2')
