# Escribir si un numero es para o impar
try: 
    numero = int(input("Ingrese un número: "))

    mensaje = "Es un número imoar"

    if numero % 2 == 0:
        print("Es un Número par")
    else:
        print(mensaje)
except Exception as e:
    # print(e)
    print(f"Error: {e}")
  