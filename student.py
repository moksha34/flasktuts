# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return "hello world"

# if __name__=="__main__" :
#     app.run(debug=True)

# def new_decorator(text):
#     def my_decorater(newfunc):
#         def more_func(*args,**kwargs):
#             print(f"going to execute the function {newfunc.__name__}")
#             print(text)
#             newfunc(*args,**kwargs)
#             print("done running func")
#         return more_func
#     return my_decorater    

# @new_decorator("wtf")
# def test(x,y):
#     print(x,y)
    


# test(1,2)