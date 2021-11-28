# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__, static_folder="./",template_folder='./',static_url_path='')  # 实例化app对象

user = 'jacky'
password = 'a1b2/a'
database = 'jingyou'
uri = 'mysql+pymysql://%s:%s@localhost:3306/%s' % (user, password, database)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Tree(db.Model):
    __tablename__ = 'A_tree'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    parentid = db.Column(db.Integer)
    jine = db.Column(db.Float)

    def dump(self):
        print(self.id, self.name, self.parentid,self.jine)

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


@app.route('/', methods=['GET', 'POST'])  # 路由
def test_post():
    file_name = '你好,flask'
    # 把值传给 div 中 data
    trees = Tree.query.all()
    tlist = []
    for tree in trees:
        print(tree.to_json())
        tlist.append(tree.to_json())
    #print(tlist)
    #treevalue = jsonify(tlist)

    #print(type(treevalue))
    treevalue1=json.dumps(tlist)
    print(type(treevalue1))
    #print(treevalue.json())
    #print(json.dumps(treevalue.json(), indent=2, ensure_ascii=False))
    #print(treevalue["parentid"])
    treevalue = ''' 
    {'guan':{ 
            '1':null, 
            '2':{ 
                '21':{
					'211':null,
					'212':null,
					'213':null
				},
                '22':null,
                '23':null
            },
            '3':null
        },
        'sun':{
            's1':null,
            's2':null
        },
        'last':null
    }
    '''
    treevalue=treevalue.replace("\'","\"")
    treevalue2 ='''
    [{'name': '01', 'id': 1, 'child': [{'name': '0101', 'id': 2, 'child': [{'name': '010101', 'id': 5, 'child': []}, {'name': '010102', 'id': 6, 'child': []}, {'name': '010103', 'id': 7, 'child': []}]}, {'name': '0102', 'id': 3, 'child': [{'name': '010201', 'id': 8, 'child': []}]}, {'name': '0103', 'id': 4, 'child': [{'name': '010301', 'id': 9, 'child': [{'name': '01030101', 'id': 10, 'child': []}, {'name': '01030102', 'id': 11, 'child': []}]}]}]}]
    '''
    #print(treevalue)
    return render_template('jsgetdata.html', data=treevalue2)

if __name__ == '__main__':
    app.run(host='127.0.0.1',  # 任何ip都可以访问
            port=7777,  # 端口
            debug=True
            )