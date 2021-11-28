from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def disp():
    name = 'tom'
    age =10
    return render_template("index.html",name=name,age=age)



if __name__ == '__main__':
    app.run(debug='ON')
