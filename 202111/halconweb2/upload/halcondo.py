import halcon as ha
import os
import threading
import requests
#import Hdevengine as hdev
# 本程序实现灯珠抠图的功能，抠出来保存到一个新的文件夹中
from globalValue import Set_value,Get_value



def halcon_circle1(uploadpath):
    print('Initialized!!!')


    #nonlocal DLModelHandle
    ha.set_dl_model_param(Get_value('dl'), 'batch_size', 1)
    ha.set_dl_model_param(Get_value('dl'), 'runtime', 'cpu')
    print('web路径：', uploadpath)
    Image = ha.read_image(uploadpath)
    Width, Height = ha.get_image_size(Image)

    ImageZoom = ha.zoom_image_size(Image, 512, 320, 'constant')
    ImageConverted = ha.convert_image_type(ImageZoom, 'real')
    ImageScaled = ha.scale_image(ImageConverted, 1, -127)

    # 构造识别参数
    DLSampleInference = ha.create_dict()
    ha.set_dict_object(ImageConverted, DLSampleInference, 'image')

    print('DLModelHandle: ' + str(Get_value('dl')))
    print('DLSampleInference: ' + str(DLSampleInference))
    # 应用识别参数
    outputs = []
    DLResult = ha.apply_dl_model(Get_value('dl'), DLSampleInference, outputs)

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


def halcon_circle():
    basepath = os.path.dirname(__file__)
    modelFile = os.path.join(basepath, 'static\model', 'model_best.hdl')
    DLModelHandle = ha.read_dl_model(modelFile)


    print('Initialized!!!')

    def in_halcon_circle(uploadpath):
        #nonlocal DLModelHandle
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

    return in_halcon_circle

#currentfunc = halcon_circle()




class MyDeepLearning:

    def __init__(self):
        pass

    def halcon_circle2(self,uploadpath):
        basepath = os.path.dirname(__file__)
        modelFile = os.path.join(basepath, 'static\model', 'model_best.hdl')
        DLModelHandle = ha.read_dl_model(modelFile)
        ha.set_dl_model_param(DLModelHandle, 'batch_size', 1)
        ha.set_dl_model_param(DLModelHandle, 'runtime', 'cpu')
        print('Initialized!!!')

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
