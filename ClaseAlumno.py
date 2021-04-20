
class Alumno:
    cantmaxinasist=3
    canttotalclases=10

    def __init__(self,nom,anio,div,inasist):
        self.__nombre=nom
        self.__anio=anio
        self.__division=div
        self.__cantinasist=inasist


    def getnombre(self):
        return self.__nombre

    def getinasist(self):
        return self.__cantinasist

    @classmethod
    def getcantmaxinasist(cls):
        return cls.cantmaxinasist


    @classmethod
    def modificarcantmax(cls,nueva):
        cls.cantmaxinasist=nueva

