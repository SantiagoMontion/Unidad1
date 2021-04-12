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
        return self.__lista[i-1].CantMillasAcum()

    def Acumular(self,i,millas):
        self.__lista[i-1].AcumularMillas(millas)

    def Canjear(self,i,millas):
        self.__lista[i-1].CanjearMillas(millas)
