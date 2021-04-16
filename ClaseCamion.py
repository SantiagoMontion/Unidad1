
class Camion:
    __id=0
    __nombreconductor=''
    __patente=''
    __marca=''
    __tara=0.0  #Peso del camion vacio


    def __init__(self,id,nc,pat,marca,tara):
        self.__id=id
        self.__nombreconductor=nc
        self.__patente=pat
        self.__marca=marca
        self.__tara=tara


    def gettara(self):
        return self.__tara

    def getpatente(self):
        return self.__patente

    def getnombre(self):
        return self.__nombreconductor