from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'Thisissecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\rain1\SQLite3\TestDB.db'
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))




class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])


@app.route("/", methods=['GET', 'POST'])
def index():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.password.data:
                return redirect(url_for('greet'))
        return '<h1>Invalid username of password</h1>'
    return render_template("index.html", form=form)


@app.route("/registration", methods=['GET', 'POST'])
def registration():
    form = RegisterForm()

    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('greet'))
        #return '<h1>' + form.username.data + '' + form.email.data + '' + form.password.data + '</h1>'
    return render_template("registration.html", form=form)


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