#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///mytestdb.db"
db = SQLAlchemy(app)

class Present(db.Model):
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
    taken = db.Column(db.Boolean, unique=False, nullable=False)

    def __repr__(self):
        return "%r" % (self.name)

@app.route("/", methods=["GET"])
def root_view():
    return render_template("index.html", \
            presents=Present.query.filter_by(taken=False))

@app.route("/", methods=["POST"])
def root_post():
    params = request.form
    if "present" not in params or params["present"] == "":
        return "ERROR: Missing param\n"
    Present.query.filter_by(name=params['present']) \
           .update({ "taken" : True })
    db.session.commit()
    return ("Chose {}\n".format(params["present"]))

def dbinit():
    db.create_all()
    if len(Present.query.all()) < 1:
        available_presents = [ Present(name="kassi", description="Hieno kassi", taken=False),
                               Present(name="lusikka", description="Puurolusikka", taken=False),
                               Present(name="sushi", description="Nakkisushi", taken=False),
                               Present(name="kieli", description="Jaappanian alkeet", taken=False),
                               Present(name="tutti", description="Huvitutti", taken=False),
                               Present(name="matka", description="New Yorkin matka", taken=False),
                               Present(name="poni", description="Poni", taken=False)
                             ]
        db.session.add_all(available_presents)
        db.session.commit()

if __name__ == '__main__':
    dbinit()
    app.run(debug=True, use_reloader=True, host="127.0.0.1")

