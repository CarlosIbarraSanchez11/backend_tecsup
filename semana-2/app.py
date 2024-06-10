import os
from flask import Flask, jsonify
from config import Config
from extensions import db, migrate
from flask_cors import CORS
from blueprints.users.routes import users_bp
from blueprints.products.routes import products_bp


app = Flask(__name__)  # Crear una instancia de la aplicación Flask
app.config.from_object(Config)

CORS(app)

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(users_bp) #vinculamos nuestro user_bp con nuestro app.py
app.register_blueprint(products_bp)

# users =[] # ya no nos vamos a conectar a un array, sino a una base de datos

@app.route('/')
def home():
    return jsonify([])

if __name__ == '__main__':
    with app.app_context(): # Necesario para que el sqlAlchemy acceda a la base de datos
        db.create_all() # si exiten en la base de datos, no pasa nada. Si no existen lo crea
    app.run(port=5000, debug=True)  # Ejecutar la aplicación en modo de depuración

