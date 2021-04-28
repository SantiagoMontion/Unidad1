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
            if fila[0].isdigit()==True and fila[4].isdigit()==True:
                C=Camion(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.__lista.append(C)
            

        archivo.close()


    def getpesovacio(self,id):
        if id<len(self.__lista):
            return self.__lista[id].gettara()
        else:
            print("Camion no registrado")

    def getpatente(self,i):
        if i<len(self.__lista):
            return self.__lista[i].getpatente()

    def getnombre(self,i):
        if i<len(self.__lista):
            return self.__lista[i].getnombre()
        else:
            print("Camion no registrado")
