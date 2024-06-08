import os
from flask import Flask, jsonify, request
from utils import encrypt_password
from config import Config
from extensions import db, migrate
from entities.users_model import User

app = Flask(__name__)  # Crear una instancia de la aplicación Flask
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

# users =[] # ya no nos vamos a conectar a un array, sino a una base de datos

@app.route('/')
def home():
    return jsonify([])

# Get
@app.route('/api/v1/user')
def get_all_users():
    try:
        users = User.query.all()
        dic_users = []
        for user in users:
            dic_users.append(user.to_dic())
        return jsonify({
            'users': dic_users
        })
    except Exception as e:
        return jsonify({
            "error" : e,
            "linea" : e.__traceback__.tb_lineno
        }), 500
# Get by user id
@app.route('/api/v1/user/<int: user_id>')
def get_user_by_id(user_id):
    try:
        # Buscamos al usuario por el Id
        user = User.query.get(user_id)
        if user is None:
            return jsonify({
                "message" : "user not found"
            })
        return jsonify({
            "user": user.to_dic()
        })
    except Exception as e:
        return jsonify({
            "error": e,
            "linea": e.__traceback__.tb_lineno
        }),500

# Post
@app.route('/api/v1/user', methods=['POST'])
def create_user():
    user_data = request.get_json()
    # user_data['password'] = encrypt_password(request.get_data('password'))
    user_data['password'] = encrypt_password(user_data.get('password')).decode('utf-8')

    new_user = User(
        full_name = f"{user_data.get('name')} {user_data.get('lastname')}",
        email = user_data.get('email') ,
        password = user_data.get('password'), 
        phoneNumber = user_data.get('phone_number'),
        genre = user_data.get('genre')
        # full_name = "Carlos",
        # email = "carlos@gmail.com" ,
        # password = "123456", 
        # phoneNumber = "921872052",
        # genre = "Male"
    )

    db.session.add(new_user)
    db.session.commit()
    # print(user_data)
    # users.append(user_data)
    return jsonify({
        "new_user": user_data
    })

if __name__ == '__main__':
    with app.app_context(): # Necesario para que el sqlAlchemy acceda a la base de datos
        db.create_all()
    app.run(port=5000, debug=True)  # Ejecutar la aplicación en modo de depuración

