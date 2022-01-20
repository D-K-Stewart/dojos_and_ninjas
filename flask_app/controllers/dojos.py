from flask import render_template,redirect,request,session,flash

from flask_app import app

from flask_app.models.dojo import Dojo


@app.route('/')
@app.route('/dojos')
def all_dojos():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('index.html', all_dojos = dojos)


@app.route('/dojos/create', methods=['POST'])
def create_dojos():
    data = {
        
        "name" : request.form["name"]

    }
    Dojo.create(data)

    return render_template('/')


@app.route('/dojos/<int:id>')
def show_dojos(id):

    data = {

        'id' : id
    }
    return render_template('dojo_show.html', dojo=Dojo.get_dojo_with_ninjas(data))