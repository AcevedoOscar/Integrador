class Veterinaria:
    def __init__(self):
        self.listado = []

    def setPaciente(self, paciente):
        self.listado.append(paciente)

    def deletePaciente(self, paciente):
        self.listado.remove(paciente)

    def getListado(self):
        return self.listado

    def __str__(self):
        return f"La veterinaria tiene {len(self.listado)} pacientes."


class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"


class Paciente(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza
        self.consultas = []
        self.paciente_con_tratamiento_medico = False

    def __str__(self):
        return f"{super().__str__()}, Raza: {self.raza}, Consultas: {len(self.consultas)}"

    def setConsulta(self, consulta):
        self.consultas.append(consulta)

    def getDatos(self):
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "raza": self.raza,
            "consultas": self.consultas,
            "paciente_con_tratamiento_medico": self.paciente_con_tratamiento_medico,
        }