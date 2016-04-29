# all the imports
from flask import Flask, render_template, redirect, request, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
from sqlalchemy import Column, Integer, Text
import re
import query

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///picfood.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(Text, unique=True)
    password = Column(Text, unique=False)
    user_preference = Column(Text, unique=False)

    def __init__(self, username, password, user_preference):
        self.username = username
        self.password = password
        self.user_preference = user_preference

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
            new_user = User(_username, _password, " ")
            db.session.add(new_user)
            db.session.commit()
            session['username'] = _username
            session['password'] = _password
            return redirect(url_for('myaccount'))
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
    user = User.query.filter(User.username == session['username']).first()
    session['user_preference'] = str(user.user_preference)
    if session.get('username'):
        return render_template('picfood.html')
    else:
        return redirect(url_for('index'))


@app.route('/algorithm')
def algorithm():
    username = request.args.get('username', 0, type=str)
    password = request.args.get('password', 0, type=str)
    pref = request.args.get('preferences', 0, type=str)
    query_string = request.args.get('query', 0, type=str)
    preferences = pref.split(';')
    results = query.query_pic_food(username, password, preferences, query_string)
    return jsonify(results)


@app.route('/myaccount', methods=['GET', 'POST'])
def myaccount():
    user = User.query.filter(User.username == session['username']).first()
    session['user_preference'] = re.sub(';', ',', str(user.user_preference))
    if session.get('username'):
        if request.method == 'POST':
            user = User.query.filter(User.username == session['username']).first()
            request_string = request.form['user_preference']
            if request_string not in str(user.user_preference):
                if user.user_preference == " " or user.user_preference is None:
                    user.user_preference = request_string
                else:
                    user.user_preference = str(user.user_preference) + "; " + request_string
                user.user_preference = re.sub('None', '', str(user.user_preference))
            db.session.commit()
            return redirect(url_for('myaccount'))
        return render_template('myaccount.html')
    else:
        return redirect(url_for('index'))

app.debug = True
app.secret_key = 'n81\x01\x18\xe3s\x86\x9d:\x01\xade\x00\x0f\x11/\xe37\x0c9O\xb3\xb0'
if __name__ == '__main__':
    app.run()
