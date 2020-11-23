#!/usr/bin/env python3

from flask import (
    Flask,
    jsonify,
    request,
)  # jsonify takes in a python dictionairy and converts to json

app = Flask(__name__)

# From the servers perspective
## POST - used to receive data
## GET - used to send data back only

# POST /foo data: {name:}
# GET /foo/<string:name>
# GET /store
# POST /store/<string:name>/item
# GET /store/<string:name>/item

# endpoing: @app.route('/')
# app.route by default is GET

bar = [{"foo": "hello", "boo": [{"name": "my item", "price": 10}]}]


@app.route("/")
def home():
    return "<b>cool cool cool, this is bold</b>\n<i> and this is ital</i>"


@app.route("/foo", methods=["POST"])
def create_foo():
    request_data = request.get_json()


@app.route("/bar<string:name>")  #'http://127.0.0.1:5000/bar/some_name'
def get_bar(name):
    pass


@app.route("/baz")
def get_baz():
    return jsonify({"bar": bar})


@app.route("/baz<string:name>/boo", methods=["POST"])
def create_baz():
    pass


app.run(debug=True, host="0.0.0.0")
