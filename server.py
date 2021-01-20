from flask import Flask, jsonify, request, g, render_template
from flask_cors import CORS
from controllers import dogs
from werkzeug import exceptions
from db import get_db

server = Flask(__name__)
CORS(server)

@server.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with server.server_context():
        db = get_db()
        with server.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@server.route('/new', methods=['GET', 'POST'])
def new_dogs():
    db = get_db()
    cursor.db.cursor()

    if request.method == 'POST':
        name = request.form['name']
        breed = request.form['breed']
        owner = request.form['owner']
        cursor.execute(
            "INSERT INTO dogs (id, name, breed, owner) VALUES (? ? ?);",
            (2, name, breed, owner)
        )
        db.commit()
    
    cursor.execute("SELECT * from dogs")
    dogs = cursor.fetchall()

    return render_template("new.html", dogs=dogs)


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

