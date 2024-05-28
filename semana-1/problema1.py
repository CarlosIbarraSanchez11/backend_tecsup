# Escribe un programa que retorne la suma de 2 numeros 

numero_1 = input("Ingresar número A: ")
numero_2 = input("Ingresar numero B: ")

print(type(numero_1), type(numero_2))

# Toda información llegar como 'str'
try:
    suma = int(numero_1) + int (numero_2)
    print(suma)
except Exception as e:
    print(e)