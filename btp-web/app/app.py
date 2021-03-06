from flask import Flask, request, redirect, render_template, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config.from_object(os.environ["APP_SETTINGS"])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from models import tmpUsers
from forms import RegistrationForm, LoginForm
from functions import user_check


@app.route("/")
def root():
    return redirect(url_for("login"))

@app.route("/login", methods=['GET','POST'])
def login():
    failed = request.args.get('failed')
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        if not user_check(form.username.data):
            return redirect(url_for('login', failed=True))
        #check
        flash("Logged In")
        return redirect(url_for("registeredlist"))
    return render_template('unauth/login/login.html', form=form, failed_login=failed)

@app.route("/register", methods=["GET", "POST"])
def register():
    failed = request.args.get('failed')
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate():
        if user_check(form.username.data):
            return redirect(url_for('register', failed=True))
        tmpUsers.insert(name=form.username.data)
        flash("Thanks for registering")
        return redirect(url_for("registeredlist"))
    return render_template("unauth/register/register.html", form=form, failed_registration=failed)


@app.route("/registeredlist", methods=["GET"])
def registeredlist():
    users = tmpUsers.get()
    users = [user.name for user in users]
    print(users)
    return render_template("unauth/register/list.html", users=users)

@app.route("/home", methods=["GET"])
def home():
    return render_template("auth/home/home.html")
