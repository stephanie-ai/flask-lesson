from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import dogs
from werkzeug import exceptions

server = Flask(__name__)
CORS(server)

@server.route('/')
def home():
    return jsonify({'message': 'Hello from Flask!'}), 200

@server.route('/api/dogs', methods=['GET', 'POST'])
def dogs_handler():
    fns = {
        'GET': dogs.index,
        'POST': dogs.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@server.route('/api/dogs/<int:dog_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def dog_handler(dog_id):
    fns = {
        'GET': dogs.show,
        'PATCH': dogs.update,
        'PUT': dogs.update,
        'DELETE': dogs.destroy
    }
    resp, code = fns[request.method](request, dog_id)
    return jsonify(resp, code)

@server.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@server.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

if __name__ == "__main__":
    server.run(debug=True)

