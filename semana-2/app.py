from flask import Flask, jsonify, request
import bcrypt

app = Flask(__name__)  # Crear una instancia de la aplicación Flask

users =[]

def encrypt_password(password):
    # Generar un salt(es un numero aleatorio que se genera y es concatenado al password)
    # esto se usa por seguridad y evitar ataques de fuerza bruta
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

@app.route('/')
def home():
    # datos2 = {
    #     "carros": [
    #         {
    #             "id": 1,
    #             "marca": "Toyota",
    #             "modelo": "Corolla"
    #         },
    #         {
    #             "id": 2,
    #             "marca": "Honda",
    #             "modelo": "Civic"
    #         },
    #         {
    #             "id": 3,
    #             "marca": "Ford",
    #             "modelo": "Mustang"
    #         },
    #         {
    #             "id": 4,
    #             "marca": "Chevrolet",
    #             "modelo": "Camaro"
    #         },
    #         {
    #             "id": 5,
    #             "marca": "BMW",
    #             "modelo": "M3"
    #         }
    #     ]
    # }
    # return jsonify(datos2)
    return jsonify(users)
    # datos ={
    #     "celulares":[
    #         {
    #             "id" : 1,
    #             "marca": "apple",
    #             "modelo": "iPhone14"
    #         },
    #         {
    #             "id" : 2, 
    #             "marca": "Samsung",
    #             "modelo": "A34"
    #         },
    #         {
    #             "id" : 3,
    #             "marca": "Redmi",
    #             "modelo": "Nova 11"
    #         }
    #     ]
    # }

    # return jsonify(datos)
    # return jsonify({
    #     "message" : "Hola mundo desde Flask"
    # })
    #return "Hola mundo desde Flask"  # Definir la función para la ruta raíz
@app.route('/api/v1/user', methods=['POST'])
def create_user():
    user_data = request.get_json()
    # user_data['password'] = encrypt_password(request.get_data('password'))
    user_data['password'] = encrypt_password(user_data.get('password')).decode('utf-8')
    # print(user_data)
    users.append(user_data)
    return jsonify({
        "new_user": user_data
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)  # Ejecutar la aplicación en modo de depuración

# 02:00:34