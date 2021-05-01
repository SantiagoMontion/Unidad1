from ClaseIntegrantes import Integrantes
import csv

class ManejadorIntegrantes:
    __lista=[]

    def __init__(self):
        self.__lista=[]

    def CargarIntegrantes(self):
        archivo=open("C:/Users/Montion/Desktop/Facultad/POO/Unidad2/Repositorio/EjercicioIntegrador/integrantesProyecto.csv")
        reader=csv.reader(archivo,delimiter=';')

        for fila in reader:
            if fila[2].isdigit()==True:
                I=Integrantes(fila[0],fila[1],fila[2],fila[3],fila[4])
            self.__lista.append(I)

        archivo.close()


    def Contador(self,id):
        cont=0
        if type(id)==str:
            for i in range(len(self.__lista)):
                if self.__lista[i].getid() == id:
                    cont+=1

        return int(cont)


    def BuscarDirector(self,id):
        bandera=False
        director=False
        if type(id)==str:
            
            for i in range(len(self.__lista)):
                if self.__lista[i].getid() == id and self.__lista[i].getrol()== 'director':
                    director=True
                    if self.__lista[i].getcategoria()== 'I' or self.__lista[i].getcategoria()=='II':
                        bandera=True

        return bandera,director


    def BuscarCoDirector(self,id):
        bandera=False
        codirector=False
        if type(id)==str:
            
            for i in range(len(self.__lista)):   
                if self.__lista[i].getid() == id and self.__lista[i].getrol()== 'codirector':
                    codirector=True
                    if self.__lista[i].getcategoria()== 'I' or self.__lista[i].getcategoria()=='II' or self.__lista[i].getcategoria()=='III':
                        bandera=True

        return bandera,codirector

        

    def CargarTest(self):
        self.CargarIntegrantes()
        I=Integrantes('1TEST','Santiago Montion','156728963','IV','integrante')
        I2=Integrantes('1TEST','Agusto Gomez','15583993','I','codirector')
        I3=Integrantes('1TEST','Juan Molina','154896453','IV','director')
        self.__lista.append(I)
        self.__lista.append(I2)
        self.__lista.append(I3)



