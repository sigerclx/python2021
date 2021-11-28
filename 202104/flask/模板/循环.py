from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def disp_names():
    names = {"jacky","tom","xiuly"}
    return render_template("circle.html",names=names )

if __name__ == '__main__':
    app.run(debug=True)
