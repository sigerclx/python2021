import halcon as ha
# pip install mvtec-halcon==20111 (版本要对应就行)
#Image = ha.read_image('D:\我的文档\Pictures\yindu.jpg')

Image = ha.read_image(r'E:\Source\Gitee\python2021\2021\202110\halcon\car.jpg')
# D:\我的文档\Pictures
Width,Height = ha.get_image_size(Image)
print(Width,Height)
WindowHandle = ha.open_window(0, 0, Width[0]/2, Height[0]/2,
                              father_window=0,mode='visible',machine='')

gray = ha.rgb1_to_gray(Image)
thres = ha.threshold(gray, 100, 200)

ha.disp_obj(Image, WindowHandle)
ha.wait_seconds(2)
ha.clear_window(WindowHandle)
ha.disp_obj(thres, WindowHandle)
ha.wait_seconds(5)
