from multiprocessing import Process
import os
import time


def func(name):
    print('start a process')
    time.sleep(1)
    print('the process parent id :', os.getppid())
    print('the process id is :', os.getpid())


if __name__ == '__main__':
    processes = []
    for i in range(2):
        p = Process(target=func, args=(i,))
        processes.append(p)
    for i in processes:
        i.start()
    print ('start all process')
    for i in processes:
        i.join()
        # pass
    print('all sub process is done!')