def sum_digitos(numero):
    suma = 0
    for n in numero:
        suma += int(n)
    return suma

numero = input("Escrbia un numero: ")
print(sum_digitos(numero))