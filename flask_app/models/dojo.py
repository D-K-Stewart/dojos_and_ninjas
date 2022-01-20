from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja



class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name= data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_dojo_with_ninjas( cls , data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_ninjas').query_db( query , data )
            # results will be a list of topping objects with the burger attached to each row. 
        dojo = cls( results[0] )
        ninjas=[]
        for row_from_db in results:
                # Now we parse the burger data to make instances of burgers and add them into our list.
            ninja_data = {
                    "id" : row_from_db["ninjas.id"],
                    'first_name' : row_from_db['first_name'],
                    "last_name" : row_from_db["last_name"],
                    "age" : row_from_db["age"],
                    "created_at" : row_from_db["ninjas.created_at"],
                    "updated_at" : row_from_db["ninjas.updated_at"],
                    "dojo_id" : row_from_db["dojo_id"]
                    
            }
            ninjas.append( ninja.Ninja( ninja_data ) )
        dojo.ninjas=ninjas
        return dojo

    # ----------------------------------------------------------------C

    @classmethod # doesn't taget the instance but instead targets the class itself
    def create(cls,data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL('dojos_ninjas').query_db(query, data) # list of dictionaries

    # ---------------------------------------------------------------R

    @classmethod # doesn't taget the instance but instead targets the class itself
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_ninjas').query_db(query)   #list of dictionaries

        dojos = []
        for dojo in results: # for loop through the response from the DB _> list of dictionaries
            dojos.append( cls(dojo) ) # cls takes the dict transforms into a class instance
        return dojos # returns a list of instance



    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE dojos.id=%(id)s;"
        results = connectToMySQL('dojos_ninjas').query_db(query, data)
        dojo=cls(results[0]) #

        return dojo