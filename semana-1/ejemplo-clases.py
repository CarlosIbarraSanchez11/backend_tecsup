# Las clases siemre de debe comenzar con mayusculas
class Persona:
    # Constructores __init__ Reservado para todas las clases
    def __init__(self, nombre, apellido, edad, altura, direccion, peso):
        # print(nombre, apellido,edad, altura, direccion, peso)
        
        # Vamos a agregar propiedades a self
        # sel.nombre_de_la_propiedad = valor
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = altura
        self.direccion = direccion
        self.peso = peso

    def saludar(self):
        return f"Hola me llamo {self.nombre} {self.apellido}, tengo {self.edad} años de edad, vivo en {self.direccion}"
    def obtener_direccion(self):
        return f"El joven vive en {self.direccion}"

# Para instancia una clase, debemos simplemente llamarla por su nombre y guardarla en una variable

persona1 = Persona("Pepe", "Perez", 29, 1.94, "av La libertad", 80.2)
print(persona1.saludar())
print(persona1.obtener_direccion())


# 1:06

