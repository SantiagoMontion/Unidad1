

class Hora:
    __hora=0
    __min=0
    __seg=0



    def __init__(self,hora,min,seg):
        self.__hora=hora
        self.__min=min
        self.__seg=seg



    def Mostrar(self):
        print("\nHora: {}  Min: {}  Seg: {}".format(self.__hora,self.__min,self.__seg))


    def gethora(self):
        return self.__hora

    def getmin(self):
        return self.__min

    def getseg(self):
        return self.__seg

