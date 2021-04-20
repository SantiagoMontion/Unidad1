
from ManejadorAlumnos import Manejador

class Menu:
    __switcher=None
    __M=None

    def __init__(self):
        self.__switcher = { 
            'a':self.opcion1,
            'b':self.opcion2,
            '0':self.salir
            }
        self.__M=Manejador()

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print('Salir')

    def opcion1(self):
        anio=int(input("Ingrese un año: "))
        division=str(input("Ingrese una division: "))
        self.__M.Listar(anio,division)


    def opcion2(self):
        self.__M.Modificarinasistencias()


