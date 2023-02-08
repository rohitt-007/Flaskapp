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
def hello_world3(name):
    return '<h1>hello %s how are you boi!!!!</h1>' %name

@app.route('/page4/<int:age>')
#defining a function
def hello_world4(age):
    return '<h1>hello your age = %d</h1>' %age

#main driver function

if __name__ == '__main__': 


    app.run(debug=False)


