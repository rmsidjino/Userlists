from flask import Flask, render_template
from data import Articles
app = Flask(__name__)
articles = Articles()

@app.route('/', methods=['Get' , 'POST'])
def hello_world():
    return render_template('home.html')

@app.route('/about',methods=['Get' , 'POST'])
def about():
    return render_template('about.html')

@app.route('/articles',methods=['Get' , 'POST'])
def articles():
    return render_template('articles.html', articles = Articles())

if __name__ == '__main__':
    app.run(port = 8080, debug = True ) 