from flask import Flask, redirect, request, render_template



app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def user_signup():
    
    if request.method=="POST":    
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']
    else:
        username = request.args.get('username')
        password = request.args.get('password')
        verify = request.args.get('verify')
        email = request.args.get('email')

    username_error1 = ''
    password_error1 = ''
    verify_error1 = ''
    email_error1 = ''

    new_user=""
    log =True
     
    if " " in username:
        username_error1 ="That's not a valid username"
        log=False
            
    elif len(str(username))>20 or len(str(username))< 3:
        username_error1 ="That's not a valid username"
        log=False
    else:
        new_user=username 
  
    if len(str(password))>20 or len(str(password))< 3:
        password_error1 ="That's not a valid password"
        log=False

    if " " in password:
        password_error1 = "That's not a valid password"
        log=False

    if password != verify:
        verify_error1 = "Passwords don't match" 
        log=False



    if email !="":
        if "@" not in email or "." not in email:
            email_error1 = "not valid"
            log=False

        if " " in email:
            email_error1 ='not valid'
            log=False
                
        if len(str(email))>20 or len(str(email))< 3:
            email_error1 ='not valid'
            log=False
        else:
            email=email
        
    if log==False:
                return render_template('login.html', username_error=username_error1,
                password_error=password_error1
                ,verify_error=verify_error1,email_error=email_error1)



    if log==True:
        return render_template('welcome.html', username=new_user)


app.run()