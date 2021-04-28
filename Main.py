from Menu import Menu
import os

def test(o1,o2,o3,Menu):
    Menu.opcion(o1)
    Menu.opcion(o2)
    Menu.opcion(o3)


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


    test('1','2','3',Menu)


   
