import halcon as ha
import os
#import Hdevengine as hdev
# 本程序实现灯珠抠图的功能，抠出来保存到一个新的文件夹中

def halcon_circle(uploadpath):
    Image = ha.read_image(uploadpath)
    Width, Height = ha.get_image_size(Image)
    #print(Width, Height)

    WindowHandle = ha.open_window(0, 0, Width[0] / 2, Height[0] / 2, father_window=0, mode='visible', machine='')
    Red, Green, Blue = ha.decompose3(Image)
    ImageResult1, ImageResult2, ImageResult3 = ha.trans_from_rgb(Red, Green, Blue, 'hsv')
    h_s, UsedThreshold1 = ha.binary_threshold(ImageResult2, 'max_separability', 'light')
    h_h = ha.threshold(ImageResult1, 0, 10)
    RegionIntersection = ha.intersection(h_s, h_h)
    RegionClosing = ha.closing_rectangle1(RegionIntersection, 1, 15)
    ConnectedRegions2 = ha.connection(RegionIntersection)
    SelectedRegions = ha.select_shape(ConnectedRegions2, 'area', 'and', 50, 99999999)
    RegionUnion = ha.union1(SelectedRegions)
    RegionClosing1 = ha.closing_rectangle1(RegionUnion, 1, 50)
    ConnectedRegions1 = ha.connection(RegionClosing1)
    SelectedRegions1 = ha.select_shape_std(ConnectedRegions1, 'max_area', 70)
    Row1, Column1, Row2, Column2 = ha.smallest_rectangle1(SelectedRegions1)
    Rectangle = ha.gen_rectangle1(Row1[0], Column1[0], Row2[0], (Column2[0] + Column1[0]) / 2)
    RegionIntersection1 = ha.intersection(SelectedRegions1, Rectangle)
    Row11, Column11, Row21, Column21 = ha.smallest_rectangle1(RegionIntersection1)
    Rectangle1 = ha.gen_rectangle1(Row11[0], Column11[0], Row11[0] + 5, Column21[0])
    RegionIntersection2 = ha.intersection(RegionIntersection1, Rectangle1)
    ConnectedRegions = ha.connection(RegionIntersection2)
    SortedRegions = ha.sort_region(ConnectedRegions, 'first_point', 'false', 'column')
    ObjectSelected = ha.select_obj(SortedRegions, 1)
    Area, Row, Column = ha.area_center(ObjectSelected)
    Circle = ha.gen_circle(Row[0], Column[0], 10)
    Circle1 = ha.gen_circle(Row[0], Column[0], 20)
    mark = ha.difference(Circle1, Circle)
    ImageResult01 = ha.paint_region(mark, ImageResult1, 100, 'fill')
    ImageResult02 = ha.paint_region(mark, ImageResult2, 255, 'fill')
    ImageResult03 = ha.paint_region(mark, ImageResult3, 255, 'fill')
    ImageRed, ImageGreen, ImageBlue = ha.trans_to_rgb(ImageResult01, ImageResult02, ImageResult03, 'hsv')
    ImageRGB = ha.compose3(ImageRed, ImageGreen, ImageBlue, )
    ha.write_image(ImageRGB, 'png', 0, './static/ok/1')
    #ha.disp_obj(ImageRGB, WindowHandle)
    #
    #ha.wait_seconds(5)


#halcon_circle(r'E:\Source\Gitee\python2021\2021\202110\halcon\现场照片\02.png')
