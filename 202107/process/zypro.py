import os
import time

def isRunning(process_name) :
    try:
        print('tasklist | findstr '+process_name)
        line = os.popen('tasklist | findstr ' + process_name).readlines()
        process=len(line)
        print(process)
        print(line)
        if process >=1 :
            return True
        else:
            return False
    except:
        print("程序错误")
        return False


if __name__=="__main__":
    flag=True
    while flag:
        flag = isRunning("XMind")
        print(flag)
        time.sleep(3)##每隔60s进行检查