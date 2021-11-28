from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from datetime import timedelta
import os
import json
from halcondo import halcon_circle,halcon_circle1,ReleaseS0,AcquireS1,SetPath,GetJo
from download import downloadfile
from flask_cors import *

# 本程序功能：是自建一个web站，可以上传图片到static/images目录中
# 可用pyinstaller FlaskServer.py 生成EXE。单独运行. 但是要拷贝templates 目录里文件和static/images ，构成一个完整的站点
# 需要用到static/model/model_best.hdl，暂时不上传到gitlee
app = Flask(__name__)
CORS(app, supports_credentials=True,resource=r"/*")  # 设置跨域

# 输出
@app.route('/')
def hello_world():
    return 'Hello World!'

# 设置允许的文件格式
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# 设置静态文件缓存过期时间
app.send_file_max_age_default = timedelta(seconds=1)

# 添加路由
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        # 通过file标签获取文件
        f = request.files['file']
        if not (f and allowed_file(f.filename)):
            return jsonify({"error": 1005, "msg": "支持图片类型：png、PNG、jpg、JPG、bmp"})
        # 当前文件所在路径
        basepath = os.path.dirname(__file__)
        # 一定要先创建该文件夹，不然会提示没有该路径
        upload_path = os.path.join(basepath, 'static/images', secure_filename(f.filename))
        # 保存文件
        f.save(upload_path)
        halcon_circle2(upload_path)
        # 返回上传成功界面
        return render_template('upload_ok.html')
    # 重新返回上传界面
    return render_template('upload.html')


@app.route('/cmprocess.do', methods=['GET'])
def cmprocess_get():
    # 重新返回上传界面
    return jsonify({"error": 1000, "msg": "please use post method!"})

@app.route('/cmprocess.do', methods=['POST'])
def cmprocess():
    jo = request.get_json()
    #print('>>>',jo)
    fid = jo['fid']
    if(fid==1):
        # 参数中的文件路径
        furl = jo['fp']
        picName = furl.split(r'/')[-1]
        #print('准备下载：',picName)
        basepath = os.path.dirname(__file__)
        fp = os.path.join(basepath, 'static\images',picName[:-4]+'_upload'+picName[-4:])
        #print('fp:',fp)

        if downloadfile(furl,fp)==0:
            return jsonify({"error": 1001, "msg": "图片下载错误，请检查url"})
        #print('fp=',fp)

        #jr = halcon_circle2(fp)
        #jr = halcon_circle2(r'D:\Python\python2021\2021\202110\halconweb\upload\static\images\test2_upload.png')
        # runatonce()
        #md = MyDeepLearning.getInstance()
        #jr = md.halcon_circle2(fp)
        #设置新工作
        #_1_path = fp
        #fp = r'D:\Python\python2021\2021\202110\halconweb\upload\static\images\test3_upload.png'
        SetPath(fp)
        ReleaseS0()
        AcquireS1()
        jr = GetJo()
        return jsonify(jr)

    return jsonify({"error": 1002, "msg": "fid未指定"})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8888)

