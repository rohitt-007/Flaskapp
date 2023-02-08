from flask import *  
app = Flask(__name__)  

def success_func(name):
    return "<h1>Welcome %s </h1>" %name

app.add_url_rule("/success/<name>","success",success_func)

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))


if __name__ == '__main__':
   app.run(debug = False) 