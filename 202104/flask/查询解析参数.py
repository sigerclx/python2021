from flask import Flask, request
app = Flask(__name__)

# http://localhost:5000/query?name=zhangsan&age=13
# 参数打印在控制台
@app.route('/query')
def query():
    print('name =', request.args['name'])
    print('age =', request.args['age'])
    return 'hello'

if __name__ == '__main__':
    app.run(debug = True)