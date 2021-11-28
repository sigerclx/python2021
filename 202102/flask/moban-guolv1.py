from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', input = 123)

def increase(input):
    output = input + 1
    return output
app.add_template_filter(increase, 'increase1')

@app.template_filter('decrease1')
def decrease(input):
    output = input - 1
    return output


if __name__ == '__main__':
    app.run(port = 80,debug = True)