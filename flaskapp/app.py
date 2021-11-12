from typing import ValuesView
from flask import Flask, request
from flask import render_template
from flask_wtf.csrf import CSRFProtect
#import pymssql
from forms import Loginform
#from app import app
import cgi


app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"
app.config['WTF_CSRF_SECRET_KEY'] = "secretkey"
csrf = CSRFProtect(app)
csrf.init_app(app)


@app.route('/')
def index():
    loginform = Loginform()
    return render_template('index.html', loginform=loginform)

@app.route('/login/',methods =['POST',])
def login():
    loginform=Loginform(request.form)
    formdata=cgi.FieldStorage()
    dat=formdata.getvalue('username')
    if not loginform.validate_on_submit():
        return "ERROR"
    return print(dat)

if __name__ == "__main__":
    app.run(debug=True)