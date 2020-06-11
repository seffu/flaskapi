from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


def checkposteddata(posteddata, func):
    if func == 'add' or func == 'subtract' or func == 'multiply':
        if 'x' not in posteddata or 'y' not in posteddata:
            return 301
        else:
            return 200

    elif func == 'divide':
        if 'x' not in posteddata or 'y' not in posteddata:
            return 301
        elif posteddata['y'] == 0:
            return 302
        else:
            return 200


class Add(Resource):
    def post(self):
        posteddata = request.get_json()
        status_code = checkposteddata(posteddata, 'add')
        if status_code != 200:
            retjson = {
                'Message': 'An error occured',
                'status Code': status_code
            }
            return jsonify(retjson)
        else:
            x = posteddata["x"]
            y = posteddata["y"]
            x = int(x)
            y = int(y)
            z = x + y
            retmap = {
                'Message': z,
                'Status Code': 200,
            }
            return jsonify(retmap)


class Subtract(Resource):
    def post(self):
        posteddata = request.get_json()
        status_code = checkposteddata(posteddata, 'subtract')
        if status_code != 200:
            retjson = {
                'Message': 'An error occured',
                'status Code': status_code
            }
            return jsonify(retjson)
        else:
            x = posteddata["x"]
            y = posteddata["y"]
            x = int(x)
            y = int(y)
            z = x - y
            retmap = {
                'Message': z,
                'Status Code': 200,
            }

            return jsonify(retmap)


class Multiply(Resource):
    def post(self):
        posteddata = request.get_json()
        status_code = checkposteddata(posteddata, 'multiply')
        if status_code != 200:
            retjson = {
                'Message': 'An error occured',
                'status Code': status_code
            }
            return jsonify(retjson)
        else:
            x = posteddata["x"]
            y = posteddata["y"]
            x = int(x)
            y = int(y)
            z = x * y
            retmap = {
                'Message': z,
                'Status Code': 200,
            }

            return jsonify(retmap)

class Divide(Resource):
    def post(self):
        posteddata = request.get_json()
        status_code = checkposteddata(posteddata, 'divide')
        if status_code == 302:
            retjson = {
                'Message': 'Div by 0 error',
                'status Code': status_code
            }
            return jsonify(retjson)
        elif status_code != 200:
            retjson = {
                'Message': 'An error occured',
                'status Code': status_code
            }
            return jsonify(retjson)
        else:
            x = posteddata["x"]
            y = posteddata["y"]
            x = int(x)
            y = int(y)
            z = x / y
            retmap = {
                'Message': z,
                'Status Code': 200,
            }
            return jsonify(retmap)


api.add_resource(Add, '/add')
api.add_resource(Subtract, '/subtract')
api.add_resource(Multiply, '/multiply')
api.add_resource(Divide, '/divide')


@app.route('/')
def index():
    return 'Welcome home'


if __name__ == '__main__':
    app.run(debug=True)
