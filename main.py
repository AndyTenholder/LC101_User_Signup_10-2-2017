from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def index():
    return render_template('user-signup.html')

@app.route("/", methods=['POST'])
def signin():
    password_error = ""
    verify_error = ""
    username_error = ""
    email_error = ""

    password = request.form['password']
    verify = request.form['verify']
    username = request.form['username']
    email = request.form['email']


    if password == "":
        password_error = "Need password"
    
    if username == "":
        username_error = "Need username"
    

    if len(password)<3 or len(password)>20 or  (" " in password):
        password_error = "Enter valid password: 2>password<20 & no spaces"
    

    if not password==verify:
        verify_error = "passwords do not match"
    

    if not email == "":
        if not ("@" in email) or not ('.' in email) or len(email)<3 or len(email)>20:
            email_error = 'Enter valid email'
    

    return render_template('user-signup.html', email = email, username = username, 
                            username_error = username_error, password_error= password_error,
                            verify_error = verify_error, email_error = email_error)

app.run()