from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True)
    age = db.Column(db.Integer, index=True)
    address = db.Column(db.String(256))
    city = db.Column(db.String(256))
    state = db.Column(db.String(256))
    zip = db.Column(db.String(256))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(120))

    def to_dict(self):
        return {
            'first_name': self.first_name,
            # 'last_name': self.last_name,
            'age': self.age,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zip': self.zip,

            'phone': self.phone,
            'email': self.email

        }

db.create_all()


@app.route('/')
def index():
    return render_template('ajax_table.html', title='Ajax Table')


@app.route('/api/data')
def data():
    return {'data': [user.to_dict() for user in User.query]}


if __name__ == '__main__':
    app.run()
