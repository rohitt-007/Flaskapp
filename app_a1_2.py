# importing FLask 
from flask import Flask

#Flask constructor takes the name of
app = Flask(__name__)


@app.route('/page1')
#defining a function
def hello_world1():
    return 'Hello World Flask'

@app.route('/page2')
#defining a function
def hello_world2():
    return '<h1>Hello World Flask is a Header </h1>'

@app.route('/page3')
#defining a function
def hello_world3():
    return '<p>Hello World Flask</p>'

#main driver function

if __name__ == '__main__': 


    app.run(debug=False)
