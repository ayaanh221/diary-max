import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"]= 'mongodb+srv://ayaanh221:missayaan221@myfirstcluster-lj4yz.mongodb.net/diary-max?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())


@app.route('/add_task')
def add_task():
    
    return render_template('addtask.html',
                           categories=mongo.db.categories.find())

                           
@app.route('/task_recipe')
def recipes():
    return render_template("recipes.html", tasks=mongo.db.tasks.find())
    

@app.route('/insert_task', methods=['POST'])
def insert_task():
   
    tasks = mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))
    
    
    



@app.route('/edit_task/<task_id>')
def edit_task(task_id):
    the_task =  mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('edittask.html', task=the_task,
                           categories=all_categories)

   
   
@app.route('/update_task/<get_tasks>', methods=["POST"])
def update_task(task_id):
    tasks = mongo.db.tasks
    tasks.update( {'_id': ObjectId(task_id)},
    {
       'recipe_name':request.form.get('recipe_name'),
        'photo_link':request.form.get('photo_link'),
        'cooking_time': request.form.get('cooking_time'),
        'ingredients': request.form.get('ingredients'),
        'method': request.form.get('method'),
        'due_date': request.form.get('due_date'),
        'vegetarian':request.form.get('vegetarian')
    })
    return redirect(url_for('get_tasks'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
