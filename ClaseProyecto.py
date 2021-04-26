
class Proyecto:
    __idproyecto=''
    __titulo=''
    __palabrasclave=''
    __puntos=0

    def __init__(self,id,tit,palabras):

        self.__idproyecto=id
        self.__titulo=tit
        self.__palabrasclave=palabras
        self.__puntos=0


    def getid(self):
        return self.__idproyecto

    def gettitulo(self):
        return self.__titulo

    def getpalabrasclave(self):
        return self.__palabrasclave

    def CargarPuntos(self,pts):
        self.__puntos+=pts

    def getpuntos(self):
        return self.__puntos


    def __gt__(self,P):
        return self.__puntos>P.__puntos