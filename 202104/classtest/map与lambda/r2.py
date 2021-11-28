'''
旅行者 坐标移动
每次的在x,y的移动步长为[[1,1],[-2,2],[3,-3],[4,4],[5,6],[6,5]]
循环计算走了N步后的现坐标
'''
from functools import reduce
import numpy as np
list_x = np.array([[1,1],[-2,2],[3,-3],[4,4],[5,6],[6,5]])
list_y = [1,2,3,4,5]

k = reduce(lambda x,y:x+y,list_x)
print(k)