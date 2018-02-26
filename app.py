#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET"])
def root_view():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def root_post():
    params = request.form
    if "present" not in params or params["present"] == "":
        return "ERROR: Missing param\n"
    return ("Chose {}\n".format(params["present"]))

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1")
