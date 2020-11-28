#!/usr/bin/env python3

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Student(Resource):
    def get(self, name):
        return {"studen": name}


api.add_resource(
    Student, "/student/<string:name>"
)  # https://127.0.0.1:5000/student/some_name

app.run(debug=True, host="0.0.0.0")
