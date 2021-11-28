import psutil
import os
print(u'内存使用：{}M'.format(psutil.Process(os.getpid()).memory_info().rss/1024/1024))