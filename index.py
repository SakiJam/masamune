from flask import Flask, render_template, request
from pymongo import MongoClient
import datetime, pprint

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.test_database
collection = db.test_collection

@app.route("/hello")
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    post = {"author": "Mike", "text": "My first blog post!"}
    post_id = collection.insert_one(post).inserted_id
    return str(post_id)

@app.route('/find_one', methods=['GET'])
def find_one():
    pprint.pprint(collection.find_one())
    return str(collection.find_one())
