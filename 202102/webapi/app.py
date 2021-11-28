#!flask/bin/python
from flask import Flask, jsonify,abort
from flask import make_response

app = Flask(__name__)

tasks = [
        {
            'id': 1,
            'title': u'Buy groceries',
            'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
            'done': False
        },
        {
            'id': 2,
            'title': u'Learn Python',
            'description': u'Need to find a good Python tutorial on the web',
            'done': False
        }
    ]

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):

    task = filter(lambda t: t['id'] == task_id, tasks)
    if (len(list(task))==0):
        abort(404)

    #if len(list(task)) == 0:
    #    abort(404)
    return jsonify({'task': tasks[task_id-1]})
    #return jsonify({'task': str(list[task])})

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'ID Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True,host='192.168.0.61',port=5000)