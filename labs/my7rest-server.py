# flask server that links to a DAO
# this is our server that will deal with the database. 
# note: There's no database code in here at all. This is relatively simple. 
# This sample code is in REST-server and the only difference when I actually go and do a book deal is I'm just going to take that skeleton out 
# and we're going to use this real my7bookDAO that I've created already and that will actually deal with the database
# create, put title harry, author jk, price 12 will still hv 
# {
#     "author": "someone",
#     "id": 1,
#     "price": 999,
#     "title": "blah"
# }
# bc this is not actually putting any real data into the database.
# so it's only said the DAO doesn't actually exist. It doesn't actually do anything real. 
# I'm just sort of checking that it these do what I think they do, which hits my skeleton do which doesn't do any work yet, so the data isn't real yet. 
# But the mapping between the http://requests and my flask server works, and that calls a DAO. 
# So now when I go and do work, I don't need to do any more work with my REST server. 
# The work I'm now doing is in the DAO where I don't have to worry about where the code comes from.
# author: Andrew Beatty

from flask import Flask, request, jsonify, abort
from my7bookDAOskeleton import bookDAO

app = Flask(__name__)

@app.route('/')
def index():
        return "Hello world"

# getall
# curl http://127.0.0.1:5000/books

@app.route('/books', methods=['GET'])
def getall():
        return jsonify(bookDAO.getAll())

# find by id
# curl http://127.0.0.1:5000/books/1

@app.route('/books/<int:id>', methods=['GET'])
def findbyid(id):
        return jsonify(bookDAO.findByID(id))

#create
#curl -X POST -d "{\"title\":\"test\", \"author\":\"some guy\", \"price\":123}" http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def create():
        # read json from the body
        jsonstring = request.json
        book = {}

        if "title" not in jsonstring: # create uses not in
                abort(403) # pass whatever error is appropriate. look it up
        book["title"] = jsonstring["title"]

        if "author" not in jsonstring:
                abort(403)
        book["author"] = jsonstring["author"]
        
        if "price" not in jsonstring:
                abort(403)
        book["price"] = jsonstring["price"]
        
        return jsonify(bookDAO.create(book))

# update
# curl -X PUT -d "{\"title\":\"test\", \"author\":\"some guy\", \"price\":123}" http://127.0.0.1:5000/books/1
# in postman, put http://127.0.0.1:5000/books/1

@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
        jsonstring = request.json
        book = {}

        if "title" in jsonstring: # update uses in, if it's there, update
                book["title"] = jsonstring["title"]
        if "author" in jsonstring:
                book["author"] = jsonstring["author"]
        if "price" in jsonstring:
                book["price"] = jsonstring["price"]
        
        return jsonify(bookDAO.update(id, book))

# Delete
# curl -X DELETE  http://127.0.0.1:5000/books/1

@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
        return jsonify(bookDAO.delete(id))


if __name__ == "__main__":
    app.run(debug = True)
