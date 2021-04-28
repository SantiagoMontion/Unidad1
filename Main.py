from Menu import Menu
import os

def Opciones():
    print("\n1- Sumar Horas")
    print("\n2- Restar Horas")
    print("\n3- Definir Mayor")



def test(Menu):
    Menu.Test()

if __name__=='__main__':
    Menu=Menu()

    Opciones()

    op=int(input("\nSeleccione un opcion: (0 para salir)" ))
    while op!=0:
        os.system('cls')
        Menu.opcion(op)
        Opciones()
        op=int(input("\nSeleccione otra opcion: (0 para salir)"))


    test(Menu)
        
