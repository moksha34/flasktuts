from pprint import pprint
from collections import defaultdict
from sqltest import *


    

# allusers=[User(1,"ram","acdf"),User(2,'rahim','red')]

# user_mapping = defaultdict()
# userid_mapping=defaultdict()
# for x in allusers:
#     user_mapping[x.name]=x
#     userid_mapping[x.id]=x


# def adduser(x):
#     allusers.append(x)
#     user_mapping[x.name]=x
#     userid_mapping[x.id]=x

def authenticate(username,password):
    user=get_user_by_name(username)
    if user and user.password==password:
        print(f"user {username} is successfully authenticated")
        return user
    return None 

def identity(payload):
    user_id =payload['identity']
    user=get_user_by_id(user_id)
    if user:
        return user
    return None    


print(authenticate("user001","passwod"))
  
