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

stores = [{"name": "My Store", "items": [{"name": "my item", "price": 15.99}]}]


@app.route("/")
def home():
    return render_template("index.html")


# post /store data: {name :}
@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return jsonify(new_store)
    # pass


# get /store/<name> data: {name :}
@app.route("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
    return jsonify({"message": "store not found"})
    # pass


# get /store
@app.route("/store")
def get_stores():
    return jsonify({"stores": stores})
    # pass


# post /store/<name> data: {name :}
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return jsonify(new_item)
    return jsonify({"message": "store not found"})
    # pass


# get /store/<name>/item data: {name :}
@app.route("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({"items": store["items"]})
    return jsonify({"message": "store not found"})


app.run(debug=True, host="0.0.0.0")
