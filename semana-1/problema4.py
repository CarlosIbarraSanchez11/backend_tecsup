# Escribir un texto que se invierta despues

# cadena = input("Ingresar texto que desea invertir: ")
# longitud = len(cadena)

# for letra in range(longitud -1, -1, -1):
#     print(letra)

cadena = input("Ingresar texto que desea invertir: ")
longitud = len(cadena)
cadena_invertida = ""

for letra in range(longitud - 1, -1, -1):
    cadena_invertida += cadena[letra]
print(cadena_invertida)