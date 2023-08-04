from clases import Veterinaria, Paciente


def nuevoPaciente(nombre, edad, raza):
    paciente = Paciente(nombre, edad, raza)
    return paciente


def quitarPaciente(veterinaria, paciente):
    veterinaria.deletePaciente(paciente)


def listarPacientes(veterinaria):
    pacientes = veterinaria.getListado()
    if not pacientes:
        print("No hay pacientes en la base de datos.")
    else:
        for idx, paciente in enumerate(pacientes, 1):
            print(f"{idx}. {paciente}")


def nuevaConsulta(paciente, consulta):
    paciente.setConsulta(consulta)


def obtenerDetallePaciente(paciente):
    return paciente.getDatos()