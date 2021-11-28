from flask import Flask
app = Flask(__name__)
## 自己写代码实现as_view


class Index:
    def dispatch_request(self):
        return 'hello world！!!!！！123'

    @staticmethod
    def as_view():
        name = Index()
        return name.dispatch_request

app.add_url_rule(rule='/', view_func = Index.as_view())

app.run(debug = True)
