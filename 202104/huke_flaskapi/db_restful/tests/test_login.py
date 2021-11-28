import unittest
import json
from db_restful import create_app,db
'''
单元测试命令：2021\202104\huke_flaskapi>python -m unittest discover 
带token的测试部分，没记录代码，具体看虎课视频44集
'''



class TestUser(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name='development')
        self.client = self.app.test_client
        self.user_data  = {
            'username':'jacky',
            'password':'12345',
            'email':'test@126.com'
        }
        with self.app.app_context():
            db.create_all()


    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_login(self):
        url = '/user/{}'.format(self.user_data['username'])
        self.client().post(
            url,
            data=self.user_data
        )
        url ='auth/login'
        res = self.client().post(
            url,
            data=json.dumps({'username':'jacky','password':'12345'}),
            headers = {'Content-Type':'application/json'}
        )
        self.assertEqual(res.status_code, 200)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertIn('access_token',res_data)

        res = self.client().post(
            url,
            data=self.user_data
        )
        self.assertEqual(res.status_code, 200)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertIn(res_data)