from ClaseAlumno import Alumno
import csv
class Manejador:
    __lista=[]

    def __init__(self):
        archivo=open("listadoalumnos.csv")
        reader=csv.reader(archivo,delimiter=",")
        
        for fila in reader:

            A=Alumno(fila[0],fila[1],fila[2],fila[3])
            self.__lista.append(A)

        archivo.close()

    def Listar(self,anio,div):
        print("{}{}".format("Alumno".ljust(24),"Porcentaje".center(14)))
        
        for i in range(len(self.__lista)):
            if str(self.__lista[i].getdivision()) == str(div) and int(self.__lista[i].getanio()) == anio:
                if int(self.__lista[i].getinasist())>int(self.__lista[i].getcantmaxinasist()):
                    porcentaje=(int(self.__lista[i].getinasist())*100)/self.__lista[i].getcantmaxinasist()
                    print("{}{:.2f}%".format(str(self.__lista[i].getnombre()).ljust(24),float(porcentaje)))
                    
            
                else:
                    print("\nNingun alumno cumple las condiciones")


    def Modificarinasistencias(self):
        nueva=int(input("Ingrese la nueva cantidad: "))
        for i in self.__lista:
            i.modificarcantmax(nueva)
            
