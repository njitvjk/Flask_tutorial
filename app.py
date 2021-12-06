import flask
from flask import Flask, render_template, flash, request, redirect, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
Bootstrap(app)


@app.route('/')
def index():
    # Here you could register the user.
    # Add them to a database, for example.
    return render_template("index.html")

@app.route('/dashboard',methods=['GET', 'POST'])
def dashboard():
    # flash("message test")
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            flash('Invalid credentials','danger')
        else:

            flash('You were successfully logged in','success')
            return redirect(url_for('index'))


    return render_template('dashboard.html',error=error)





