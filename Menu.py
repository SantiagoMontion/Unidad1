
from ClaseFechaHora import FechaHora

class Menu:
    __switcher=None

    def __init__(self):
        self.__switcher = { 
            1:self.opcion1,
            2:self.opcion2,
            3:self.opcion3,
            0:self.salir
            }

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print('Salir')

    def formulario(self):
        print("---Ingrese la Primera Fecha---")
        d=int(input("\nIngrese Dia: "))
        mes=int(input("\nIngrese Mes: "))
        a=int(input("\nIngrese Año: "))
        h=int(input("\nIngrese Hora: "))
        m=int(input("\nIngrese Minutos: "))
        s=int(input("\nIngrese Segundos: "))
        Fecha1=FechaHora(d,mes,a,h,m,s)
        print("\n---Ingrese la Segunda Fecha---")
        d=int(input("\nIngrese Dia: "))
        mes=int(input("\nIngrese Mes: "))
        a=int(input("\nIngrese Año: "))
        h=int(input("\nIngrese Hora: "))
        m=int(input("\nIngrese Minutos: "))
        s=int(input("\nIngrese Segundos: "))
        Fecha2=FechaHora(d,mes,a,h,m,s)
        return Fecha1,Fecha2

    def opcion1(self):
        f1,f2=self.formulario()
        suma=f1 + f2
        suma.check()
        print("-----Resultado-----")
        suma.Mostrar()


    def opcion2(self):
        f1,f2=self.formulario()
        resta=f1 - f2
        resta.check()
        print("-----Resultado-----")
        resta.Mostrar()

    def opcion3(self):
        f1,f2=self.formulario()
        mayor=f1>f2
        print("-----Resultado-----")
        print("\nLa fecha mayor es:  ")
        mayor.Mostrar()
        



    def Test(self):
        f1=FechaHora(1,1,1,1,1,60)
        f2=FechaHora(5,6,2020,1,0,0)
        suma=f1+f2
        suma.check()
        print("-----Resultado-----")
        suma.Mostrar()   #6,7,2021,1,2,0

        resta=f1 - f2
        resta.check()
        print("-----Resultado-----")
        resta.Mostrar()

        mayor=f1>f2
        print("-----Resultado-----")
        print("\nLa fecha mayor es:  ")
        mayor.Mostrar()





