import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


# 任意读取图片转化为验证图时的矩阵
imm = np.array(Image.open('3.jpg').convert('L'))
imm = imm/255 # 转化为0-1
imm1 = Image.fromarray(imm)  # 转化为图像
imm2 = imm1.resize([28,28])  # 压缩
im_array = np.array(imm2)
fs =im_array.reshape((1,28,28))  # 转化成可以用model.evaluate验证的矩阵
print(fs.shape)
print(fs)
#print(im_array)
print(len(im_array[0]))

#把转成矩阵的图画出来
plt.figure(figsize=(2,2))
plt.imshow(im_array, cmap=plt.cm.binary)
plt.show()

y_test = np.array([3])
print(y_test.shape)