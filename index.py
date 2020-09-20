from flask import Flask, render_template, request, url_for
from pymongo import MongoClient
import datetime, pprint, os

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.test_database
collection = db.test_collection

@app.route("/hello")
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

"""@app.route('/insert', methods=['GET', 'POST'])
def insert():
    post = {"author": "Mike", "text": "My first blog post!"}
    post_id = collection.insert_one(post).inserted_id
    return str(post_id)

@app.route('/find_one', methods=['GET'])
def find_one():

    pprint.pprint(collection.find_one())
    return str(collection.find_one())"""

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method =="POST":
        f = request.files['fileToUpload']
        f.save('static/' + f.name)
        return "post"
    else:
        return render_template('upload.html')

@app.route('/gallery', methods=['GET'])
def gallery():
    path = "static"
    images = os.listdir(path)
    url_for('static', filename='style.css')
    images = [url_for('static', filename=f) for f in images if os.path.isfile(os.path.join(path, f))]
    print(images)
    return render_template('gallery.html', images=images)
