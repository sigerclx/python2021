import halcon as ha
import os
import threading
import requests
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

def halcon_circle1(uploadpath):
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
    #picName = furl.split(r'/')[-1]
    picName = uploadpath.split('\\')[-1]
    print('halcon:',picName)
    newurl = r'http://nas.clearmediatech.com:8888/static/images/' +picName[:-4] + '_circle.png'
    basepath = os.path.dirname(__file__)
    newpath = os.path.join(basepath, 'static\images', picName[:-4] + '_circle.png')
    ha.write_image(ImageRGB, 'png', 0, newpath)
    # fp = secure_filename(newpath)
    jo = {'fid':1, 'fp':newurl}
    areas = [
        {"type": "前置液阶段","x1": 0, "x2": 10},
        {"type": "携砂液阶段1","x1": 20, "x2": 25},
        {"type": "暂堵转向阶段","x1": 25, "x2": 30},
        {"type": "携砂液阶段2","x1": 30, "x2": 35},
        {"type": "顶替液阶段","x1": 35, "x2": 40}
             ]
    jo["areas"] = areas
    points = [
        {"type": "破裂压力点", "x": Column[0], "x1": 0, "y": Row[0]},
        {"type": "停泵压力点", "x": 1, "x1": 0, "y": 2},
        {"type": "平均砂浓度", "x": 11, "x1": 25, "y": 20},
        {"type": "主体施工排量", "x": 11, "x1": 25, "y": 12}
    ]
    jo["points"] = points

    #js = json.dumps(jo)
    return jo
    #ha.disp_obj(ImageRGB, WindowHandle)
    #
    #ha.wait_seconds(5)

#halcon_circle(r'E:\Source\Gitee\python2021\2021\202110\halcon\现场照片\02.png')



def halcon_circle12(uploadpath):
    print('web路径：', uploadpath)
    Image = ha.read_image(uploadpath)
    Width, Height = ha.get_image_size(Image)

    ImageZoom = ha.zoom_image_size(Image, 512, 320, 'constant')
    ImageConverted = ha.convert_image_type(ImageZoom, 'real')
    ImageScaled = ha.scale_image(ImageConverted, 1, -127)

    # 构造识别参数
    DLSampleInference = ha.create_dict()
    ha.set_dict_object(ImageConverted, DLSampleInference, 'image')

    print('DLModelHandle: ' + str(DLModelHandle))
    print('DLSampleInference: ' + str(DLSampleInference))
    # 应用识别参数
    outputs = []
    DLResult = ha.apply_dl_model(DLModelHandle, DLSampleInference, outputs)

    # 获取识别结果
    row1 = ha.get_dict_tuple(DLResult, 'bbox_row1')
    col1 = ha.get_dict_tuple(DLResult, 'bbox_col1')
    row2 = ha.get_dict_tuple(DLResult, 'bbox_row2')
    col2 = ha.get_dict_tuple(DLResult, 'bbox_col2')
    class_id = ha.get_dict_tuple(DLResult, 'bbox_class_id')
    confidence = ha.get_dict_tuple(DLResult, 'bbox_confidence')

    count = len(confidence)
    Red, Green, Blue = ha.decompose3(Image)
    ImageResult1, ImageResult2, ImageResult3 = ha.trans_from_rgb(Red, Green, Blue, 'hsv')

    flag0 = False
    flag1 = False
    colors = [100, 200]
    for i in range(count):
        if class_id[i] == 0:
            if (flag0):
                continue
            else:
                flag0 = True
                color = colors[0]
        if class_id[i] == 1:
            if (flag1):
                continue
            else:
                flag1 = True
                color = colors[1]
        # 坐标转换
        row11 = row1[i] * Height[0] / 320
        col11 = col1[i] * Width[0] / 512
        row21 = row2[i] * Height[0] / 320
        col21 = col2[i] * Width[0] / 512
        Rectangle = ha.gen_rectangle1(row11, col11, row21, col21)

        Area, Row, Column = ha.area_center(Rectangle)

        Circle = ha.gen_circle(Row[0], Column[0], 10)
        Circle1 = ha.gen_circle(Row[0], Column[0], 20)
        mark = ha.difference(Circle1, Circle)
        # 准备画圈圈
        ImageResult1 = ha.paint_region(mark, ImageResult1, color, 'fill')
        ImageResult2 = ha.paint_region(mark, ImageResult2, 255, 'fill')
        ImageResult3 = ha.paint_region(mark, ImageResult3, 255, 'fill')
    ImageRed, ImageGreen, ImageBlue = ha.trans_to_rgb(ImageResult1, ImageResult2, ImageResult3, 'hsv')
    ImageRGB = ha.compose3(ImageRed, ImageGreen, ImageBlue, )

    picName = uploadpath.split('\\')[-1]

    newurl = r'http://nas.clearmediatech.com:8888/static/images/' + picName[:-4] + '_circle.png'
    basepath = os.path.dirname(__file__)
    newpath = os.path.join(basepath, 'static\images', picName[:-4] + '_circle.png')
    ha.write_image(ImageRGB, 'png', 0, newpath)

    jo = {'fid': 1, 'fp': newurl}
    areas = [
        {"type": "前置液阶段", "x1": 0, "x2": 10},
        {"type": "携砂液阶段1", "x1": 20, "x2": 25},
        {"type": "暂堵转向阶段", "x1": 25, "x2": 30},
        {"type": "携砂液阶段2", "x1": 30, "x2": 35},
        {"type": "顶替液阶段", "x1": 35, "x2": 40}
    ]
    jo["areas"] = areas
    points = [
        {"type": "破裂压力点", "x": Column[0], "x1": 0, "y": Row[0]},
        {"type": "停泵压力点", "x": 1, "x1": 0, "y": 2},
        {"type": "平均砂浓度", "x": 11, "x1": 25, "y": 20},
        {"type": "主体施工排量", "x": 11, "x1": 25, "y": 12}
    ]
    jo["points"] = points

    # js = json.dumps(jo)
    return jo



