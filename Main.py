from Menu import Menu
import os
from ClaseConjuto import Conjunto

def opciones():
    print("\n1- Unión de dos conjuntos ")
    print("\n2- Diferencia de dos conjuntos ")
    print("\n3- Verificar si dos conjuntos son iguales")
    op=int(input("\nSeleccione una opcion (0 para salir): "))
    return op
    

if __name__ == '__main__':
    Menu=Menu()
    C1=Conjunto()
    C2=Conjunto()
    C1.CargarConjunto()
    C2.CargarConjunto()
    op=int(opciones())
    
    while op!=0 :
        if op<4:
            os.system('cls')
            Menu.opcion(op,C1,C2)
            op=opciones()
        else:
            print("Opcion Incorrecta")
            op=opciones()
