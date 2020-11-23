#!/usr/bin/env python3

from flask import (
    Flask,
    jsonify,
    request,
    render_template,
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
    return render_template("index.html")


@app.route("/foo", methods=["POST"])
def create_foo():
    request_data = request.get_json()
    some_new_foo = {"name": request_data["name"], "items": []}
    foo.append(some_new_foo)
    return jsonify({some_new_foo})


@app.route("/foo/<string:name>")  #'http://127.0.0.1:5000/bar/some_name'
def get_foo(name):
    # Iterate over stores
    for i in foo:
        if foo["name"] == name:
            return jsonify(bar)
    # if the store name matches, return it
    return jsonify({"message": "foo not found"})
    # if none match, return an error message


@app.route("/foo")
def get_foos():
    return jsonify({"bar": bar})


@app.route("/foo/<string:name>/bar", methods=["POST"])
def create_foo_in_bar(name):
    request_data = request.get_json()
    for i in foo:
        if foo["name"] == name:
            new_foo = {"name": request_data["name"], "foos": request_data["bar"]}
            foo["items"].append(new_item)
            return jsonify(new_item)
    return jsonify({"message": "foo not found"})


@app.route("/foo<string:name>/bar")
def get_bar_in_foo():
    for i in foo:
        if i["name"] == name:
            return jsonify({"item": store["items"]})
    return jsonify({"message": "foo not found"})


app.run(debug=True, host="0.0.0.0")
