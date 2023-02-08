from flask import *   
app = Flask(__name__)

@app.route('/CEO')  
def CEO():  
    return 'Welcome CEO'  
#app.add_url_rule("/CEO","CEO",CEO) 

@app.route('/Employees')  
def Employees():  
    return "Welcome Employee"  
#app.add_url_rule("/Employees","Employees",Employees) 

@app.route('/Clients')  
def Clients():  
    return 'Welcome Clients'  
#app.add_url_rule("/Clients","Clients",Clients) 


######FOR REDIRECTING PAGE########
#@app.route('/CEO_loggedin')  
def CEO_loggedin():  
    return 'You are Official LoggedIn in for Classify Info.'  
app.add_url_rule("/CEO_loggedin","CEO_loggedin",CEO_loggedin) 

#@app.route('/Employees_loggedin')  
def Employees_loggedin():  
    return 'Welcome to the CRM'  
app.add_url_rule("/Employees_loggedin","Employees_loggedin",Employees_loggedin) 

#@app.route('/Clients_loggedin')  
def Clients_loggedin():  
    return 'Welcome to Stratacent!!!!'  
app.add_url_rule("/Clients_loggedin","Clients_loggedin",Clients_loggedin) 



# so this is where the url_function helps in redirects (dynamic redirect)  
@app.route('/loggedin/<role>')  
def user(role):  
    if role == 'CEO':  
        return redirect(url_for('CEO_loggedin'))  
    if role == 'Employees':  
        return redirect(url_for('Employees_loggedin'))  
    if role == 'Clients':  
        return redirect(url_for('Clients_loggedin')) 

@app.route('/loggedin1/<role>/<int:ID>')  
def loggingwithID(role,ID):  
    if role == 'CEO':  
        return 'You Are CEO'  
    elif role == 'Employee' and ID in range(9000,9999):
        return f"Welcome {role} so you are with ID-{ID} " 

    elif role =='Employee' and ID not in range(9000,9999):
        return "<h1>INVALID EMPLOYEE!!!!</h1>"

    elif role == 'Client' and ID in range(9000,9999):
        return f"Welcome {role} so you are with ID-{ID}"  

    elif role =='Client' and ID not in range(9000,9999):
        return "<h1>INVALID CLIENT/h1>"


if __name__ =="__main__":  
    app.run(debug = False) 