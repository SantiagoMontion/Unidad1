from ClaseCosecha import Cosecha


class Menu:
    __switcher=None
    __C=None

    def __init__(self):
        self.__switcher = { 
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3
            }

        self.__C=Cosecha()
        self.__C.CargarCosechas()

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()


    def opcion1(self):
        num=int(input("Ingrese el id del camion: "))
        k=self.__C.Obtenerkilosdescargados(num-1)
        print("La cantidad de kilos descargados fue: ",k)

    def opcion2(self):
        dia=int(input("Ingrese el dia: "))
        self.__C.Mostrarlistado(dia-1)

    def opcion3(self):
        num=int(input("Ingrese el id del camion: "))
        dia=int(input("Ingrese el dia: "))
        peso=float(input("Ingrese el peso total: "))
        self.__C.RegistrarCosechas(num-1,dia-1,peso)
