from flask import Flask, render_template, redirect, request, session
from data import Articles
import pymysql
from passlib.hash import sha256_crypt
from functools import wraps
app = Flask(__name__)
#articles = Articles()

db = pymysql.connect(
    host='localhost', 
    user='root', 
    password='1234', 
    db='gangnam',
    charset='utf8mb4')

cur = db.cursor()

def is_loged_in(f):
    @wraps(f)
    def _wraps(*argrs,**kwargs):
        if 'is_loged' in session:
            return f(*argrs,**kwargs)
        else:
            return redirect('/login')
    return _wraps

@app.route('/register',methods = ["GET","POST"])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        password = sha256_crypt.encrypt(password)
        #print(password_1)
        #print(sha256_crypt.verify("1234", password_1))
        sql = f"SELECT email FROM users WHERE email ='{email}'"
        cur.execute(sql)
        db.commit()
        user_email = cur.fetchone()
        print (email)
        if user_email == None:
            query = f"INSERT INTO users (name, email, username, password) VALUES('{name}','{email}','{username}','{password}')"
            cur.execute(query)
            db.commit()
            return redirect('/login')
        else:
            return render_template('register.html')
    else:
        return render_template('register.html')

@app.route('/login',methods = ["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        print(email,password)
        query = f"SELECT * FROM users WHERE email = '{email}'"
        cur.execute(query)
        db.commit()
        user = cur.fetchone()
        if user == None:
            return redirect('/login')
        else:
            if sha256_crypt.verify(password,user[4]):
                session['is_loged'] = True
                session['email'] = user[2]
                session['username'] = user[3]
                return redirect('/')
            else:
                return redirect('/login')
    else:
        return render_template("login.html")


@app.route('/', methods=['GET' , 'POST'])
def hello_world():
    return render_template('home.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/about',methods=['GET' , 'POST'])
@is_loged_in
def about():
    print(session['username'])
    return render_template('about.html')

@app.route('/admin')
def admin():
    query = "SELECT * FROM users"
    cur.execute(query)
    db.commit()
    users = cur.fetchall()
    print (users)
    return render_template('admin.html', users=users)

@app.route('/admin/<id>/delete')
@is_loged_in
def delete_user(id):
    query = f'DELETE FROM `gangnam`.`users` WHERE `id` = {id}'

    cur.execute(query)
    db.commit()

    return redirect('/admin')
    article = cur.fetchall()

@app.route('/articles',methods=['Get' , 'POST'])
@is_loged_in
def articles():
    
    query = "SELECT * FROM topic"
    cur.execute(query)
    db.commit()

    articles = cur.fetchall()
    print (articles)
    return render_template('articles.html', articles = articles)

@app.route('/article/<id>',methods=['Get' , 'POST'])
@is_loged_in
def article(id):

    query = f"SELECT * FROM topic where id = {id}"
    cur.execute(query)
    db.commit()
    article = cur.fetchall()
    print(article)
    if article == None:
        return redirect('/acticles')
    else:
        return render_template('article.html',article = article[0])
'''
    if (len(articles)) >= int(id):
        article = articles[int(id)-1]
        return render_template('article.html',article = article)
    else:
        return render_template('article.html',article = "No Data")  
'''

@app.route('/add_article', methods=['GET','POST'])
@is_loged_in
def add_article():
    cur = db.cursor()
    
    if request.method == "POST":
        title = request.form['title']
        description = request.form['description']
        author = request.form['author']

        query = "INSERT INTO `topic` (`title`, `description`, `author`) VALUES (%s, %s, %s);"
        input_data = [title,description,author]
        cur.execute(query, input_data)
        db.commit()
        return redirect("/articles")
    else:
        return render_template('add_article.html')

    return "SECESS"

@app.route('/articles/<id>/delete')
@is_loged_in
def delete_article(id):
    query = f'DELETE FROM `gangnam`.`topic` WHERE `id` = {id}'

    cur.execute(query)
    db.commit()

    return redirect('/articles')
    article = cur.fetchall()

@app.route('/articles/<id>/edit', methods = ['GET','POST'])
@is_loged_in
def edit_article(id):
    if request.method == "POST":
        title = request.form['title']
        description = request.form['description']
        author = request.form['author']
        print(title, description,author)
        query = f"UPDATE gangnam.topic SET  title='{title}',description= '{description}' ,author='{author}' WHERE id = {id};"
        cur.execute(query)
        db.commit()

        return redirect('/articles')
        #return "SECESS"
    else:
        print("ZZZ")
        query = f'SELECT * FROM topic where id = {id}'
        cur.execute(query)
        db.commit()

        article = cur.fetchone()

        return render_template('edit_article.html', article = article)



if __name__ == '__main__':
    app.secret_key = "gangnamsmart"
    app.run(port = 5000, debug = True ) 
