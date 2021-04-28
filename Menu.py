
from ClaseConjuto import Conjunto

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

    def opcion(self, op,C1,C2):
        func=self.__switcher.get(op, lambda: print("\nOpción no válida"))
        func(C1,C2)

    def salir(self):
        print('Salir')

    def opcion1(self,C1,C2):
        union = C1 + C2
        print("\nla Union es: {}".format(union))




    def opcion2(self,C1,C2):
        Diferencia= C1 - C2
        print("\nLa diferencia es: {}".format(Diferencia))


    def opcion3(self,C1,C2):
        igualdad= C1 == C2
        if igualdad:
            print("\nLos Cojuntos son iguales")
        else:
            print("\nLos Conjuntos son diferentes")



    def Test(self):
        print("-----TEST-----")
        C1=Conjunto()
        C2=Conjunto()
        C1.Cargarporparametros([1,5,6,8])
        C2.Cargarporparametros([1,2,3,4,7])

        union = C1 + C2
        print("\nla Union es: {}".format(union))

        Diferencia= C1 - C2
        print("\nLa diferencia es: {}".format(Diferencia))

        igualdad= C1 == C2
        if igualdad:
            print("\nLos Cojuntos son iguales")
        else:
            print("\nLos Conjuntos son diferentes")


