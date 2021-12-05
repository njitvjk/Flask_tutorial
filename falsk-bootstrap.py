from flask import Flask, render_template, flash, request, redirect, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    flash("message test")
    return render_template('dashboard.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('dashboard'))
    return render_template('dashboard.html', error=error)


if __name__ == '__main_':
    app.run(debug=True)
