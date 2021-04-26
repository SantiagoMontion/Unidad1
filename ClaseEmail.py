import re
class Email:
    __IdCuenta=""
    __Dominio=""
    __TipoDominio=""
    __Contra=""

    def __init__(self,id="",dom="",tipodom="",contra="1234"):
        self.__IdCuenta=id
        self.__Dominio=dom
        self.__TipoDominio=tipodom
        self.__Contra=contra
        

    def RetornaEmail(self):
        cadena=str(self.__IdCuenta)+"@"+str(self.__Dominio)+"."+str(self.__TipoDominio)
        return cadena


    def getdominio(self):
        return self.__Dominio


    def CrearCuenta(self,correo):
        
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
            separado=correo.split("@")
            id=separado[0]
            sep2=separado[1].split(".")
            dominio=sep2[0]
            tipo=sep2[1]
            self.__init__(id,dominio,tipo)
            print("\n--Cuenta Registrada con Exito!--\n")
            return True
            


        else:
	        print ("Correo incorrecto")

                

    
    def ChequearContra(self,contra):
        if self.__Contra == contra:
            nueva=input("Ingrese su nueva contraseña ")
            self.CambioContra(nueva)
            
        else:
            return print("Las contraseñas no coinciden")
    

    def CambioContra(self,nueva):
        self.__Contra=nueva
        return print("Contraseña modificada con exito!")

