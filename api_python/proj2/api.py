#!/usr/bin/env python3

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

technologies = []

# 404 NOT FOUND
# 201 CREATED
# 202 ACCEPTED (delaying the creation)(ie the creation takes a couple of minutes)


class Tech(Resource):
    def get(self, name):
        for tech in technologies:
            if tech["name"] == name:
                return tech
        return {"item": None}, 404

    def post(self, name):
        item = {"name": name, "cool factor": 1000}
        technologies.append(item)
        return item, 201


api.add_resource(Tech, "/tech/<string:name>")  # https://127.0.0.1:5000/tech/some_tech

app.run(debug=True, host="0.0.0.0")