#设置工作互斥量。多线程
_1_S0 = threading.Semaphore(0)
#工单完成互斥量
_1_S1 = threading.Semaphore(0)
_1_path = 'None'
_1_jo = None

def ReleaseS0():
    _1_S0.release()
    print('S0 released!!!')
def AcquireS1():
    print('S1 acquiring....')
    _1_S1.acquire()
    print('S1 acquired!')

def SetPath(path):
    global _1_path
    _1_path = path

def GetJo():
    return _1_jo

def mywork(arg):
    global _1_path
    global _1_jo
    global _1_S0
    global _1_S1
    basepath = os.path.dirname(__file__)
    modelFile = os.path.join(basepath, 'static\model','model_best.hdl')
    DLModelHandle = ha.read_dl_model(modelFile)
    ha.set_dl_model_param(DLModelHandle, 'batch_size', 1)
    ha.set_dl_model_param(DLModelHandle, 'runtime', 'cpu')
    print('Initialized!!!')
    while(True):
        #等待设置工作
        print('S0 acquiring...')
        _1_S0.acquire()
        #工作已设置，标记工单工作中
        if len(_1_path)>10:
            #_1_jo = halcon_circle2(_1_path)
            uploadpath = _1_path
            print('web路径：', uploadpath)
            Image = ha.read_image(uploadpath)
            Width, Height = ha.get_image_size(Image)

            ImageZoom = ha.zoom_image_size(Image, 512, 320, 'constant')
            ImageConverted = ha.convert_image_type(ImageZoom, 'real')
            ImageScaled = ha.scale_image(ImageConverted, 1, -127)

            # 构造识别参数
            DLSampleInference = ha.create_dict()
            ha.set_dict_object(ImageConverted, DLSampleInference, 'image')

            print('DLModelHandle: ' + str(DLModelHandle))
            print('DLSampleInference: ' + str(DLSampleInference))
            # 应用识别参数
            outputs = []
            DLResult = ha.apply_dl_model(DLModelHandle, DLSampleInference, outputs)

            # 获取识别结果
            row1 = ha.get_dict_tuple(DLResult, 'bbox_row1')
            col1 = ha.get_dict_tuple(DLResult, 'bbox_col1')
            row2 = ha.get_dict_tuple(DLResult, 'bbox_row2')
            col2 = ha.get_dict_tuple(DLResult, 'bbox_col2')
            class_id = ha.get_dict_tuple(DLResult, 'bbox_class_id')
            confidence = ha.get_dict_tuple(DLResult, 'bbox_confidence')

            count = len(confidence)
            Red, Green, Blue = ha.decompose3(Image)
            ImageResult1, ImageResult2, ImageResult3 = ha.trans_from_rgb(Red, Green, Blue, 'hsv')

            flag0 = False
            flag1 = False
            flag_is_0 = False
            x0 = -1
            y0 = -1
            x1 = -1
            y1 = -1
            colors = [100, 200]
            for i in range(count):
                if class_id[i] == 0:
                    if (flag0):
                        continue
                    else:
                        flag0 = True
                        color = colors[0]
                        flag_is_0 = True
                if class_id[i] == 1:
                    if (flag1):
                        continue
                    else:
                        flag1 = True
                        color = colors[1]
                # 坐标转换
                row11 = row1[i] * Height[0] / 320
                col11 = col1[i] * Width[0] / 512
                row21 = row2[i] * Height[0] / 320
                col21 = col2[i] * Width[0] / 512
                Rectangle = ha.gen_rectangle1(row11, col11, row21, col21)

                Area, Row, Column = ha.area_center(Rectangle)

                if(flag_is_0):
                    x0 = Column[0]
                    y0 = Row[0]
                else:
                    x1 = Column[0]
                    y1 = Row[0]
                Circle = ha.gen_circle(Row[0], Column[0], 10)
                Circle1 = ha.gen_circle(Row[0], Column[0], 20)
                mark = ha.difference(Circle1, Circle)
                # 准备画圈圈
                ImageResult1 = ha.paint_region(mark, ImageResult1, color, 'fill')
                ImageResult2 = ha.paint_region(mark, ImageResult2, 255, 'fill')
                ImageResult3 = ha.paint_region(mark, ImageResult3, 255, 'fill')
            ImageRed, ImageGreen, ImageBlue = ha.trans_to_rgb(ImageResult1, ImageResult2, ImageResult3, 'hsv')
            ImageRGB = ha.compose3(ImageRed, ImageGreen, ImageBlue, )

            picName = uploadpath.split('\\')[-1]

            newurl = r'http://nas.clearmediatech.com:8888/static/images/' + picName[:-4] + '_circle.png'
            basepath = os.path.dirname(__file__)
            newpath = os.path.join(basepath, 'static\images', picName[:-4] + '_circle.png')
            ha.write_image(ImageRGB, 'png', 0, newpath)

            jo = {'fid': 1, 'fp': newurl}
            areas = [
                {"type": "前置液阶段", "x1": 0, "x2": 10},
                {"type": "携砂液阶段1", "x1": 20, "x2": 25},
                {"type": "暂堵转向阶段", "x1": 25, "x2": 30},
                {"type": "携砂液阶段2", "x1": 30, "x2": 35},
                {"type": "顶替液阶段", "x1": 35, "x2": 40}
            ]
            jo["areas"] = areas
            points = [
                {"type": "破裂压力点", "x": x0, "x1": 0, "y": y0},
                {"type": "停泵压力点", "x": x1, "x1": 0, "y": y1},
                {"type": "平均砂浓度", "x": 11, "x1": 25, "y": 20},
                {"type": "主体施工排量", "x": 11, "x1": 25, "y": 12}
            ]
            jo["points"] = points

            _1_jo = jo

            _1_S1.release(1)
            print('S1 realeased!!')

