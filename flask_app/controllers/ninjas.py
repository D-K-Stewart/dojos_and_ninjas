from flask import render_template,redirect,request,session,flash

from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo



@app.route('/ninjas')
def new_ninjas():
    
    return render_template('new_ninja.html', all_dojos=Dojo.get_all())



@app.route('/ninja', methods=['POST'])
def create_ninjas():
    
    data = {
        'first_name' : request.form['first_name'],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo_id"]
    }
    dojo_id = request.form["dojo_id"]
    Ninja.create(data)

    return redirect(f'/dojos/{dojo_id}')