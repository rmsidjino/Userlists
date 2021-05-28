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

@app.route('/article/<id>',methods=['Get' , 'POST'])
def article(id):
    articles = Articles()
    print(len(articles))
    if (len(articles)) >= int(id):
        article = articles[int(id)-1]
        return render_template('article.html',article = article)
    else:
        return render_template('article.html',article = "No Data")  

@app.route('/add_article', methods=['Get' , 'POST'])
def add_article():
    return render_template('add_article.html')

if __name__ == '__main__':
    app.run(port = 8080, debug = True ) 