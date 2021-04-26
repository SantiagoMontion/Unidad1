from ClaseIntegrantes import Integrantes
import csv

class ManejadorIntegrantes:
    __lista=[]

    def __init__(self):
        self.__lista=[]

    def CargarIntegrantes(self):
        archivo=open("integrantesProyecto.csv")
        reader=csv.reader(archivo,delimiter=';')

        for fila in reader:
            I=Integrantes(fila[0],fila[1],fila[2],fila[3],fila[4])
            self.__lista.append(I)

        archivo.close()


    def Contador(self,id):
        cont=0
        for i in range(len(self.__lista)):
            if self.__lista[i].getid() == id:
                cont+=1

        return cont


    def BuscarDirector(self,id):
        bandera=False
        director=False
        for i in range(len(self.__lista)):
            if self.__lista[i].getrol()== 'director' and director==False:
                director=True
            if self.__lista[i].getid() == id and self.__lista[i].getrol()== 'director' and bandera==False:
                if self.__lista[i].getcategoria()== 'I' or self.__lista[i].getcategoria()=='II':
                    bandera=True

        return bandera,director


    def BuscarCoDirector(self,id):
        bandera=False
        codirector=False
        for i in range(len(self.__lista)):
            if self.__lista[i].getrol()== 'director' and codirector==False:
                codirector=True

        
            if self.__lista[i].getid() == id and self.__lista[i].getrol()== 'codirector' and bandera==False:
                if self.__lista[i].getcategoria()== 'I' or self.__lista[i].getcategoria()=='II' or self.__lista[i].getcategoria()=='III':
                    bandera=True

        return bandera,codirector


