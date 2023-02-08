# importing FLask 
from flask import Flask

#Flask constructor takes the name of
app = Flask(__name__)


@app.route('/')
#defining a function
def hello_world():
    return 'Hello World Flask'

#main driver function

if __name__ == '__main__': 


    app.run(debug=False)
