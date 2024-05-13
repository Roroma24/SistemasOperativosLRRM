"""
Aaron Hector Reyna Gomez
Giovanni Melo Garcia
Luis Roberto Rodriguez Marroquin
"""
import os
import subprocess

def ejecutar_comando(comando):
    subprocess.run(comando,shell=True)

def menu():
    print("1. Crear archivo 'holamundo.txt'")
    print("2. Crear carpeta 'Python'")
    print("3. Crear carpeta 'MisProgramas'")
    print("4. Listar el directorio actual")
    print("5. Copiar archivo 'holamundo.txt' a 'Python'")
    print("6. Eliminar la carpeta 'MisProgramas'")
    print("7. Localizar 'holamundo.txt")
    print("8. Localizar 'prueba.txt'")
    print("9. Salir")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            ejecutar_comando("touch holamundo.txt")
        elif opcion == '2':
            ejecutar_comando("mkdir Python")
        elif opcion == '3':
            ejecutar_comando("mkdir MisProgramas")
        elif opcion == '4':
            ejecutar_comando("ls")
        elif opcion == '5':
            ejecutar_comando("cp holamundo.txt Python")
        elif opcion == '6':
            ejecutar_comando("rmdir MisProgramas")
        elif opcion == '7':
            ejecutar_comando("find holamundo.txt")
        elif opcion == '8':
            ejecutar_comando("find prueba.txt")
        elif opcion == '9':
            break
        else:
            print("Opcion no valida. Por favor, seleccione una opcion valida.")

if __name__ == "__main__":
    main()
