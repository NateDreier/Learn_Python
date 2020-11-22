#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route("/") 
def home():
    return "<b>cool cool cool, this is bold</b>\n <i>what is the soup of the day? soup du jour</i>"


app.run(debug=True, host='0.0.0.0')
