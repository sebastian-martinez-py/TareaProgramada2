
import data_handler

def mostrar_menu():
    while True:
        print("\nMenú Principal")
        print("1. Cargar datos")
        print("2. Buscar datos")
        print("3. Listar llaves")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            archivo = input("Ingrese el nombre del archivo CSV (incluya la extensión .csv): ")
            data_handler.cargar_datos(archivo)


        elif opcion == "2":
            try:
                key = int(input("Ingrese la llave (0-749): "))
                data_handler.buscar_datos(key)
            except ValueError:
                print("Error: La llave debe ser un número entero entre 0 y 749.")


        elif opcion == "3":  
            data_handler.listar_llaves()  


        elif opcion == "4":
            print("Saliendo del programa...")
            break


        else:
            print("Opción no válida. Intente de nuevo.")
            

if __name__ == "__main__":
    mostrar_menu()
