import exifread

import time,os,glob


def get_pic_shoot_time(file):
    img = exifread.process_file(open(file, 'rb'))
    print(img)
    time1 = str(img['Image DateTime'])
    #format = "%Y:%m:%d %H:%M:%S"
    return time1 #.strptime(str(time1), format)

def get_file_modify_time(file):
    tupTime = time.localtime(os.path.getatime(file))  # 秒时间戳
    #stadardTime = time.strftime("%Y:%m:%d %H:%M:%S", tupTime)
    stadardTime = time.strftime("%Y:%m:%d", tupTime)
    return stadardTime


def set_pic_modify_time(file,time1):
    format = "%Y:%m:%d %H:%M:%S"
    t1 = time.mktime(time.strptime(str(time1), format))
    os.utime(file, times=(t1, t1))


def change_wrong_time(file):
    t1 = get_pic_shoot_time(file)
    t2 = get_file_modify_time(file)
    if t1:
        if not (t2 in t1) :
            print('Modify success!',file)
            set_pic_modify_time(file,t1)

fName = r"22.jpg"  # 文件路径，文件存在才能成功（可以写绝对路径，也可以写相对路径）
change_wrong_time(fName)

# dir_path = r'Y:\百度云\照片备份\9月6日咖啡拉花培训\9.6'
# dir_path = r'w:\jacky\Drive\Moments\photo\丈母娘\丈母娘手机2021-5\DCIM\arttx'
# for i in glob.glob(dir_path + '/**/*', recursive=True):
#     if os.path.isfile(i):
#         change_wrong_time(i)

#
# fName = r"11.jpg"  # 文件路径，文件存在才能成功（可以写绝对路径，也可以写相对路径）
# time1 ='2021:5:23 14:40:00'
# set_pic_modify_time(fName,time1)
# change_wrong_time(fName)
# print(get_pic_shoot_time(fName))







