

# importing FLask 
from flask import *

#Flask constructor takes the name of
app = Flask(__name__)


@app.route('/')
#defining a function
def hello_world():
    return render_template('app_a1_message.html')

@app.route('/home')
#defining a function
def hello_world2():
    return render_template('app_a1_2_message.html')

#main driver function

if __name__ == '__main__': 


    app.run(debug=False)



   