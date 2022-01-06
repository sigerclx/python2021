import os,glob,shutil
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

files = Get_file_list(r'U:\忠达-早期资料未整理\现场数据\Wheels-A\其他')
filelen = len(files)
i = 0
for file in files:
    i += 1
    firstStr = file.split('\\')[-1][0]
    secondstr =  file.split('\\')[-1][2]
    print(filelen,i,file,firstStr,secondstr)
    try:
        if firstStr == secondstr:
            if firstStr == '0':
                shutil.move(file,r'U:\忠达-早期资料未整理\现场数据\Wheels-A\训练标定模板文件夹\0-万向脚轮')
            if firstStr == '1':
                shutil.move(file,r'U:\忠达-早期资料未整理\现场数据\Wheels-A\训练标定模板文件夹\1-定向脚轮')
            if firstStr == '2':
                shutil.move(file,r'U:\忠达-早期资料未整理\现场数据\Wheels-A\训练标定模板文件夹\2-无脚轮')
            if firstStr == '3':
                shutil.move(file,r'U:\忠达-早期资料未整理\现场数据\Wheels-A\训练标定模板文件夹\3-日本脚轮')
            if firstStr == '4':
                shutil.move(file,r'U:\忠达-早期资料未整理\现场数据\Wheels-A\训练标定模板文件夹\4-白色脚轮')
        else:
            shutil.move(file, r'U:\忠达-早期资料未整理\现场数据\Wheels-A\训练标定模板文件夹\其他')
    except Exception:
        print('重名',file.split('\\')[-1][0:-5]+'-'+str(i)+'.jpg')
        shutil.move(file, os.path.join(r'U:\忠达-早期资料未整理\现场数据\Wheels-A\训练标定模板文件夹\重复',file.split('\\')[-1][0:-5]+'-'+str(i)+'.jpg'))