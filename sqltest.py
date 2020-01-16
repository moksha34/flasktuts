import sqlite3
from collections import namedtuple
import csv

class Userobj():
    def __init__(self,_id,name,password,dept):
        self.id=_id
        self.name=name
        self.password =password
        self.dept=dept
    # def __dict__(self):
    #     return {'id':self.id,'name': self.name,'dept': self.dept}

class Serverobj():
    def __init__(self,_id,name,owner):
        self.id=_id
        self.name=name
        self.owner=owner
        

   
def sql_init(servers='servers.csv',users='users.csv'):
    with sqlite3.connect('sqldb.db') as connection:
        cursor=connection.cursor()
        try:
            cursor.execute("CREATE TABLE servers(id int, name text,owner text)")
            cursor.execute("CREATE TABLE users(id int, name text,password text,dept text)")
        except Exception as e:
            if e.__str__() =="table servers already exists":
                pass
            else:
                raise Exception(e)
        else:
            pass
        finally:
            with open('servers.csv') as f:
                reader=csv.reader(f)
                next(reader)
                for r in reader:
                    cursor.execute("INSERT INTO servers values (?,?,?)",tuple(r))
            # allservers = cursor.execute("SELECT * FROM servers")
            
            with open('users.csv') as f:
                reader=csv.reader(f)
                next(reader)
                for r in reader:
                    cursor.execute("INSERT INTO users values (?,?,?,?)",tuple(r))


                     

def get_servers_by_owner(owner):
    command="SELECT * from servers where owner =(?)"
    with sqlite3.connect('sqldb.db') as connection:
        cursor=connection.cursor()
        output=cursor.execute(command,(owner,))
        ownedservers=[Serverobj(x[0],x[1],x[2]) for x in output]
        return ownedservers

def get_servers():
    command="SELECT * from servers "
    with sqlite3.connect('sqldb.db') as connection:
        cursor=connection.cursor()
        output=cursor.execute(command)
        ownedservers=[Serverobj(x[0],x[1],x[2]) for x in output]
        return ownedservers

def get_server_by_name(name):
    command="SELECT * from servers where name=(?)"
    with sqlite3.connect('sqldb.db') as connection:
        cursor=connection.cursor()
        output=cursor.execute(command,(name,))
        servertpl=next(output,None)
        if servertpl:
            return Serverobj(servertpl[0],servertpl[1],servertpl[2])
        return None    

def get_users():
    command="SELECT * from users "
    with sqlite3.connect('sqldb.db') as connection:
        cursor=connection.cursor()
        output=cursor.execute(command)
        allusers=[Userobj(x[0],x[1],x[2],x[3]) for x in output]
        return allusers

def get_user_by_name(name):
    command="SELECT * from users where name=(?)"
    with sqlite3.connect('sqldb.db') as connection:
        cursor=connection.cursor()
        output=cursor.execute(command,(name,))
        usertpl = next(output,None)
        if usertpl:
            return Userobj(usertpl[0],usertpl[1],usertpl[2],usertpl[3])
        return None    

def get_user_by_id(_id):
    command="SELECT * from users where id=(?)"
    with sqlite3.connect('sqldb.db') as connection:
        cursor=connection.cursor()
        output=cursor.execute(command,(_id,))
        usertpl = next(output,None)
        if usertpl:
            return Userobj(usertpl[0],usertpl[1],usertpl[2],usertpl[3])
        return None
# sql_init()
