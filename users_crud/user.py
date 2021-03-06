# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        # the update method will be used when we need to update a friend in our database
    @classmethod
    def update(cls,data, id):
        query = f"UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s WHERE id = {id};"
        return connectToMySQL('users').query_db(query,data)

        # the delete method will be used when we need to delete a friend from our database
    @classmethod
    def delete(cls, id):
        query  = f"DELETE FROM users WHERE id = {id};"
        return connectToMySQL('users').query_db(query)

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users').query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for friend in results:
            users.append( cls(friend) )
        return users

    @classmethod
    def get_one(cls,id):
        query  = "SELECT * FROM users WHERE id = %(id)s";
        result = connectToMySQL('users').query_db(query, {'id':id})
        return cls(result[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"
        result = connectToMySQL('users').query_db(query,data)
        return result