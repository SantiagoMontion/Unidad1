from Menu import Menu
import os



if __name__=='__main__':
    Menu=Menu()

    enter=input("Presione enter para abrir el Menu. (Cualquier otra tecla para salir)")
    os.system('cls')

    while enter=='':
        
        
        print("1. Mostrar la cantidad total de kilos descargados.\n")
        print("2. Mostrar Listado\n")
        print("3. Cargar Cosechas\n")
        op=str(input("Seleccione una opcion: ")).lower()
        os.system('cls')
        Menu.opcion(op)

        enter=input("Presione enter para abrir el Menu. (Cualquier otra tecla para salir)")


    