import csv
from ManejadorCamiones import ManejadorCamiones

class Cosecha:
    __lista=[]
    __M=None
    def __init__(self):
        self.__lista = [[0 for i in range(45)] for y in range(20)] 
        self.__M=ManejadorCamiones()

    def RegistrarCosechas(self,id,dia,peso):
        self.__lista[id][dia]=int(peso)
        self.guardarenarchivo(id+1,dia+1,peso)

    
    def CargarCosechas(self):
        archivo=open("C:/Users/Montion/Desktop/Facultad/POO/Unidad2/Repositorio/Ejercicio3/Cosechas.csv")
        reader=csv.reader(archivo,delimiter=',')

        for fila in reader:
            self.__lista[int(fila[0])-1][int(fila[1])-1]=float(fila[2])
        


    def Obtenerkilosdescargados(self,i):
        
        self.__M.CargarCamiones()
        tara=float(self.__M.getpesovacio(i))
        kilos=0.0
        for j in range(45):
            kilos+=self.__lista[i][j]
        return kilos-tara


    def guardarenarchivo(self,id,dia,peso):
        datos=str(id)+","+str(dia)+","+str(peso)+"\n"
        archivo=open("C:/Users/Montion/Desktop/Facultad/POO/Unidad2/Repositorio/Ejercicio3/Cosechas.csv",'a')
        archivo.write(datos)


    def Mostrarlistado(self,dia):
        self.__M.CargarCamiones()
        kilos=0.0
        print("{}{}{}".format("PATENTE".ljust(10),"CONDUCTOR".center(30),"CANTIDAD DE KILOS".rjust(15)))
        for i in range(20):

            print("{}{}{}".format(self.__M.getpatente(i).ljust(10),self.__M.getnombre(i).center(30),str(self.__lista[i][dia]).rjust(15)))
            

        
