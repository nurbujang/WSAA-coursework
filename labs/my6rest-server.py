# run in venv: source ./venv/bin/activate
# make : python -m venv venv
# make with sys packages: python -m venv venv --system-site-packages
# see packages: pip freeze
# save to file: pip freeze > requirements.txt
# load a file of packages: pip install -r > requirements.txt
# exit: deactivate
# remove (if u make a mistake): rm -rf venv

# 1 basic server and test to see if it works
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#         return "Hello world"

# if __name__ == "__main__":
#     app.run(debug = True)

# http://127.0.0.1:5000. 
#it works. good

#=================================================================
# 2. implement all the proposed interfaces (slide 4: REST for project).
# create all these routes
# make those end points and then I can test them with curl or postman
    
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#         return "Hello world"

# # getall
# # curl http://127.0.0.1:5000/books

# @app.route('/books', methods=['GET'])
# def getall():
#         return "get all"

# if __name__ == "__main__":
#     app.run(debug = True) 

#===================================================
# now do the find by id

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#         return "Hello world"

# # getall
# # curl http://127.0.0.1:5000/books

# @app.route('/books', methods=['GET'])
# def getall():
#         return "get all"

# # find by id
# # curl http://127.0.0.1:5000/books/2323

# @app.route('/books/<int:id>', methods=['GET'])
# def findbyid(id):
#         return "find by id"


# if __name__ == "__main__":
#     app.run(debug = True) 

#======================================================
# #create
# #curl -X POST -d "{\"title\":\"test\", \"author\":\"some guy\", \"price\":123}" http://127.0.0.1:5000/books
# # CANNOT TEST WITH WEB BROWSWR. TEST WITH POSTMAN
   
# from flask import Flask, request 

# app = Flask(__name__)

# @app.route('/')
# def index():
#         return "Hello world"

# # getall
# # curl http://127.0.0.1:5000/books

# @app.route('/books', methods=['GET'])
# def getall():
#         return "get all"

# # find by id
# # curl http://127.0.0.1:5000/books/2323

# @app.route('/books/<int:id>', methods=['GET'])
# def findbyid(id):
#         return "find by id"

# @app.route('/books', methods=['POST'])
# def create():
#         # read json from the body
#         jsonstring = request.json

#         return f"create {jsonstring}" 


# if __name__ == "__main__":
#     app.run(debug = True) 

#========================================

# # update
# # curl -X PUT -d "{\"title\":\"test\", \"author\":\"some guy\", \"price\":123}" http://127.0.0.1:5000/books/1
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
        return "Hello world"

# getall
# curl http://127.0.0.1:5000/books

@app.route('/books', methods=['GET'])
def getall():
        return "get all"

# find by id
# curl http://127.0.0.1:5000/books/2323

@app.route('/books/<int:id>', methods=['GET'])
def findbyid(id):
        return "find by id"

# CREATE
@app.route('/books', methods=['POST'])
def create():
        # read json from the body
        jsonstring = request.json
        return f"create {jsonstring}"

#UPDATE
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
        jsonstring = request.json
        return f"update {id} {jsonstring}"

# Delete
# curl -X DELETE  http://127.0.0.1:5000/books/1

@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
        return f"delete {id}"


if __name__ == "__main__":
    app.run(debug = True) 






###########################################################################################

# # very simple flask server

# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/')
# def index():
#         return "Hello world"

# # getall
# # curl http://127.0.0.1:5000/books

# @app.route('/books', methods=['GET'])
# def getall():
#         return "get all"

# # find by id
# # curl http://127.0.0.1:5000/books/1

# @app.route('/books/<int:id>', methods=['GET'])
# def findbyid(id):
#         return "find by id"

# #create
# #curl -X POST -d "{\"title\":\"test\", \"author\":\"some guy\", \"price\":123}" http://127.0.0.1:5000/books
# @app.route('/books', methods=['POST'])
# def create():
#         # read json from the body
#         jsonstring = request.json

#         return f"create {jsonstring}"

# # update
# # curl -X PUT -d "{\"title\":\"test\", \"author\":\"some guy\", \"price\":123}" http://127.0.0.1:5000/books/1

# @app.route('/books/<int:id>', methods=['PUT'])
# def update(id):
#         jsonstring = request.json
#         return f"update {id} {jsonstring}"

# # Delete
# # curl -X DELETE  http://127.0.0.1:5000/books/1

# @app.route('/books/<int:id>', methods=['DELETE'])
# def delete(id):
#         return f"delete {id}"


# if __name__ == "__main__":
#     app.run(debug = True)
