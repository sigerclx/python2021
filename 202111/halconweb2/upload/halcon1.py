import halcon as ha
import os
#import Hdevengine as hdev
# 本程序实现灯珠抠图的功能，抠出来保存到一个新的文件夹中


Image = ha.read_image(r'D:\Python\python2021\2021\202110\halconweb\现场照片\03.png')
path = os.path.abspath('.')
Width, Height = ha.get_image_size(Image)



#ha.close_window(WindowHandle)
WindowHandle = ha.open_window(0, 0, Width[0]/2, Height[0]/2,
                          father_window=0,mode='visible',machine='')
Red, Green, Blue = ha.decompose3(Image)
Region ,UsedThreshold = ha.binary_threshold(Green, 'max_separability', 'dark')
ConnectedRegions = ha.connection(Region)
SelectedRegions = ha.select_shape(ConnectedRegions, 'area', 'and', 3357.75, 900000)
RegionUnion = ha.union1(SelectedRegions)
Row1, Column1, Row2, Column2 = ha.smallest_rectangle1(RegionUnion)

# 返回值是list转化为int
Row1 = int(Row1[0])
Column1 = int(Column1[0])
Row2 = int(Row2[0])
Column2 = int(Column2[0])
Number = 0
Row = Row1
Area1 = 0
#print(Row1,type(Row1),type(Column1),type(Row2),type(Column2))

while (Area1 == 0):
    Rectangle = ha.gen_rectangle1( Row, Column1, Row+5,Column1+( Column2-Column1)/2)
    Row = Row + 5
    ImageReduced = ha.reduce_domain(Green, Rectangle)
    Regions = ha.threshold(ImageReduced, 0, 120)
    Area1, Row3, Column3 = ha.area_center(Regions)

ConnectedRegions1 = ha.connection(Regions)
SortedRegions = ha.sort_region(ConnectedRegions1, 'last_point', 'true', 'row')
ObjectSelected =ha.select_obj(SortedRegions, 1)
Row11, Column11, Row21, Column21 = ha.smallest_rectangle1(ObjectSelected)
print(type(Row11),type(Column11),type(Row21),type(Column21))

Row11 = int(Row11[0])
Column11 = int(Column11[0])
Row21 = int(Row21[0])
Column21 = int(Column21[0])
print(Row11,Column11,Row21,Column21)

ha.disp_obj(Image,WindowHandle)
ha.set_color(WindowHandle, 'blue')
ha.disp_circle(WindowHandle, Row21, Column21, 20)


ha.wait_seconds(3)



