import os
from Menu import Menu


if __name__=='__main__':
    Menu=Menu()
    num=int(input("Ingrese un numero de viajero frecuente "))

    while num!=0:
        
        print("\na- Consultar Cantidad de Millas.\n")
        print("b- Acumular Millas.\n")
        print("c- Canjear Millas.\n")
        op=str(input("Seleccione una opcion: ")).lower()
        os.system('cls')
        Menu.opcion(op,num)
        

        
        num=int(input("\nIngrese otro numero o 0 para finalizar "))
