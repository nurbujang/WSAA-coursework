# run in venv: source ./venv/bin/activate
# make : python -m venv venv
# make with sys packages: python -m venv venv --system-site-packages
# see packages: pip freeze
# save to file: pip freeze > requirements.txt
# load a file of packages: pip install -r > requirements.txt
# exit: deactivate
# remove (if u make a mistake): rm -rf venv

from flask import Flask, request, jsonify

# check if it runs nicely
# app = Flask(__name__)

# @app.route('/')
# def index():
#     return "hello mak"

# if __name__ == "__main__":
#     app.run(debug = True)

#===============================================

# take in data as arguments
# app = Flask(__name__)

# @app.route('/')
# def index():
#     return "hello mak"

# @app.route("/inquery")
# def inquery():
#     name = request.args["name"]
#     return name

# if __name__ == "__main__":
#     app.run(debug = True)

# http://127.0.0.1:5000/inquery?name=nur

#==================================================
    
#add 2nd argument
# app = Flask(__name__)

# @app.route('/')
# def index():
#     return "hello mak"

# @app.route("/inquery")
# def inquery():
#     name = request.args["name"]
#     return request.args

# if __name__ == "__main__":
#     app.run(debug = True)

# go to raw data http://127.0.0.1:5000/inquery?name=nur&age=18
    
#=====================================================================
    
# in the body of msg, dont go to http://127.0.0.1:5000/inbody
# method is not allowed#so use postman
    
app = Flask(__name__)

@app.route('/')
def index():
    return "hello mak"

@app.route("/inquery")
def inquery():
    name = request.args["name"]
    return request.args

@app.route("/inbody", methods=["POST"])
def inbody():
    name = request.json["name"]
    #print (request.json)
    return f"you are {name}"


if __name__ == "__main__":
    app.run(debug = True)

#========================================================
# in the body of msg with multiple args
    
# app = Flask(__name__)

# @app.route('/')
# def index():
#     return "hello mak"

# @app.route("/inquery")
# def inquery():
#     name = request.args["name"]
#     return request.args

# @app.route("/inbody", methods=["POST"])
# def inbody():
#     name = request.json["name"]
#     age = request.json["age"]
#     #print (request.json)
#     return f"you are {name} and aged {age} {type(age)}"


# if __name__ == "__main__":
#     app.run(debug = True)

# 
    
#============================================
# 

# @app.route('/user')
# def getuser():
#     user={
#         'name': "andrew",
#         'age' : 21
#     }
#     return jsonify(user)

# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return "hello mum"

# @app.route("/inquery")
# def inquery():
#     name = request.args["name"]
#     return request.args

# @app.route("/inbody", methods=["POST"])
# def inbody():
#     name = request.json["name"]
#     age = request.json["age"]
#     #print (request.json)
#     return f"you are {name} and aged {age} {type(age)}"

# @app.route('/user')
# def getuser():
#     user={
#         'name': "andrew",
#         'age' : 21
#     }
#     return jsonify(user)

# if __name__ == "__main__":
#     app.run(debug = True)
