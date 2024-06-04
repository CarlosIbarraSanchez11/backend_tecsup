def calcular_promedio(numeros):
    if len(numeros) == 0:
        return 0  # Evitar división por cero si la lista está vacía
    return sum(numeros) / len(numeros)

# Ejemplo de uso
numeros = [5, 2, 9, 1, 5, 6]
promedio = calcular_promedio(numeros)
print("El promedio es:", promedio)