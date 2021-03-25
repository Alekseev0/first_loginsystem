from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'Thisissecretkey111'
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\rain1\SQLite3\database.db'
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))



@app.route("/", methods=['GET', 'POST'])
def index():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            return redirect(url_for('greet'))
        if not user:
            msg = 'User is not created'
    elif request.method == 'POST':
        msg = 'Please fill out the form!'

    return render_template("index.html", msg=msg)


@app.route("/registration", methods=['GET', 'POST'])
def registration():
    msg = ''
    if request.method == 'POST' and 'userName' in request.form and 'password' in request.form and 'email' in request.form:
        name = request.form.get('userName')
        password = request.form.get('password')
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()

        if user:
            msg = 'Account already exists!'
        else:
            new_user = User(name=name, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('registration.html', msg=msg)




@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/greet")
def greet():
    return render_template("greet.html", login=request.args.get("login", "gaylord"))




if __name__ == '__main__':
   app.run()


#*********************************************
#*********************************************
#*********************************************


# ALEKSEEV INC.


#*********************************************
#*********************************************
#*********************************************