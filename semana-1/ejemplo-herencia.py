class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def saludar(self):
        return f"Hola, me llamo {self.nombre} {self.apellido}"
        
class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, carrera):
        super().__init__(nombre, apellido, edad)
        self.carrera = carrera

    def obtener_carrera(self):
        return f"Mi nombre es {self.nombre} y estudio {self.carrera}"

estudiante1 = Estudiante("Pepe", "Perez", 29, "Ing. Software")
print(estudiante1.saludar())
print(estudiante1.obtener_carrera())

def crear_usuario(nombre, apellido, correo, password, direccion, pais, ciudad, dni):
    return f"{nombre} {apellido} {correo} {password} {direccion} {pais} {ciudad} {dni}"

crear_usuario("Pepe", "Perez", "pepe3hs", "pepe@gmail.com", "pepe123", "Av. la libertad", "Perú", "Lima", "72317018")

crear_usuario("Lucho", "Perez", "luis3sh", "lucho@gmail.com", "lucho123", "Av. la libertad", "Chile", "Santiago", "72317009")

def crear_usuario2(user):
    return user

# Diccionario
crear_usuario2({
    "nombre": "Pepe",
    "apellido": "Perez",
    "username" : "pepe3hs"
})

# 2:19