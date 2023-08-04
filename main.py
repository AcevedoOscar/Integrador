from clases import Veterinaria
import funciones


def progPrincipal():
    veterinaria = Veterinaria()
    print("Bienvenido a la veterinaria!")

    while True:
        print("\nOpciones:")
        print("1. Listar pacientes")
        print("2. Detalle de paciente")
        print("3. Cargar nuevo paciente")
        print("4. Quitar paciente")
        print("5. Cargar consulta")
        print("6. Dar de alta tratamiento médico")
        print("7. Salir")

        opcion = input("Ingrese el número de opción deseada: ")

        if opcion == "1":
            funciones.listarPacientes(veterinaria)

        elif opcion == "2":
            funciones.listarPacientes(veterinaria)
            paciente_idx = int(input("Ingrese el número de paciente deseado: ")) - 1
            pacientes = veterinaria.getListado()
            if 0 <= paciente_idx < len(pacientes):
                detalle_paciente = funciones.obtenerDetallePaciente(pacientes[paciente_idx])
                print("Detalle del paciente:")
                for key, value in detalle_paciente.items():
                    print(f"{key}: {value}")
            else:
                print("¡Número de paciente inválido!")

        elif opcion == "3":
            nombre = input("Ingrese el nombre del nuevo paciente: ")
            edad = int(input("Ingrese la edad del nuevo paciente: "))
            raza = input("Ingrese la raza del nuevo paciente: ")
            paciente_nuevo = funciones.nuevoPaciente(nombre, edad, raza)
            veterinaria.setPaciente(paciente_nuevo)
            print("Nuevo paciente agregado exitosamente.")

        elif opcion == "4":
            funciones.listarPacientes(veterinaria)
            paciente_idx = int(input("Ingrese el número de paciente a quitar: ")) - 1
            pacientes = veterinaria.getListado()
            if 0 <= paciente_idx < len(pacientes):
                funciones.quitarPaciente(veterinaria, pacientes[paciente_idx])
                print("Paciente eliminado exitosamente.")
            else:
                print("¡Número de paciente inválido!")

        elif opcion == "5":
            funciones.listarPacientes(veterinaria)
            paciente_idx = int(input("Ingrese el número de paciente para cargar consulta: ")) - 1
            pacientes = veterinaria.getListado()
            if 0 <= paciente_idx < len(pacientes):
                consulta = input("Ingrese el motivo de la consulta: ")
                funciones.nuevaConsulta(pacientes[paciente_idx], consulta)
                print("Consulta agregada exitosamente.")
            else:
                print("¡Número de paciente inválido!")

        elif opcion == "6":
            funciones.listarPacientes(veterinaria)
            paciente_idx = int(input("Ingrese el número de paciente para dar de alta el tratamiento médico: ")) - 1
            pacientes = veterinaria.getListado()
            if 0 <= paciente_idx < len(pacientes):
                paciente = pacientes[paciente_idx]
                paciente.paciente_con_tratamiento_medico = True
                print("Tratamiento médico dado de alta.")
            else:
                print("¡Número de paciente inválido!")

        elif opcion == "7":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break

        else:
            print("¡Opción inválida! Por favor, elija una opción válida.")


if __name__ == "__main__":
    progPrincipal()