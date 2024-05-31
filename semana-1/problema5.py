# Escribir una funcion que reciba 3 numeros y mencione el maximo

# def max_de_tres(n1, n2, n3):
#     return max (n1, n2, n3)

# n1 = int (input("Ingrese el Número 1:" ))
# n2 = int (input("Ingrese el Número 2:" ))
# n3 = int (input("Ingrese el Número 3:" ))

# print (max_de_tres(n1,n2,n3))

numeros = input ("Ingrse los numeros separados por ,: ")

print(numeros.split(","))
n1,n2,n3 = numeros.split(",")
print(n1,n2,n3)