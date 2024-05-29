# Escribir un programa que calcule el area de un circulo
# Area = pi * radio al cuadrado

import math
try:
    radio = float(input("Ingrese el radio: "))
    area = math.pi * radio ** 2
    print(f"El área del cirsulo es: {area}")    

except Exception as e:
    print(f"Error: {e}")

