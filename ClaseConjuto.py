
class Conjunto:
    __lista=[]


    def __init__(self):
        self.__lista=[]


    def __add__(self,C):
        if (type(self) == type(C)):
            union=Conjunto()

            for i in range(len(self.__lista)):
                bandera=union.Controlar(self.__lista[i])
                if not bandera:
                    union.__lista.append(self.__lista[i])

            for j in range(len(C.__lista)):
                bandera=union.Controlar(C.__lista[j])
                if not bandera:
                    union.__lista.append(C.__lista[j])

            return union.__lista


    def __sub__(self,C):
        if (type(self) == type(C)):
            diferencia=Conjunto()

            for i in range(len(self.__lista)): 
                if C.__lista.count(self.__lista[i])<=0:
                    diferencia.__lista.append(self.__lista[i])

        
            return diferencia.__lista


    def __eq__(self, C):
        bandera=False
        if (type(self) == type(C)):
            if len(self.__lista)==len(C.__lista):
                for i in range(len(self.__lista)):
                    if C.__lista.count(self.__lista[i])==1:
                        bandera=True


            
            return bandera
        

    def __str__(self):
        print(self.__lista)


    def CargarConjunto(self):
        E=int(input("\nIngrese elemento por elemento (Numero negativo para finalizar)"))
        while E>=0:
            bandera=self.Controlar(E)
            if  not bandera:
                self.__lista.append(E)
            else:
                print("\nElemento repetido en el conjunto")

            E=int(input("\nIngrese otro elemento (Ingrese un numero negativo para finalizar)"))



    def Controlar(self,elem):
        bandera=False
        if self.__lista.count(elem)>0:
            bandera=True
        
        return bandera



    def Cargarporparametros(self,listado):
        for i in range(len(listado)):
            bandera=self.Controlar(listado[i])
            if  not bandera:
                self.__lista.append(listado[i])
            else:
                print("\nElemento repetido en el conjunto")

    
        
