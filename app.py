#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///mytestdb.db"
db = SQLAlchemy(app)

class Present(db.Model):
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return "<Present %r>".format(self.present)

@app.route("/", methods=["GET"])
def root_view():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def root_post():
    params = request.form
    if "present" not in params or params["present"] == "":
        return "ERROR: Missing param\n"
    present = Present(name=params["present"])
    db.session.add(present)
    db.session.commit()
    return ("Chose {}\n".format(params["present"]))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host="127.0.0.1")
