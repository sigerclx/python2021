# 运行指令：
# flaskOne>set FLASK_APP=web.py
# flaskOne>flask run
<<<<<<< HEAD
from app import create_app,db
from app.models import User, Post,Reimbursement

<<<<<<< HEAD
app = create_app()
#@app.shell_context_processor
=======
=======
from app import app, db
from app.models import User, Post

>>>>>>> parent of de53fed6 (flask报销系统的分页及bootstrap)
@app.shell_context_processor
>>>>>>> parent of de53fed6 (flask报销系统的分页及bootstrap)
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post,'Reimbursement':Reimbursement}

# if __name__ == '__main__':
#
#     app.run(host='0.0.0.0',debug=True,port=5003)
