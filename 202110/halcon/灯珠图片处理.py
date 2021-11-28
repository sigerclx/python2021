import halcon as ha
# 本程序实现灯珠抠图的功能，抠出来保存到一个新的文件夹中
ImageFiles = ha.list_files ('E:/Source/Gitee/halcon/202110/灯珠抠图/crack1', ['files','follow_links'])
ImageFiles = ha.tuple_regexp_select (ImageFiles, ['\\.(tif|tiff|gif|bmp|jpg|jpeg|jp2|png|pcx|pgm|ppm|pbm|xwd|ima|hobj)$','ignore_case'])
i=0
for eachimg in ImageFiles:
    i+=1
    Image = ha.read_image(eachimg)
    ROI_0 = ha.gen_circle( 1045.5, 1441.5, 399.299)
    ImageReduced = ha.reduce_domain(Image, ROI_0)
    ImagePart = ha.crop_domain(ImageReduced)
    path = r'E:/Source/Gitee/halcon/202110/灯珠抠图/处理好/ok1/' + str(i)
    ha.write_image(ImagePart, 'bmp', 0, path)