thread_started = False

def StartThread():
    global  thread_started
    if not thread_started:
        thread_started = True
        thread = threading.Thread(target=mywork, args = ('',))
        thread.start()

StartThread()
# def runatonce():
#     r = self.halcon_circle2(r'D:\Python\python2021\2021\202110\halconweb\upload\static\images\test1_upload.png')
#     print(r)
#     r = self.halcon_circle2(r'D:\Python\python2021\2021\202110\halconweb\upload\static\images\test2_upload.png')
#     print(r)
#     print('DL Initialized')

#@staticmethod

#DLModelHandle = ha.read_dl_model(r'D:\Python\python2021\2021\202110\halconweb\框框训练结果\model_best.hdl')


class MyDeepLearning1666:

    def __init__(self):
        global DLModelHandle

        print('Initialized!!!')

    @staticmethod
    def halcon_circle2(uploadpath):
        global DLModelHandle
        ha.set_dl_model_param(DLModelHandle, 'batch_size', 1)
        ha.set_dl_model_param(DLModelHandle, 'runtime', 'cpu')
        print('web路径：', uploadpath)
        Image = ha.read_image(uploadpath)
        Width, Height = ha.get_image_size(Image)

        ImageZoom = ha.zoom_image_size(Image, 512, 320, 'constant')
        ImageConverted = ha.convert_image_type(ImageZoom, 'real')
        ImageScaled = ha.scale_image(ImageConverted, 1, -127)

        # 构造识别参数
        DLSampleInference = ha.create_dict()
        ha.set_dict_object(ImageConverted, DLSampleInference, 'image')

        print('DLModelHandle: ' + str(DLModelHandle))
        print('DLSampleInference: ' + str(DLSampleInference))
        # 应用识别参数
        outputs = []
        DLResult = ha.apply_dl_model(DLModelHandle, DLSampleInference, outputs)

        # 获取识别结果
        row1 = ha.get_dict_tuple(DLResult, 'bbox_row1')
        col1 = ha.get_dict_tuple(DLResult, 'bbox_col1')
        row2 = ha.get_dict_tuple(DLResult, 'bbox_row2')
        col2 = ha.get_dict_tuple(DLResult, 'bbox_col2')
        class_id = ha.get_dict_tuple(DLResult, 'bbox_class_id')
        confidence = ha.get_dict_tuple(DLResult, 'bbox_confidence')

        count = len(confidence)
        Red, Green, Blue = ha.decompose3(Image)
        ImageResult1, ImageResult2, ImageResult3 = ha.trans_from_rgb(Red, Green, Blue, 'hsv')

        flag0 = False
        flag1 = False
        colors = [100, 200]
        for i in range(count):
            if class_id[i] == 0:
                if (flag0):
                    continue
                else:
                    flag0 = True
                    color = colors[0]
            if class_id[i] == 1:
                if (flag1):
                    continue
                else:
                    flag1 = True
                    color = colors[1]
            # 坐标转换
            row11 = row1[i] * Height[0] / 320
            col11 = col1[i] * Width[0] / 512
            row21 = row2[i] * Height[0] / 320
            col21 = col2[i] * Width[0] / 512
            Rectangle = ha.gen_rectangle1(row11, col11, row21, col21)

            Area, Row, Column = ha.area_center(Rectangle)

            Circle = ha.gen_circle(Row[0], Column[0], 10)
            Circle1 = ha.gen_circle(Row[0], Column[0], 20)
            mark = ha.difference(Circle1, Circle)
            # 准备画圈圈
            ImageResult1 = ha.paint_region(mark, ImageResult1, color, 'fill')
            ImageResult2 = ha.paint_region(mark, ImageResult2, 255, 'fill')
            ImageResult3 = ha.paint_region(mark, ImageResult3, 255, 'fill')
        ImageRed, ImageGreen, ImageBlue = ha.trans_to_rgb(ImageResult1, ImageResult2, ImageResult3, 'hsv')
        ImageRGB = ha.compose3(ImageRed, ImageGreen, ImageBlue, )

        picName = uploadpath.split('\\')[-1]

        newurl = r'http://nas.clearmediatech.com:8888/static/images/' + picName[:-4] + '_circle.png'
        basepath = os.path.dirname(__file__)
        newpath = os.path.join(basepath, 'static\images', picName[:-4] + '_circle.png')
        ha.write_image(ImageRGB, 'png', 0, newpath)

        jo = {'fid': 1, 'fp': newurl}
        areas = [
            {"type": "前置液阶段", "x1": 0, "x2": 10},
            {"type": "携砂液阶段1", "x1": 20, "x2": 25},
            {"type": "暂堵转向阶段", "x1": 25, "x2": 30},
            {"type": "携砂液阶段2", "x1": 30, "x2": 35},
            {"type": "顶替液阶段", "x1": 35, "x2": 40}
        ]
        jo["areas"] = areas
        points = [
            {"type": "破裂压力点", "x": Column[0], "x1": 0, "y": Row[0]},
            {"type": "停泵压力点", "x": 1, "x1": 0, "y": 2},
            {"type": "平均砂浓度", "x": 11, "x1": 25, "y": 20},
            {"type": "主体施工排量", "x": 11, "x1": 25, "y": 12}
        ]
        jo["points"] = points

        # js = json.dumps(jo)
        return jo
#MyDeepLearning.getInstance()