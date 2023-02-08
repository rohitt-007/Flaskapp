from flask import *  
app = Flask(__name__)  

@app.route('/')  
def customer():  
   return render_template('Emp_form.html')  

@app.route('/success',methods = ['POST', 'GET'])  
def print_data():  
   if request.method == 'POST':  
      display = request.form  
      return render_template("display_Emp.html",display = display)  



if __name__ == '__main__':  
   app.run(debug = False)