'''
虎课网 flask教程第二遍学习
本次例子，演示了注册用户，login.html模版里使用了js，
<!--{{ form.submit(class = "querybtn",onclick="ajaxForm()") }}--><!--这里如果用这个会造成表单提交两次，而且第二次是get会刷新页面-->
所以使用了现有login.html里的点击按钮调用函数ajaxForm（）的形式
给后台API提交的是json ，异步返回的也是json，
在JS中
success:function(rtn){
                    $('#result').text(rtn.message) }

rtn 是 '/registuser' 返回的json ，可以随意命名，而message是对应JSON的key

针对 form 的 application/x-www-form-urlencoded 是默认提交方式可获取数据，如果需要提交json，则提交方式要改为：application/json形式
如下：

$.ajax({
                url:"registuser",
                type:"POST",
                data:JSON.stringify($('form').serializeObject()),
                contentType:"application/json",  //缺失会出现URL编码，无法转成json对象
                success:function(rtn){
                    $('#result').text(rtn.message)
                }
            });

上例的rtn 是webAPI registuser 返回的json ，message 是对应的key
'''

from flask import Flask,jsonify,request,render_template
app = Flask(__name__)

user_list = [
    {
        'username':'abc',
        'password':'abc'
    },
    {
        'username':'123',
        'password':'123'
    }
]

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/reg',methods=['GET'])
def reg():
    return render_template('login.html')
    # return render_template('login.html')

@app.route('/userlist',methods=['GET'])
def get_users():
    return jsonify(user_list)

@app.route('/registuser',methods=['POST'])
def create_user():
    user = request.get_json()
    if user['username']:
        print(user)
        user_list.append(user)
        return jsonify({
            'message': 'user created'
        })
    else:
        return jsonify({
            'message': '请输入用户信息'
        })
    # username = request.form['username'] # 针对 form 的 application/x-www-form-urlencoded 默认提交方式可获取数据，对提交application/json形式无效
    # password = request.form['password']
    #
    # print('username=',request.args.get('username')) # 针对 form 的 application/x-www-form-urlencoded 默认提交方式，对json无效





if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5000)
