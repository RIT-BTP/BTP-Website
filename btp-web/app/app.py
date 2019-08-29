
from flask import Flask, request, redirect, render_template, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import tmpUsers
from forms import RegistrationForm

@app.route("/")
def root():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = tmpUsers.insert(name=form.username.data)
        flash('Thanks for registering')
        return redirect(url_for('root'))
    return render_template('register/register.html', form=form)
