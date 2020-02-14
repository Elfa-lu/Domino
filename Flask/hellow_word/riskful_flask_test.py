# ========== 1. basic REST API using Flask ===============

# get/post
# provide parameters to the url
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # how to extract the content from a post
    # maybe can be used to process the data/ validate the data
    # maybe process in backends and return some results
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'you sent' : some_json}), 201
    else:
        return jsonify({'about': 'Hello World'})


# create endpoints that accepts values that you need further process
## cmd: curl http://127.0.0.1:5000/multi/10
## return  result: 100
@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
    return jsonify({'result': num*10})

if __name__ == '__main__':
    app.run(debug=True)


# =================== 2. REST API using Flask-Restful =================
# https://flask-restful.readthedocs.io/en/latest/quickstart.html
# better code maintainence

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'about': 'Hello World!'}

    def post(self):
        some_json = request.get_json()
        return {'you sent': some_json}, 201

class Multi(Resource):
    def get(self, num):
        return {'result': num*10}

# don't have to keep decorating all the functions with the different routes
api.add_resource(HelloWorld, '/')
api.add_resource(Multi, 'multi/<int:num>')

if __name__ == '__main__':
    app.run(debug=True)
