# 为了解决某一目录下9万多张照片，想按年建文件夹存放。
from tools import *
import os,shutil
# 手机备份到百度云后，太多年没有清理，所以，下载下来后，目录里文件太多超过9w,所以写程序分年存放
path = r'Y:\百度云\照片备份\来自：iPhone'
nums=0
for lists in os.listdir(path):
        curr_path = os.path.join(path, lists)
        if os.path.isfile(curr_path):
            #print(lists,type(lists))
            if ('baiduyun' in lists):
                continue
            if ('.tiff' in lists) or ('.mov' in lists) or ('.jpg' in lists) or ('.png' in lists)or ('.heic' in lists):
                nums +=1

                file = lists.split('-')[0]
                try:
                    if  int(file)<2022 :
                        dest_path = os.path.join(path,file)
                    else:
                        continue
                except Exception:
                    c_date= get_pic_shoot_time1(curr_path)
                    if c_date:
                        dest_path =os.path.join(path, str(c_date.tm_year))

                    else:
                        c_date= get_file_modify_time(curr_path)
                        if c_date:
                            dest_path =os.path.join(path, str(c_date))
                        else:
                            print('no date-----------------------')
                            continue

                Create_folder(dest_path)

                print(nums,curr_path, dest_path)
                try:
                    shutil.move(curr_path, dest_path)
                except Exception:
                    pass




