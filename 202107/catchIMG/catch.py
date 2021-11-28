# 参考 https://github.com/pysrc/remote-desktop
from PIL import ImageGrab
#import pyautogui
img =  ImageGrab.grab()
height, width =img.size
print(height, width)
#img.show()
# 无损保留
img.save('p1.jpg')