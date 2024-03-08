# run in venv: source ./venv/bin/activate
# make : python -m venv venv
# make with sys packages: python -m venv venv --system-site-packages
# see packages: pip freeze
# save to file: pip freeze > requirements.txt
# load a file of packages: pip install -r > requirements.txt
# exit: deactivate
# remove (if u make a mistake): rm -rf venv

from flask import Flask, url_for, redirect

# instead of just doing app = flask, static url path is blank

# app = Flask(__name__, static_url_path='', static_folder='my6staticpages')

# if __name__ == "__main__":
#     app.run(debug=True)

# view page source on view-source:http://127.0.0.1:5000/index.html, we will see the same thing in index
    # can do get http://127.0.0.1:5000/index.html on postman
# you can put as many different files as you like into the static pages and they'll be found 
#=================================================================================================

app = Flask(__name__, static_url_path='', static_folder='my6staticpages')

# # mapping
# @app.route('/')
# def index():
#     return "<h1>hi there ibu</h1>"

# if __name__ == "__main__":
#     app.run(debug=True)
#===============================================================================================
# if dealing with users:

# app = Flask(__name__, static_url_path='', static_folder='my6staticpages')

# # mapping
# @app.route('/')
# def index():
#     return "<h1>hi there ibu</h1>"

# # get all user
# @app.route('/users', methods=['GET'])
# def get_users():
#     return "getting all users"

# # get a user
# @app.route("/users/<username>", methods=['GET']) 
# def get_user_byname(username):
#     return f"hello {username}" 

# if __name__ == "__main__":
#     app.run(debug=True)

# go to http://127.0.0.1:5000/users
# go to http://127.0.0.1:5000/users/andrew
#====================================================================================================
app = Flask(__name__, static_url_path='', static_folder='my6staticpages')

# mapping
@app.route('/')
def index():
    return "<h1>hi there ibu</h1>"

# get all user
@app.route('/users', methods=['GET'])
def get_users():
    return "getting all users"

# get a user
@app.route("/users/<username>", methods=['GET']) 
def get_user_byname(username):
    return f"hello {username}" 

# if use number (but not advisable)
@app.route("/users/<int:id>", methods=['GET']) 
def get_user_byid(id):
    return f"your id is {id}"

# to send post to users
@app.route('/users', methods=['POST'])
def create_user():
    return "creating a user"

# to update a user:
@app.route('/users', methods=['PUT'])
def update_user():
    return "update a user"

# if you can do redirects when you've finished your code. 
# So let's say if you did an update and you just wanted to update to redirect straight to back to the index
# Let's say we had an app root invalid. Pretend that there's some invalid URL.
# Will redirect the post to some URL. 
@app.route('/invalid', methods=['GET'])
def testingredirect():
    return redirect(url_for('index')) # index needs to be a string
# go to 127.0.0.1:5000/invalid, but will go back to http://127.0.0.1:5000
# on postman, get http://127.0.0.1:5000/invalid, will go to hi there ibu

# if u write a function called square:
@app.route("/square/<int:id>", methods=['GET']) 
def square(id):
    return f"the square of {id} is {id**2}" 
# go to http://127.0.0.1:5000/square/5
# on postman get http://127.0.0.1:5000/square/5

if __name__ == "__main__":
    app.run(debug=True)

# go to http://127.0.0.1:5000/users/2345
# on postman get http://127.0.0.1:5000/users/2345. post will get error
# on potman, post http://127.0.0.1:5000/users
# on postman put http://127.0.0.1:5000/users








# if __name__ == "__main__":
#     app.run(debug=True)







# ori

# from flask import Flask, url_for, redirect

# app = Flask(__name__, static_url_path='', static_folder='staticpages')

# # mapping
# @app.route('/')
# def index():
#     return "<h1>hi there mom</h1>"

# @app.route('/users', methods=['GET'])
# def get_users():
#     return "getting all users"

# @app.route("/users/<username>", methods=['GET']) 
# def get_user_byname(username):
#     return f"hello {username}" 

# @app.route("/users/<int:id>", methods=['GET']) 
# def get_user_byid(id):
#     return f"your id is {id}" 

# @app.route('/users', methods=['POST'])
# def create_user():
#     return "createing a user"

# @app.route('/users', methods=['PUT'])
# def update_user():
#     return "update a user"

# @app.route('/invalid', methods=['GET'])
# def testingredirect():
#     return redirect(url_for('index'))

# @app.route("/square/<int:id>", methods=['GET']) 
# def square(id):
#     return f"the square of {id} is {id**2}" 


# if __name__ == "__main__":
#     app.run(debug=True)
