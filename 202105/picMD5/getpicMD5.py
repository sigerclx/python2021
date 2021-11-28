import hashlib
import os
import datetime



#@
def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename,'rb')
    while True:
        b = f.read(2048)
        if not b :
            break
        myhash.update(b)
        f.close()
        return myhash.hexdigest()

def main():
    # starttimeB = datetime.datetime.now()
    for j in range(10):
        for i in range(8000):
            # print(GetFileMd5('829.zip'))
            GetFileMd5('1.pkg')

    # endtime = datetime.datetime.now()

if __name__ == '__main__':
    main()