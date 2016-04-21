# all the imports
from flask import Flask, render_template, redirect, request, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
from sqlalchemy import Column, Integer, Text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///picfood.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(Text, unique=True)
    password = Column(Text, unique=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()


api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(User, methods=['GET', 'POST', 'DELETE', 'PUT'])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        _username = request.form['username']
        _password = request.form['password']
        if db.session.query(User).filter(User.username == _username).scalar() is None:
            new_user = User(_username, _password)
            db.session.add(new_user)
            db.session.commit()
            return redirect("http://localhost:5000/login")
        else:
            error = "That Username is Already Taken!"
            return render_template('signup.html', error=error)
    return render_template('signup.html', error=error)


# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    print User.query.all()
    if request.method == 'POST':
        if User.query.filter(User.username == request.form['username'],
                                         User.password == request.form['password']).count():
            session['username'] = request.form['username']
            session['password'] = request.form['password']
            return redirect(url_for('picfood'))
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/picfood', methods=['GET', 'POST'])
def picfood():
    if session.get('username'):
        return render_template('picfood.html')
    else:
        return redirect(url_for('index'))

@app.route('/myaccount')
def myaccount():
    if session.get('username'):
        return render_template('myaccount.html')
    else:
        return redirect(url_for('index'))

app.debug = True
app.secret_key = 'n81\x01\x18\xe3s\x86\x9d:\x01\xade\x00\x0f\x11/\xe37\x0c9O\xb3\xb0'
if __name__ == '__main__':
    app.run()
