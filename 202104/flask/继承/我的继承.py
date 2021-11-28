from flask import Flask, render_template, views
app = Flask(__name__)

class BaseView(views.View):
    def get_template(self):
        raise NotImplementedError()

    def get_data(self):
        raise NotImplementedError()

    def dispatch_request(self):
        data = self.get_data()
        template = self.get_template()
        return render_template(template, **data)  # 双星号是把字典解析成多关键参数

class Userview(BaseView):
    def get_template(self):
        return "user.html"

    def get_data(self):
        users ={"name":'jacky',"age":34}
        return users

app.add_url_rule("/",view_func=Userview.as_view("index"))

app.run(debug=True)
