from ClaseEmail import Email
import csv
import re

class ManejadorEmail:
    __lista=[]

    def __init__(self):
        self.__lista=[]


    def CargarLista(self):
        archivo=open("Listado.csv")
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            for j in range(10):
                correo=str(fila[j])
                if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
                    f=str(fila[j])
                    separado=f.split("@")
                    id=separado[0]
                    sep2=separado[1].split(".")
                    dominio=sep2[0]
                    tipo=sep2[1]
                    E=Email(id,dominio,tipo)
                    self.__lista.append(E)
                    
                else:
                    print ("Correo incorrecto")
        archivo.close()
        

        
    def BuscarDominio(self,dom):
        cont=0
        self.CargarLista()
        for i in range(len(self.__lista)):
            if str(self.__lista[i].getdominio())==str(dom):
                cont+=1

        print("La cantidad de cuentas con el dominio {} es de: {}".format(dom,cont))
