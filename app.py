from flask import Flask
from flask.templating import render_template

app = Flask(__name__)
app.debug = True

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    return render_template('home.html' , data = "김태경")

if __name__ == '__main__':
    app.run(port = 5000)