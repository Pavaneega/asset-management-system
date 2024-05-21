from flask import Flask,redirect,render_template,request,url_for
from flask_pymongo import MongoClient
import json
from bson import ObjectId
import pymongo


app = Flask(__name__)

client = MongoClient('localhost', 27017)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content':content,'degree':degree})
        return redirect(url_for('index'))
    all_todos = todos.find()
    return  render_template('index.html',todos=all_todos)
@app .post("/<id>/delete/")
def delete(id):
    todos.delete_one({"_id":ObjectId(id)})
    return redirect(url_for('index'))

db = client.flask_database
todos = db.todos
 
if __name__=='__main__':
    app.run(debug=True)