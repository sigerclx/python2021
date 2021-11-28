from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from datetime import timedelta
import os

# 本程序功能：是自建一个web站，可以上传图片到static/images目录中
# 可用pyinstaller -F FlaskServer.py 生成EXE。单独运行. 但是要拷贝templates 目录里文件和static/images ，构成一个完整的站点
app = Flask(__name__)

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
            return jsonify({"error": 1001, "msg": "支持图片类型：png、PNG、jpg、JPG、bmp"})
        # 当前文件所在路径
        basepath = os.path.dirname(__file__)
        # 一定要先创建该文件夹，不然会提示没有该路径
        upload_path = os.path.join(basepath, 'static/images', secure_filename(f.filename))
        # 保存文件
        f.save(upload_path)
        # 返回上传成功界面
        return render_template('upload_ok.html')
    # 重新返回上传界面
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(host="127.0.0.1")