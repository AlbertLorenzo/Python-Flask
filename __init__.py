from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import loads, dumps
import __modules__

# Init app
app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/articlesdb'
mongo = PyMongo(app)

# Índice
@app.route('/', methods=['GET'])
def home_page():
    return 'Índice'

# Rutas para usuarios
@app.route('/users/fetch-all-users', methods=['GET'])
def feth_all_users():
    all_users = mongo.db.users.find({})
    return render_template('index.html', all_users=dumps(all_users))


@app.route('/users/create-user', methods=['POST'])
def create_user():
    data = request.get_json()
    if __modules__.data_is_not_empty(data):
        mongo.db.users.insert_one(
            # TODO
        )
        return jsonify({'Check': True, 'message': 'Usuario Eliminado'}), 200
    else:
        return jsonify({'Check': False, 'message': 'Se ha encontrado algún error en la petición'}), 400


@app.route('/users/delete-user/<id>', methods=['DELETE'])
def delete_user():
    data = request.get_json()
    if __modules__.data_is_not_empty(data):
        mongo.db.users.delete_one(
            # TODO
        )
        return jsonify({'Check': True, 'message': 'Usuario Eliminado'}), 200
    else:
        return jsonify({'Check': False, 'message': 'Se ha encontrado algún error en la petición'}), 400


@app.route('/users/update-user/<id>', methods=['PUT'])
def update_user():
    data = request.get_json()
    if __modules__.data_is_not_empty(data):
        mongo.db.users.update_one(
            # TODO
        )
        return jsonify({'Check': True, 'message': 'Usuario actualizado'}), 200
    else:
        return jsonify({'Check': False, 'message': 'Se ha encontrado algún error en la petición'}), 400

# Otras rutas


# Servidor
if __name__ == '__main__':
    app.run(port=3000, debug=True)
