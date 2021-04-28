from ClaseViajeroFrecuente import ViajeroFrecuente
import csv

class Manejador:
    __lista=[]


    def __init__(self):
        self.__lista=[]


    def CargarLista(self):
        archivo=open("Lista.csv")
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            V=ViajeroFrecuente(fila[0],fila[1],fila[2],fila[3],fila[4])
            self.__lista.append(V)


    def ConsultaMillas(self,i):
        if i-1 <=len(self.__lista):
            return self.__lista[i-1].CantMillasAcum()
        else:
            print("\nEl viajero ingresado no se encuentra registrado")

    def Acumular(self,i,millas):
        if i-1 <=len(self.__lista):
            self.__lista[i-1].AcumularMillas(millas)
        else:
            print("\nEl viajero ingresado no se encuentra registrado")

    def Canjear(self,i,millas):
        if i-1 <=len(self.__lista):
            self.__lista[i-1].CanjearMillas(millas)
        else:
            print("\nEl viajero ingresado no se encuentra registrado")
        
        
