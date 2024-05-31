# Escribir una funcion para contar las pablas

def contar_palabra(palabras):
    return len(palabras.split(" "))


# Hola como estas?
palabras = input("Ingrese algunas palabras: ")
print(contar_palabra(palabras))