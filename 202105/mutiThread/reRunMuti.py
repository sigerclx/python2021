import os,time
from multiprocessing import Process
#  使用multiprocessing模块: 派生Process的子类，重写run方法

class MyProcess(Process):
  def __init__(self):
    Process.__init__(self)
  def run(self):
    print("子进程开始>>> pid={0},ppid={1}".format(os.getpid(),os.getppid()))
    time.sleep(2)
    print("子进程终止>>> pid={}".format(os.getpid()))

def main():
  print("主进程开始>>> pid={}".format(os.getpid()))
  myp=MyProcess()
  myp.start()
  # myp.join()
  print("主进程终止")

if __name__ == '__main__':
    main()