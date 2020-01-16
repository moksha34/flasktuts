from flask import Flask,request
from sqltest import *
from collections import defaultdict
from flask_restful import Api,Resource
import json
from flask_jwt import JWT,jwt_required
from security import Userobj,authenticate,identity
# GET /users  to send all the users and brief
# POST /Users create a new user
# GET /users/{id} to send all the details of the user

app = Flask(__name__,root_path='assets')
app.config['SECRET_KEY']='secret-super'
jwt=JWT(app,authenticate,identity)
api=Api(app)

class User(Resource):
    
    def get(self,id):
        user_returned=get_user_by_id(id)
        if user_returned:
            return user_returned.__dict__,200
        return "user not found",400


    def post(self,id):
        user=request.get_json()
       


class Users(Resource):
    # @jwt_required()
    def get(self):
        allusers=[x.__dict__ for x in get_users()]
        [x.pop("password",None) for x in allusers]
        return allusers

class Servers(Resource):

    def get(self):
        allservers =[x.__dict__ for x in get_servers()]
        return allservers


class Server(Resource):

    def get(self,owner):
        allservers =[x.__dict__ for x in get_servers_by_owner(owner)]
        return allservers

api.add_resource(User,'/api/users/<int:id>')
api.add_resource(Users,'/api/users')
api.add_resource(Servers,'/api/servers')
api.add_resource(Server,'/api/servers/owner/<string:owner>')

# @app.route('/',methods=['GET']d)
# def home():
#     return "welcome to my api"

# @app.route('/users')
# def getusers():
#     allusers=defaultdict()
#     for user in users:
#         allusers[user['name']]=user['id']
#     return json.dumps(allusers)
    
# @app.route('/users/<int:id>')
# def getuser(id):
#     user = list(filter(lambda x: x['id']==id,users))
#     return json.dumps(user)



if __name__=="__main__":
    app.run(port=8080,debug=True,host="0.0.0.0")

