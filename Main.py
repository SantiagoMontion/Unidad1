from Menu import Menu
import os
def muestraopciones():
    print("\na- Listado y porcentaje por alumno ")
    print("\nb- Modificar la cantidad máxima de inasistencias permitidas ")

if __name__=='__main__':
    Menu=Menu()
    muestraopciones()
    op=str(input("\nSeleccione un opcion: (0 para salir)" )).lower()
    while op!='0':
        os.system('cls')
        Menu.opcion(op)
        muestraopciones()
        op=str(input("\nSeleccione otra opcion: (0 para salir)")).lower()
        