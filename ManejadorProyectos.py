from ClaseProyecto import Proyecto
import csv

class ManejadorProyecto:
    __lista=[]

    def __init__(self):
        self.__lista=[]


    def CargarProyectos(self):
        archivo=open("proyectos.csv")
        
        reader=csv.reader(archivo,delimiter=';')

        for fila in reader:
            P=Proyecto(fila[0],fila[1],fila[2])
            self.__lista.append(P)

        archivo.close()


    def CalcularPuntos(self,MI):

        for i in range(len(self.__lista)):

            id=self.__lista[i].getid()
            cont=MI.Contador(id)

            if int(cont)>=3:
                self.__lista[i].CargarPuntos(10)

            elif int(cont)<3:
                self.__lista[i].CargarPuntos(-20)
                print("\nEl Proyecto {} debe tener como mínimo 3 integrantes.".format(id))

            bandera,director=MI.BuscarDirector(id)

            if bandera==True:
                self.__lista[i].CargarPuntos(10)
            elif bandera ==False:
                self.__lista[i].CargarPuntos(-5)
                print("\nEl Director del Proyecto {} debe tener categoría I o II.".format(id))


            bandera2,codirector=MI.BuscarCoDirector(id)

            if bandera2==True:
                self.__lista[i].CargarPuntos(10)
            elif bandera2 ==False:
                self.__lista[i].CargarPuntos(-5)
                print("\nEl Codirector del Proyecto {} debe tener como mínimo categoría III.".format(id))


            if director==False or codirector==False:
                self.__lista[i].CargarPuntos(-10)

            if  director==False:
                print("\nEl Proyecto {} debe tener un Director".format(id))
            
            if codirector==False:
                print("\nEl Proyecto {} debe tener un Codirector".format(id))



    def MostrarPuntos(self):
        self.ordenar()
        for i in range(len(self.__lista)):
            print("\nPosición {}".format(i+1))
            print("\nTitulo: {}    \nPuntos: {}".format(self.__lista[i].gettitulo(),self.__lista[i].getpuntos()))
            
            print("---------------------------------")



            


    def ordenar(self):
        for i in range(len(self.__lista)):
            
            for j in range(i+1,len(self.__lista)):

                if self.__lista[j]>self.__lista[i]:
                    
                    aux=self.__lista[i]
                    self.__lista[i]=self.__lista[j]
                    self.__lista[j]=aux


