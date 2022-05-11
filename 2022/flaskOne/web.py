# 运行指令：
# flaskOne>set FLASK_APP=web.py
# flaskOne>flask run
from app import app, db
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post,'Reimbursement':Reimbursement}

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5003)

#
# from app import create_app, db
# from app.models import User, Post, Message, Notification, Task
#
# app = create_app()
#
#
#
# @app.shell_context_processor
# def make_shell_context():
#     return {'db': db, 'User': User, 'Post': Post, 'Message': Message,
#             'Notification': Notification, 'Task': Task}
