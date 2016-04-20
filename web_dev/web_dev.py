# all the imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
from sqlalchemy import Column,Integer, Text


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///picfood.db'
db=SQLAlchemy(app)


class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(Text, unique= True)
    password = Column(Text, unique= False)

db.create_all()

api_manager = APIManager(app,flask_sqlalchemy_db=db)
api_manager.create_api(User, methods=['GET', 'Post', 'DELETE', 'PUT'])

@app.route('/')
def index():
    return app.send_static_file('index.html')

app.debug=True

if __name__ == '__main__':
    app.run()
