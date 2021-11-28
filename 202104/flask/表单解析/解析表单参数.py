from flask import Flask, request
app = Flask(__name__)
#点击提交，浏览器将请求 /addUser 发送给服务端，服务端在终端打印输出：

@app.route('/')
def root():
    file = open('表单解析/form.html', encoding ='utf-8')
    return file.read()

@app.route('/addUser', methods = ['POST'])
def check_login():
    name = request.form['name']
    age = request.form['age']
    print('name = %s' % name)
    print('age = %s' % age)
    return 'addUser OK'

if __name__ == '__main__':
    app.run(debug = True)
