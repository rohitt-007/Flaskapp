# importing FLask 
from flask import *

#Flask constructor takes the name of
app = Flask(__name__)


@app.route('/')
#defining a function
def message():
        return render_template('app_a1_message.html')

#main driver function

if __name__ == '__main__': 


    app.run(debug=False)