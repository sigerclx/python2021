# 参考 https://github.com/pysrc/remote-desktop
# 如果抓图远程传递出去，每次都传完整的抓图，图像太大1920*1080*3=5.9m
# 求图像的减法，每次把差异部分传出去，就会小很多。
# 目前是无损保存
from PIL import ImageGrab
import numpy as np
from cv2 import cv2
import time

img1 = ImageGrab.grab()
time.sleep(1)
img2 = ImageGrab.grab()

imgnp1 = np.asarray(img1)
imgnp2 = np.asarray(img2)


# 求两个图像的np差
imgnp3 = imgnp2 - imgnp1


img1.save("1.png")
img2.save("2.png")

cv2.imwrite('1sub2.png',imgnp3)