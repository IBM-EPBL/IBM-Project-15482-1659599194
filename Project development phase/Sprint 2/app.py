'''
This is main file in this app starts and execute
This file route home,dashboard,login,register,logout,profile,course
'''

from flask import Flask,render_template,request,redirect,url_for,session

from auth import LogAuth
# auth: Import credentials for database
import fetch 
# fetch: In this package has 2 methods fetchData(fetch data from database) & addData(add user data to database)
import profileUpdate 
# profileUpdate: The user update the information , the information update database to   
import jobLoad  
# jobLoad: Through external api fetch Jobs when the search and load the jobs
import jobDetailsLoad 
# jobDetailsLoad: it gives job description and apply link when click the job post
import RegisterData
# RegisterData: it check valid name,email,password

app = Flask(__name__)
app.secret_key="123"

@app.route('/')
def home():
    ''' Route Home page '''
    return render_template ("index.html")

@app.route("/user/<username>")
def dashboard(username):
    ''' Route Dashboard. When user log in the session is stored if the user  logged in it redirect to 
    dashboard else it redirect to login page '''
    if ('user' in session):  
        jobs=jobLoad.fetchDefaultJob()
        return render_template('dashboard.html',username=session['user'],jobs=jobs,count="None")
    else:
        return redirect(url_for('login'))
    
@app.route('/login')
def login():
    ''' Route login Page. when click login page it checks session is active if active it redirects 
    dashboard else redirect to login page'''
    if ('user' in session):
        return redirect(url_for("dashboard",username=session['user']['name']))
    else:
        return render_template("./auth/login.html")

@app.route('/logout')
def logout():
    ''' Route logout. When use click log out the user session is deleted '''
    session.pop('user')
    return redirect(url_for('home'))

@app.route('/register')
def register():
    ''' Route register page. It render register page '''
    return render_template("./auth/register.html")

@app.route('/registerData',methods=["POST",'GET'])
def registerData():
    ''' Route register Data. when user filled the register form the details are verified if it's valid redirect
    to  home page else it rendered register page with exception message '''
    if request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        password=request.form.get('password')
        error= registerData.checkValid(name,email,password)
        if error != None:
            return render_template("./auth/register.html",error=error)
        try:
            user=LogAuth.auth.create_user_with_email_and_password(email,password)
            fetch.addData(user['idToken'],name,email)   
        except :
            error="You already Registered Please Login with Your Credentials"
            return  render_template("./auth/register.html",error=error)
    return redirect(url_for('home'))

@app.route('/loginData',methods=["POST","GET"])
def logindata():
    ''' Route login Data. When user filled the login form and press submit the api pass email, password. 
    The email and password verify if exists in database. If exist fetch the user data and create a session'''
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
            error="Your email/password are not matched.."
            return render_template("./auth/login.html",error=error)
    return redirect(url_for("dashboard",username=fetchData['name']))

@app.route('/user/profile')
def profile():
    ''' Route Profile page. It shows user information stored in session'''
    const =session['user']
    return render_template('profile.html',data=const)

@app.route('/check')
def check():
    ''' Route check. if user logged in it shows dashboard else it shows landing page '''
    if ('user' in session):
        return redirect(url_for('dashboard',username=session['user']['name']))
    else:
        return redirect(url_for('home'))

@app.route('/course')
def course():
    ''' Route course. if logged in it shows profile button else it shows log in button '''
    if ('user' in session):
        return render_template('course.html', see=True )
    else:
        return render_template('course.html', see=False  )

@app.route('/update',methods=["POST","GET"])
def update():
    ''' Route update. It fetch all details in profile update form and update in database and session '''
    if request.method=='POST':
        try:
            id = session['user']['id']
            name = session ['user']['name']
            email =session['user']['email']
            number=request.form['number']
            role =request.form['role']
            skill1 =request.form['skill1']
            skill2 =request.form['skill2']
            skill3 =request.form['skill3']
            data={'id':id,'name':name,'email':email,'number':number,'role':role,'skill1':skill1,'skill2':skill2,
                'skill3':skill3,'update':True,'jobFetchCount':session['user']['jobFetchCount']}
            profileUpdate.update(id,data)
            session['user']=data
        except:
            return "user update failed"
    return render_template('profile.html',data=data)

@app.route('/search',methods=['POST'])
def search():
    ''' Route search. Each user gets 3 free search so it check search limit stored in session if it's under 
    limit request job details in job api and the job results are passes into dasboard and the results also 
    stored in database. meanwhile the Search limit is updated in cloud and session '''
    if request.method=='POST':
        try:
            id=session['user']['id']
            count=session['user']['jobFetchCount']  
            role=request.form['role']
            city=request.form['city']
            country=request.form['country']
            if count < 3:
                # jobLoad.jobapi(id,count,role,city,country)
                jobs=jobLoad.fetchDefaultJob(id+str(session['user']['jobFetchCount']))
                data=session['user']
                data['jobFetchCount']= data['jobFetchCount']+1 
                session['user']=data
                profileUpdate.update(id,data)
                return render_template('dashboard.html',username=session['user'],jobs=jobs,count=data['jobFetchCount']-1)
            else:
                return "You Used 3 searches If you need more Please Mail to this ID prakasha.ece19@gmail.com"
        except:
            return "Search failed"
            return redirect(url_for("dashboard",username=session['user']))

@app.route("/history/<history>")
def history(history):
    ''' Route History. The history of job searches are stored in database. when the user request to see the jobs 
    and details. it get from database and showed in history page '''
    error=""
    if session['user']['jobFetchCount']!=0:
        print((session['user']['jobFetchCount']))
        print(int(history))
        if (session['user']['jobFetchCount']) > int(history):
            print("....loaded")
            jobs=jobLoad.fetchDefaultJob(str(session['user']['id'])+(history))
            return render_template("history.html",history=history,jobs=jobs,count=history)
        else:
            error="No Search History. Search the job results are saved in history"
            # return render_template("history.html")
            # return "No Search results"
    else:
        error="you don't have search history"
        # return "you not having search history"
    return render_template("history.html",error=error)

@app.route('/user/apply/<x>',methods=['GET'])
def apply(x):
    ''' In home latest jobs are shown when user request to show more details about latest job these method fetch 
    data about job description,apply link it showed in apply.html'''
    jobDetails = jobDetailsLoad.findJobDetails(x)
    return render_template('apply.html',job=jobDetails[0])

@app.route('/user/applys/<count>/<x>',methods=['GET'])
def applys(count,x):
    ''' In search result jobs are stored in database when user request the search history of job description,apply
    link the applys method fetch from database '''
    merge = session['user']['id']+str(int(count))
    jobDetails = jobDetailsLoad.findJobDetails(x,merge)
    return render_template('apply.html',job=jobDetails[0])

@app.route("/<job>")
def roleBasedJob(job):
    ''' These route method rol based job details from database '''
    # under process
    if job=="Full Stack Developer":
        jobs=jobLoad.fetchDefaultJob("defaultJob")
        return "coming soon sprint-3"
        # return render_template('dashboard.html',username='Guest',jobs=jobs,count="None")

if __name__ == "__main__":
    app.run('0.0.0.0',port=8080,debug=True)