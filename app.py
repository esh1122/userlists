from flask import Flask
from flask.templating import render_template
from data import Articles

app = Flask(__name__)
app.debug = True

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    return render_template('home.html')

@app.route('/about', methods = ['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/articles', methods = ['GET', 'POST'])
def articles():
    articles = Articles()
    return render_template('articles.html', articles = articles)

@app.route('/article/<id>', methods = ['GET', 'POST'])
def article():
    articles = Articles()
    article = articles[int(id)-1]
    return render_template('article.html', article = article)

if __name__ == '__main__':
    app.run(port = 5000)