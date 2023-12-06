## Start at "Handle the form submit and create new todo items"

from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
import certifi
from datetime import timezone, datetime

ca = certifi.where()

app = Flask(__name__)
uri = "mongodb+srv://dbUSer:fgzgzNrEMHOvh5P1@marcodominicanu.bspya9y.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, tlsCAFile=ca)

db = client.flask_final_db
todos = db.todos

@app.route('/', methods=('GET', 'POST'))
def index():
    """Homepage displaying a form for new todos, and a list of exisiting todos"""
    if request.method=='POST':
        content = request.form['content']
        priority = request.form['priority']
        current_date = datetime.now(timezone.utc)
        formatted_date = current_date.strftime('%B %d %Y')
        todos.insert_one({'content': content, 'priority': priority, 'complete': False, 'date': formatted_date})
        return redirect(url_for('index'))

    all_todos = todos.find().collation({'locale': 'en'}).sort('priority')

        
    context = {
        'todos': all_todos
    }
    return render_template('index.html', **context)

@app.post('/<id>/complete/')
def complete(id):
    """Updates todo with complete if complete button is clicked"""
    filter = { '_id': ObjectId(id) }
    new_values = { '$set': { 'complete': True } }
    todos.update_one(filter, new_values)
    return redirect(url_for('index'))

@app.post('/<id>/delete/')
def delete(id):
    """Deletes todo from database based on objectId"""
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)