## run in venv: source ./venv/bin/activate
# make : python -m venv venv
# make with sys packages: python -m venv venv --system-site-packages
# see packages: pip freeze
# save to file: pip freeze > requirements.txt
# load a file of packages: pip install -r > requirements.txt
# exit: deactivate
# remove (if u make a mistake): rm -rf venv

# curl


# lab 06
# python -m venv venv
# source ./venv/bin/activate
# pip install flask
# pip freeze > requirements.txt
# create .gitignore in venv/: touch .gitignore


# Create a basic Flask Server
# 8. Create a file called rest_server.py
# 9. Make a basic server in it and test it

from flask import Flask, url_for, request, redirect, abort

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return "hello"

# Modify the Flask Server to deal with the required URL mappings 
# (the functions can be just skeletons at this stage, I have done this for books)
# 10. Create a mapping and function for each of the possible API calls

@app.route('/books', methods=['GET'])
def getall():
    return "get all"
# getall
# curl http://127.0.0.1:5000/books

@app.route('/books/<int:id>', methods=['GET'])
def findbyid(id):
    return "find by id"
# find by id
# curl http://127.0.0.1:5000/books/1

#create
@app.route('/books', methods=['POST'])
def create():
    # read json from the body
    jsonstring = request.json
    return f"create {jsonstring}"
#create
#curl -X POST -d "{\"title\":\"test\", \"author\":\"some guy\", \"price\":123}" http://127.0.0.1:5000/books

# update
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    jsonstring = request.json
    return f"update {id} {jsonstring}"
# update
# curl -X PUT -d "{\"title\":\"test\", \"author\":\"some guy\", \"price\":123}" http://127.0.0.1:5000/books/1

#delete
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    return f"delete {id}"
#delete
# curl -X DELETE http://127.0.0.1:5000/books/1
 

if __name__ == "__main__":
    app.run(debug=True)


# Test them.
# 11. Using either postman or CURL test each of your endpoints

# getall
# curl http://127.0.0.1:5000/books

# find by id
# curl http://127.0.0.1:5000/books/1

#create
#curl -H "Content-Type:application/json" -X POST -d "{\"title\":\"test\", \"author\":\"some guy\", \"price\":123}" http://127.0.0.1:5000/books

# update
# curl -H "Content-Type:application/json" -X PUT -d "{\"title\":\"test\", \"author\":\"some guy\", \"price\":123}" http://127.0.0.1:5000/books/1

#delete
# curl -H "Content-Type:application/json" -X DELETE http://127.0.0.1:5000/books/1
    

# Future: create the DAO
# 12. Create another file for interacting with the database, mine is for books so is called bookdao.py
    

# returns all the books in the database table
# def getall():
#     return [{}]

# # returns one book
# def findById(id):
#     return {}

# # inserts a book into the database
# def create(book):
#     return book

# # updates the book
# def update(id, book):
#     return book

# # deletes the book with the id
# def delete(id):
#     return True

# Future: integrate the DAO with the server