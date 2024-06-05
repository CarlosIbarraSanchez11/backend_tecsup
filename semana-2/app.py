from flask import Flask, jsonify, request

app = Flask(__name__)  # Crear una instancia de la aplicación Flask

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
    datos ={
        "celulares":[
            {
                "id" : 1,
                "marca": "apple",
                "modelo": "iPhone14"
            },
            {
                "id" : 2,
                "marca": "Samsung",
                "modelo": "A34"
            },
            {
                "id" : 3,
                "marca": "Redmi",
                "modelo": "Nova 11"
            }
        ]
    }

    return jsonify(datos)
    # return jsonify({
    #     "message" : "Hola mundo desde Flask"
    # })
    #return "Hola mundo desde Flask"  # Definir la función para la ruta raíz
@app.route('/api/v1/user', methods=['POST'])
def create_user():
    user_data = request.get_json()
    print(user_data)
    return jsonify({
        "new_user": user_data
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)  # Ejecutar la aplicación en modo de depuración

# 02:00:34