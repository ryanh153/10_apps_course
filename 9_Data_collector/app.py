from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

from send_email import send_email


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/height_collector'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://sjnjsdvsyvmsow" \
                                        ":76ac0b3cef08d708dee0a900ebaf78398d2037c5f51954aecc17545c73f89d68@ec2-54-211" \
                                        "-210-149.compute-1.amazonaws.com:5432/d2ritkfr4q97ul?sslmode=require"
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    height = db.Column(db.Integer)

    def __init__(self, email, height):
        self.email = email
        self.height = height


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email_name"]
        height = request.form["height_val"]
        if db.session.query(Data).filter(Data.email == email).count() == 0:  # new e-mail
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()
            average_height = db.session.query(func.avg(Data.height)).scalar()
            average_height = round(average_height, 1)
            count = db.session.query(Data.height).count()
            send_email(email, height, average_height, count)
            return render_template('success.html')
        return render_template('index.html', text='E-mail already stored in database! Please enter a new e-mail')


if __name__ == '__main__':
    app.debug = True
    app.run()
