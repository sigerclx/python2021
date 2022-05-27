import os
import backup5.tools.log

# 文件的工具函数

# 获取当前目录下的文件和目录，当前层，不含子目录。默认同时返回目录和文件列表
def folderfilelist(folder,includefile=True):
    folderlists =[]
    filelists = []

    for file in os.listdir(folder):
        file = os.path.join(folder,file)
        if os.path.isdir(file):
            folderlists.append(file)
        else:
            filelists.append(file)

    if includefile:
        return filelists,folderlists
    else:
        return filelists


def delete_folder(path):
    # 如果上面文件都删除了，那就把目录也删除掉
    if os.path.isdir(path):
        try:
            backup5.tools.log.write_log('deleting folder ' + path)
            os.rmdir(path)  # 删空目录,如果目录里文件不空,则不能删除
            print('deleting folder ' + path + ' ...')
        except Exception as e:
            backup5.tools.log.write_log(e)