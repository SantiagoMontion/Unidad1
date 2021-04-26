
class Integrantes:
    __idproy=''
    __ApellidoNombre=''
    __dni=''
    __categoria=''
    __rol=''


    def __init__(self,id,nombre,dni,cat,rol):

        self.__idproy=id
        self.__ApellidoNombre=nombre
        self.__dni=dni
        self.__categoria=cat
        self.__rol=rol

    def getid(self):
        return self.__idproy

    def getnombre(self):
        return self.__ApellidoNombre

    def getdni(self):
        return self.__dni

    def getcategoria(self):
        return self.__categoria

    def getrol(self):
        return self.__rol


    

