'''
This is main file in the program starts and execute
This file route home,dashboard,login,register,logout,profile,course
'''
from flask import Flask,render_template,request,redirect,url_for,session

# import credentials init pyrebase for auth login and register + db2 credentials for user database
from auth import LogAuth
import fetch # in this package has 2 methods  fetchData & addData 

app = Flask(__name__)
app.secret_key="123"

@app.route('/')
def home():
    return render_template ("index.html")

@app.route("/user/<username>")
def dashboard(username):
    if ('user' in session):
        return render_template('dashboard.html',username=username)
    else:
        return redirect(url_for('login'))
    
@app.route('/login')
def login():
    # if already logged in check cookies if yes then click login button it redirects account
    if ('user' in session):
        return redirect(url_for("dashboard",username=session['user']['name']))
    else:
        return render_template("./auth/login.html")

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for('home'))

@app.route('/register')
def register():
    return render_template("./auth/register.html")

@app.route('/registerData',methods=["POST",'GET'])
def registerData():
    if request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        password=request.form.get('password')
        try:
            user=LogAuth.auth.create_user_with_email_and_password(email,password) 
            fetch.addData(user['idToken'],name,email)   
        except :
            return  "error plz make sure password has 6 characters and email id valid"
    return redirect(url_for('home'))

@app.route('/loginData',methods=["POST","GET"])
def logindata():
    if request.method=='POST':
        try:
            emailEl=request.form['emailEl']
            passwordEl=request.form['passwordEl']
            user = LogAuth.auth.sign_in_with_email_and_password(emailEl,passwordEl)
            userId =(user['localId'])
            # fetch method ==> fetch user data  
            fetchData=fetch.fetchData(userId)
            session['user']=fetchData
        except:
            return "Failed to login"
    return redirect(url_for("dashboard",username=fetchData['name']))


# individual profile page
@app.route('/user/profile')
def profile():
    return render_template('profile.html',username=session['user']['name'],email=session['user']['email'])

@app.route('/check')
def check():
    if ('user' in session):
        return redirect(url_for('dashboard',username=session['user']['name']))
    else:
        return redirect(url_for('home'))

# if already log in it shows profile button else it shows log in button
@app.route('/course')
def course():
    a=False
    if ('user' in session):
        a=True
    return render_template('course.html', session=a )

if __name__ == "__main__":
    app.run('0.0.0.0',port=8080,debug=True)
