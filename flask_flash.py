from flask import Flask, render_template, flash

from content_management.Content import Content


app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("dashboard.html")
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.route('/dashboard/')
def dashboard( ):
    topic_dist = Content()
    flash("flash test!!!!")
    flash("fladfasdfsaassh test!!!!")
    flash("asdfas asfsafs!!!!")
    return render_template("dashboard.html", TOPIC_DICT=topic_dist)
