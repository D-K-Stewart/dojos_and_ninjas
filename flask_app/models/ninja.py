from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo



# DATABASE = ''

class Ninja:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.age = db_data['age']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.dojo_id = None
        

# ----------------------------------------------------------------C

    @classmethod # doesn't taget the instance but instead targets the class itself
    def create(cls,data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW());"
        return connectToMySQL('dojos_ninjas').query_db(query, data) # list of dictionaries

    # ---------------------------------------------------------------R

    @classmethod # doesn't taget the instance but instead targets the class itself
    def get_all(cls):
        query = "SELECT * FROM ninjas WHERE dojo_id=%(id)s;"
        results = connectToMySQL('dojos_ninjas').query_db(query)  #list of dictionaries

        ninjas = []
        for ninja in results: # for loop through the response from the DB _> list of dictionaries
            ninjas.append( cls(ninja) ) # cls takes the dict transforms into a class instance
        return ninjas # returns a list of instance