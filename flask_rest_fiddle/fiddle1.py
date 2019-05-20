from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

employee_dict = {}


class EmployeeList(Resource):
    def get(self):
        return employee_dict


class Employee(Resource):
    def get(self, id):
        try:
            return {id: employee_dict[id]}
        except KeyError:
            return {'message': 'Not Found'}, 404

    def post(self, id):
        try:
            employee_dict[id] = request.form['data']
        except KeyError:
            return {'message': 'Not Found'}, 404
        return {id: request.form['data']}, 201


api.add_resource(EmployeeList, '/')
api.add_resource(Employee, '/<int:id>')
if __name__ == '__main__':
    app.run(debug=True)
