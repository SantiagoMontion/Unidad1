from ManejadorViajeros import Manejador

def menu():
    print("\na- Consultar Cantidad de Millas.\n")
    print("b- Acumular Millas.\n")
    print("c- Canjear Millas.\n")
    op=input("Seleccione una opcion: ")
    return op

if __name__=='__main__':
    M=Manejador()
    M.CargarLista()

    num=int(input("Ingrese un numero de viajero frecuente "))

    while num!=0:
        opcion=str(menu()).lower()
        
        if opcion=='a':
            print("La Cantidad de Millas es: {}".format(M.ConsultaMillas(num)))

        elif opcion=='b':
            millas=int(input("Ingrese La cantidad de millas para acumular "))
            M.Acumular(num,millas)

        elif opcion =='c':
            millas=int(input("Ingrese La cantidad de millas para canjear "))
            M.Canjear(num,millas)
        
        else:
            print("Opcion inocrrecta\n")

        
        num=int(input("\nIngrese otro numero o 0 para finalizar "))