#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route("/")  # 'http://www.google.com/'
def home():
    return "<b>This text is bold</b>"


app.run(debug=True, host='0.0.0.0')
