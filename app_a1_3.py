# importing FLask 
from flask import Flask

#Flask constructor takes the name of
app = Flask(__name__)


@app.route('/Home')
#defining a function
def hello_world1():
    return '<h1>This the home Page</h1>'

@app.route('/About Us')
#defining a function
def hello_world2():
    return '<p>This is About Us </p>'

@app.route('/Location')
#defining a function
def hello_world3():
    return '<h1>Location is here WeWork Pune</h1>'

@app.route('/Contact Us')
#defining a function
def hello_world4():
    return '<h1>Contact us here number is - 100 </h1>'

#main driver function

if __name__ == '__main__': 


    app.run(debug=False)
