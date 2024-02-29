# a very simple flask server

from flask import Flask

app = Flask(__name__) # give this the same name as the file that's been run

@app.route('/')
def index():
    return "Hello mamm/Maxi"

@app.route('/blah2')
def blah():
    return "this is blahblah2" # another route

if __name__ == "__main__":
    app.run(debug = True)

#  * Serving Flask app 'my6a_server'
#  * Debug mode: on
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
#  * Running on http://127.0.0.1:5000
# Press CTRL+C to quit
#  * Restarting with stat
#  * Debugger is active!
#  * Debugger PIN: 880-671-283
    

# CrtlC to stop running the program
    
# for blah, go to http://127.0.0.1:5000/blah
    
    # if in the middle of program running and u change to blah2, it will usually detect and update

