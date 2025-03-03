
import data_handler

def mostrar_menu():
    while True:
        print("\nMenú Principal")
        print("1. Cargar datos")
        print("2. Buscar datos") #Imprime las opciones del menu
        print("3. Listar llaves")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            archivo = input("Ingrese el nombre del archivo CSV (incluya la extensión .csv): ")#carga csv que da el usuario o carga el default  y lo lleva a info.dat
            data_handler.cargar_datos(archivo)


        elif opcion == "2":
            try:
                key = int(input("Ingrese la llave (0-749): "))
                data_handler.buscar_datos(key)#Indica si hay datos guardados en esa llave y si hay colisiones
            except ValueError:
                print("Error: La llave debe ser un número entero entre 0 y 749.")


        elif opcion == "3":  
            data_handler.listar_llaves()  #imprime las llaves que exiten y si tiene colisiones


        elif opcion == "4":
            print("Saliendo del programa...")
            #sale del programa
            break


        else:
            print("Opción no válida. Intente de nuevo.")#si se digita un numero que no esta en el menu 
            

if __name__ == "__main__":
    mostrar_menu()
