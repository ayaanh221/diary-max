{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":20,"column":62},"end":{"row":20,"column":63},"action":"remove","lines":["@"],"id":506}],[{"start":{"row":20,"column":62},"end":{"row":20,"column":63},"action":"insert","lines":["@"],"id":507}],[{"start":{"row":20,"column":62},"end":{"row":20,"column":63},"action":"remove","lines":["@"],"id":508}],[{"start":{"row":20,"column":62},"end":{"row":20,"column":63},"action":"insert","lines":["@"],"id":509}],[{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"remove","lines":["S"],"id":510}],[{"start":{"row":7,"column":62},"end":{"row":7,"column":63},"action":"remove","lines":["@"],"id":511}],[{"start":{"row":7,"column":62},"end":{"row":7,"column":63},"action":"insert","lines":["@"],"id":512}],[{"start":{"row":19,"column":15},"end":{"row":19,"column":16},"action":"remove","lines":["S"],"id":513}],[{"start":{"row":0,"column":0},"end":{"row":9,"column":20},"action":"remove","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId","","app = Flask(__name__)","app.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"]= 'mongodb+srv://ayaanh221:missayaan221@myfirstcluster-lj4yz.mongodb.net/diary-max?retryWrites=true&w=majority'","","mongo = PyMongo(app)"],"id":514}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":515}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":516}],[{"start":{"row":27,"column":39},"end":{"row":27,"column":41},"action":"remove","lines":["))"],"id":517},{"start":{"row":27,"column":39},"end":{"row":27,"column":78},"action":"insert","lines":[" categories=mongo.db.categories.find())"]}],[{"start":{"row":27,"column":39},"end":{"row":27,"column":40},"action":"insert","lines":[","],"id":518}],[{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"remove","lines":["",""],"id":519}],[{"start":{"row":9,"column":0},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":520}],[{"start":{"row":21,"column":41},"end":{"row":21,"column":42},"action":"remove","lines":[")"],"id":521},{"start":{"row":21,"column":41},"end":{"row":23,"column":0},"action":"insert","lines":[",","                           categories=mongo.db.categories.find())",""]}],[{"start":{"row":29,"column":39},"end":{"row":29,"column":77},"action":"remove","lines":[", categories=mongo.db.categories.find("],"id":522}],[{"start":{"row":32,"column":0},"end":{"row":34,"column":70},"action":"remove","lines":["@app.route('/task_recipe')","def recipes():","    return render_template(\"recipes.html\", task=mongo.db.tasks.find())"],"id":523}],[{"start":{"row":32,"column":0},"end":{"row":34,"column":70},"action":"insert","lines":["@app.route('/task_recipe')","def recipes():","    return render_template(\"recipes.html\", task=mongo.db.tasks.find())"],"id":524}],[{"start":{"row":25,"column":12},"end":{"row":25,"column":13},"action":"remove","lines":["/"],"id":525}],[{"start":{"row":25,"column":12},"end":{"row":25,"column":13},"action":"insert","lines":["/"],"id":526}],[{"start":{"row":25,"column":12},"end":{"row":25,"column":13},"action":"remove","lines":["/"],"id":527}],[{"start":{"row":25,"column":12},"end":{"row":25,"column":13},"action":"insert","lines":["/"],"id":528}],[{"start":{"row":29,"column":29},"end":{"row":29,"column":30},"action":"insert","lines":["/"],"id":529}],[{"start":{"row":29,"column":30},"end":{"row":30,"column":0},"action":"insert","lines":["",""],"id":530},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"remove","lines":["    "],"id":531},{"start":{"row":29,"column":30},"end":{"row":30,"column":0},"action":"remove","lines":["",""]},{"start":{"row":29,"column":29},"end":{"row":29,"column":30},"action":"remove","lines":["/"]}],[{"start":{"row":0,"column":0},"end":{"row":41,"column":23},"action":"remove","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId","","","app = Flask(__name__)","app.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"]= 'mongodb+srv://ayaanh221:missayaan221@myfirstcluster-lj4yz.mongodb.net/diary-max?retryWrites=true&w=majority'","","mongo = PyMongo(app)","","","@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"tasks.html\", task=mongo.db.tasks.find())","","","@app.route('/add_task')","def add_task():","    return render_template('addtask.html',","                           categories=mongo.db.categories.find())","","","@app.route('/insert_task', methods=['POST'])","def insert_task():","    tasks = mongo.db.tasks","    tasks.insert_one(request.form.to_dict())","    return redirect(url_for('get_tasks'))","","","@app.route('/task_recipe')","def recipes():","    return render_template(\"recipes.html\", task=mongo.db.tasks.find())","   ","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":532},{"start":{"row":0,"column":0},"end":{"row":41,"column":23},"action":"insert","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId","","","app = Flask(__name__)","app.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"]= 'mongodb+srv://ayaanh221:missayaan221@myfirstcluster-lj4yz.mongodb.net/diary-max?retryWrites=true&w=majority'","","mongo = PyMongo(app)","","","@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"tasks.html\", task=mongo.db.tasks.find())","","","@app.route('/add_task')","def add_task():","    return render_template('addtask.html',","                           categories=mongo.db.categories.find())","","","@app.route('/insert_task', methods=['POST'])","def insert_task():","    tasks = mongo.db.tasks","    tasks.insert_one(request.form.to_dict())","    return redirect(url_for('get_tasks'))","","","@app.route('/task_recipe')","def recipes():","    return render_template(\"recipes.html\", task=mongo.db.tasks.find())","   ","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"]}],[{"start":{"row":37,"column":0},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":533},{"start":{"row":38,"column":0},"end":{"row":39,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":38,"column":0},"end":{"row":50,"column":0},"action":"insert","lines":["@app.route('/update_task/<task_id>', methods=[\"POST\"])","def update_task(task_id):","    tasks = mongo.db.tasks","    tasks.update( {'_id': ObjectId(task_id)},","    {","        'task_name':request.form.get('task_name'),","        'category_name':request.form.get('category_name'),","        'task_description': request.form.get('task_description'),","        'due_date': request.form.get('due_date'),","        'is_urgent':request.form.get('is_urgent')","    })","    return redirect(url_for('get_tasks'))",""],"id":534}],[{"start":{"row":43,"column":9},"end":{"row":43,"column":18},"action":"remove","lines":["task_name"],"id":535},{"start":{"row":43,"column":9},"end":{"row":44,"column":1},"action":"insert","lines":["recipe_name",":"]}],[{"start":{"row":44,"column":0},"end":{"row":44,"column":1},"action":"remove","lines":[":"],"id":536},{"start":{"row":43,"column":20},"end":{"row":44,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":44,"column":9},"end":{"row":44,"column":22},"action":"remove","lines":["category_name"],"id":537},{"start":{"row":44,"column":9},"end":{"row":45,"column":0},"action":"insert","lines":["photo_Link",""]}],[{"start":{"row":44,"column":19},"end":{"row":45,"column":0},"action":"remove","lines":["",""],"id":538}],[{"start":{"row":45,"column":9},"end":{"row":45,"column":25},"action":"remove","lines":["task_description"],"id":539},{"start":{"row":45,"column":9},"end":{"row":46,"column":0},"action":"insert","lines":["cooking_time",""]}],[{"start":{"row":45,"column":21},"end":{"row":46,"column":0},"action":"remove","lines":["",""],"id":540}],[{"start":{"row":45,"column":61},"end":{"row":46,"column":0},"action":"insert","lines":["",""],"id":541},{"start":{"row":46,"column":0},"end":{"row":46,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":46,"column":8},"end":{"row":48,"column":0},"action":"insert","lines":["","ingredients",""],"id":542}],[{"start":{"row":47,"column":0},"end":{"row":47,"column":1},"action":"insert","lines":["'"],"id":543}],[{"start":{"row":47,"column":12},"end":{"row":47,"column":13},"action":"insert","lines":["'"],"id":544}],[{"start":{"row":46,"column":8},"end":{"row":47,"column":0},"action":"remove","lines":["",""],"id":545}],[{"start":{"row":46,"column":21},"end":{"row":46,"column":60},"action":"insert","lines":[": request.form.get('task_description'),"],"id":546}],[{"start":{"row":49,"column":9},"end":{"row":49,"column":18},"action":"remove","lines":["is_urgent"],"id":547},{"start":{"row":49,"column":9},"end":{"row":49,"column":19},"action":"insert","lines":["vegetarian"]}],[{"start":{"row":49,"column":39},"end":{"row":49,"column":48},"action":"remove","lines":["is_urgent"],"id":548},{"start":{"row":49,"column":39},"end":{"row":49,"column":45},"action":"insert","lines":["switch"]}],[{"start":{"row":48,"column":4},"end":{"row":48,"column":8},"action":"remove","lines":["    "],"id":549},{"start":{"row":48,"column":0},"end":{"row":48,"column":4},"action":"remove","lines":["    "]},{"start":{"row":47,"column":0},"end":{"row":48,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":47,"column":0},"end":{"row":47,"column":1},"action":"insert","lines":[" "],"id":550},{"start":{"row":47,"column":1},"end":{"row":47,"column":2},"action":"insert","lines":[" "]},{"start":{"row":47,"column":2},"end":{"row":47,"column":3},"action":"insert","lines":[" "]},{"start":{"row":47,"column":3},"end":{"row":47,"column":4},"action":"insert","lines":[" "]},{"start":{"row":47,"column":4},"end":{"row":47,"column":5},"action":"insert","lines":[" "]},{"start":{"row":47,"column":5},"end":{"row":47,"column":6},"action":"insert","lines":[" "]},{"start":{"row":47,"column":6},"end":{"row":47,"column":7},"action":"insert","lines":[" "]},{"start":{"row":47,"column":7},"end":{"row":47,"column":8},"action":"insert","lines":[" "]}],[{"start":{"row":47,"column":8},"end":{"row":47,"column":9},"action":"insert","lines":[" "],"id":551}],[{"start":{"row":47,"column":8},"end":{"row":47,"column":9},"action":"remove","lines":[" "],"id":552}],[{"start":{"row":50,"column":29},"end":{"row":50,"column":38},"action":"remove","lines":["get_tasks"],"id":553},{"start":{"row":50,"column":29},"end":{"row":50,"column":35},"action":"insert","lines":["switch"]}],[{"start":{"row":50,"column":28},"end":{"row":50,"column":36},"action":"remove","lines":["'switch'"],"id":554},{"start":{"row":50,"column":28},"end":{"row":50,"column":40},"action":"insert","lines":["/task_recipe"]}],[{"start":{"row":50,"column":40},"end":{"row":50,"column":41},"action":"insert","lines":["'"],"id":555}],[{"start":{"row":50,"column":28},"end":{"row":50,"column":29},"action":"insert","lines":["'"],"id":556}],[{"start":{"row":38,"column":26},"end":{"row":38,"column":33},"action":"remove","lines":["task_id"],"id":557},{"start":{"row":38,"column":26},"end":{"row":38,"column":38},"action":"insert","lines":["/task_recipe"]}],[{"start":{"row":50,"column":28},"end":{"row":50,"column":42},"action":"remove","lines":["'/task_recipe'"],"id":558},{"start":{"row":50,"column":28},"end":{"row":50,"column":39},"action":"insert","lines":["'get_tasks'"]}],[{"start":{"row":38,"column":26},"end":{"row":38,"column":27},"action":"remove","lines":["/"],"id":559}],[{"start":{"row":38,"column":26},"end":{"row":38,"column":37},"action":"remove","lines":["task_recipe"],"id":560},{"start":{"row":38,"column":26},"end":{"row":38,"column":37},"action":"insert","lines":["'get_tasks'"]}],[{"start":{"row":38,"column":36},"end":{"row":38,"column":37},"action":"remove","lines":["'"],"id":561}],[{"start":{"row":38,"column":26},"end":{"row":38,"column":27},"action":"remove","lines":["'"],"id":562}],[{"start":{"row":34,"column":69},"end":{"row":34,"column":70},"action":"remove","lines":[")"],"id":563},{"start":{"row":34,"column":69},"end":{"row":35,"column":0},"action":"insert","lines":["",""]},{"start":{"row":35,"column":0},"end":{"row":35,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":35,"column":4},"end":{"row":35,"column":29},"action":"insert","lines":["print 'Your name is ' + x"],"id":564}],[{"start":{"row":35,"column":29},"end":{"row":35,"column":30},"action":"insert","lines":[")"],"id":565}],[{"start":{"row":35,"column":30},"end":{"row":35,"column":31},"action":"insert","lines":[")"],"id":566}],[{"start":{"row":35,"column":10},"end":{"row":35,"column":11},"action":"insert","lines":["("],"id":567}],[{"start":{"row":35,"column":31},"end":{"row":35,"column":32},"action":"remove","lines":[")"],"id":568}],[{"start":{"row":35,"column":3},"end":{"row":35,"column":31},"action":"remove","lines":[" print ('Your name is ' + x)"],"id":569}],[{"start":{"row":38,"column":0},"end":{"row":39,"column":0},"action":"remove","lines":["",""],"id":570}],[{"start":{"row":39,"column":0},"end":{"row":40,"column":0},"action":"insert","lines":["",""],"id":571}],[{"start":{"row":39,"column":0},"end":{"row":40,"column":0},"action":"remove","lines":["",""],"id":572}],[{"start":{"row":40,"column":0},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":573}],[{"start":{"row":38,"column":56},"end":{"row":39,"column":0},"action":"remove","lines":["",""],"id":574}],[{"start":{"row":38,"column":56},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":575},{"start":{"row":39,"column":0},"end":{"row":40,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":39,"column":0},"end":{"row":40,"column":0},"action":"remove","lines":["",""],"id":576}],[{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"remove","lines":["    "],"id":577},{"start":{"row":40,"column":0},"end":{"row":41,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":40,"column":0},"end":{"row":40,"column":1},"action":"insert","lines":[" "],"id":578}],[{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"remove","lines":["    "],"id":579}],[{"start":{"row":43,"column":6},"end":{"row":43,"column":7},"action":"remove","lines":[" "],"id":580}],[{"start":{"row":38,"column":0},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":581}],[{"start":{"row":38,"column":0},"end":{"row":39,"column":0},"action":"remove","lines":["",""],"id":582},{"start":{"row":37,"column":0},"end":{"row":38,"column":0},"action":"remove","lines":["",""]},{"start":{"row":36,"column":3},"end":{"row":37,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":36,"column":3},"end":{"row":37,"column":0},"action":"insert","lines":["",""],"id":583},{"start":{"row":37,"column":0},"end":{"row":37,"column":3},"action":"insert","lines":["   "]}],[{"start":{"row":37,"column":2},"end":{"row":37,"column":3},"action":"remove","lines":[" "],"id":584},{"start":{"row":37,"column":1},"end":{"row":37,"column":2},"action":"remove","lines":[" "]}],[{"start":{"row":37,"column":0},"end":{"row":37,"column":1},"action":"remove","lines":[" "],"id":585}],[{"start":{"row":38,"column":0},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":586}],[{"start":{"row":38,"column":0},"end":{"row":39,"column":0},"action":"remove","lines":["",""],"id":587}],[{"start":{"row":39,"column":1},"end":{"row":40,"column":0},"action":"insert","lines":["",""],"id":588},{"start":{"row":40,"column":0},"end":{"row":40,"column":1},"action":"insert","lines":[" "]},{"start":{"row":40,"column":1},"end":{"row":41,"column":0},"action":"insert","lines":["",""]},{"start":{"row":41,"column":0},"end":{"row":41,"column":1},"action":"insert","lines":[" "]}],[{"start":{"row":41,"column":0},"end":{"row":41,"column":1},"action":"remove","lines":[" "],"id":589},{"start":{"row":40,"column":1},"end":{"row":41,"column":0},"action":"remove","lines":["",""]},{"start":{"row":40,"column":0},"end":{"row":40,"column":1},"action":"remove","lines":[" "]},{"start":{"row":39,"column":1},"end":{"row":40,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":39,"column":1},"end":{"row":39,"column":2},"action":"insert","lines":[" "],"id":590},{"start":{"row":39,"column":2},"end":{"row":39,"column":3},"action":"insert","lines":[" "]},{"start":{"row":39,"column":3},"end":{"row":39,"column":4},"action":"insert","lines":[" "]}],[{"start":{"row":40,"column":0},"end":{"row":40,"column":1},"action":"insert","lines":[" "],"id":591},{"start":{"row":40,"column":1},"end":{"row":40,"column":2},"action":"insert","lines":[" "]},{"start":{"row":40,"column":2},"end":{"row":40,"column":3},"action":"insert","lines":[" "]},{"start":{"row":40,"column":3},"end":{"row":40,"column":4},"action":"insert","lines":[" "]}],[{"start":{"row":38,"column":16},"end":{"row":38,"column":23},"action":"remove","lines":["task_id"],"id":592},{"start":{"row":38,"column":16},"end":{"row":38,"column":28},"action":"insert","lines":["/task_recipe"]}],[{"start":{"row":31,"column":0},"end":{"row":32,"column":0},"action":"insert","lines":["",""],"id":593}],[{"start":{"row":32,"column":0},"end":{"row":37,"column":53},"action":"insert","lines":["@app.route('/edit_task/<task_id>')","def edit_task(task_id):","    the_task =  mongo.db.tasks.find_one({\"_id\": ObjectId(task_id)})","    all_categories =  mongo.db.categories.find()","    return render_template('edittask.html', task=the_task,","                           categories=all_categories)"],"id":594}],[{"start":{"row":37,"column":53},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":595},{"start":{"row":38,"column":0},"end":{"row":38,"column":27},"action":"insert","lines":["                           "]}],[{"start":{"row":38,"column":0},"end":{"row":41,"column":69},"action":"remove","lines":["                           ","@app.route('/task_recipe')","def recipes():","    return render_template(\"recipes.html\", task=mongo.db.tasks.find()"],"id":596},{"start":{"row":24,"column":0},"end":{"row":27,"column":69},"action":"insert","lines":["                           ","@app.route('/task_recipe')","def recipes():","    return render_template(\"recipes.html\", task=mongo.db.tasks.find()"]}],[{"start":{"row":27,"column":69},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":597},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":29,"column":0},"end":{"row":30,"column":0},"action":"insert","lines":["",""],"id":598}],[{"start":{"row":27,"column":69},"end":{"row":27,"column":70},"action":"insert","lines":[")"],"id":599}],[{"start":{"row":42,"column":53},"end":{"row":42,"column":54},"action":"insert","lines":[")"],"id":600}],[{"start":{"row":42,"column":53},"end":{"row":42,"column":54},"action":"remove","lines":[")"],"id":601},{"start":{"row":42,"column":52},"end":{"row":42,"column":53},"action":"remove","lines":[")"]}],[{"start":{"row":42,"column":52},"end":{"row":42,"column":53},"action":"insert","lines":[")"],"id":602}],[{"start":{"row":47,"column":16},"end":{"row":47,"column":17},"action":"remove","lines":["/"],"id":603}],[{"start":{"row":47,"column":16},"end":{"row":47,"column":27},"action":"remove","lines":["task_recipe"],"id":604},{"start":{"row":47,"column":16},"end":{"row":47,"column":23},"action":"insert","lines":["task_id"]}],[{"start":{"row":16,"column":45},"end":{"row":16,"column":46},"action":"insert","lines":["s"],"id":605}],[{"start":{"row":27,"column":47},"end":{"row":27,"column":48},"action":"insert","lines":["s"],"id":606}]]},"ace":{"folds":[],"customSyntax":"python","scrolltop":0,"scrollleft":0,"selection":{"start":{"row":11,"column":0},"end":{"row":11,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":32,"state":"start","mode":"ace/mode/python"}},"timestamp":1580751770245,"hash":"e9d4d21fcda97e10e184bb7b82b44bf6017c3b3e"}