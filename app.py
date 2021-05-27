from flask import Flask
from flask.templating import render_template

app = Flask(__name__)
app.debug = True

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    return render_template('home.html')

@app.route('/about', methods = ['GET', 'POST'])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(port = 5000)