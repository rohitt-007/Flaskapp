# importing FLask 
from flask import *

#Flask constructor takes the name of
app = Flask(__name__)


@app.route('/user/<uname>')
#defining a function
def message(uname):
        return render_template('message1.html',name=uname)

#main driver function

if __name__ == '__main__': 


    app.run(debug=False)