# importing FLask

from flask import *



#Flask constructor takes the name of

app = Flask(__name__)




@app.route('/frontpage')

#defining a function

def hello_world():

    return render_template('frontpage.html')



@app.route('/dealspage')

#defining a function

def hello_world2():

    return render_template('dealspage.html')



@app.route('/errorpage')

#defining a function

def hello_world3():

    return render_template('errorpage.html')




#main driver function



if __name__ == '__main__':




    app.run(debug=False)

