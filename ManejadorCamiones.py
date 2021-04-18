from ClaseCamion import Camion
import csv

class ManejadorCamiones:
    __lista=[]

    def __init__(self):
        self.__lista=[]


    def CargarCamiones(self):
        archivo=open("Camiones.csv")
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            C=Camion(fila[0],fila[1],fila[2],fila[3],fila[4])
            self.__lista.append(C)

        archivo.close()


    def getpesovacio(self,id):
        return self.__lista[id].gettara()

    def getpatente(self,i):
        return self.__lista[i].getpatente()

    def getnombre(self,i):
        return self.__lista[i].getnombre()
