from ClaseHora import Hora
class FechaHora:
    __dia=0
    __mes=0
    __anio=0
    __hora=0
    __min=0
    __seg=0


    def __init__(self,dia=1,mes=1,anio=2020,hora=0,min=0,seg=0):
        try:
            self.__dia=int(dia)
            self.__mes=int(mes)
            self.__anio=int(anio)
            self.__hora=int(hora)
            self.__min=int(min)
            self.__seg=int(seg)
            self.check()
        except:
            print("Datos Incorrectos\n")


    def Mostrar(self):
        print("FECHA {}/{}/{}\nHoras {}hs Minturos {}m Segundos {}s".format(self.__dia,self.__mes,self.__anio,self.__hora,self.__min,self.__seg))



    def check(self):

        if self.__seg>=60:
            self.__min+=1
            self.__seg=0
        
        if self.__min>=60:
            self.__hora+=1
            self.__min=0

        if self.__hora>=24:
            self.__dia+=1
            self.__hora=0



#divisible por 4, y si es divisible por 100, debe ser divisible por 400
        if self.__anio%4==0 and self.__anio%100!=0:
            #Año bisiesto
            
            if self.__mes==2 and self.__dia>29:
                self.__dia=1
                self.__mes+=1
        elif self.__anio%100==0 and self.__anio%400 ==0:
            #Año bisiesto
            
            if self.__mes==2 and self.__dia>29:
                
                self.__dia=1
                self.__mes+=1

        else:
            if self.__mes>=12:
                self.__anio+=1
                self.__mes=1

            if self.__mes == 2 and self.__dia>28:
                self.__mes+=1
                self.__dia=1
                
            
            if (self.__mes == 4 or self.__mes==6 or self.__mes==9 or self.__mes==11) and (self.__dia>30):
                self.__dia=1
                self.__mes+=1
       
            
            elif (self.__mes==1 or self.__mes==3 or self.__mes==5 or self.__mes==7 or self.__mes==8 or self.__mes==10 or self.__mes==12) and (self.__dia>31):
                self.__dia=1
                self.__mes+=1
                if self.__mes>12:
                    self.__mes=1
                    self.__anio+=1


            


    def __add__(self,F):
        return FechaHora(int(self.__dia),int(self.__mes),int(self.__anio),int(self.__hora)+int(F.gethora()),int(self.__min)+int(F.getmin()),int(self.__seg)+int(F.getseg()))


    def __radd__(self,H):
        if type(self) ==FechaHora and type(H)==Hora:
            return FechaHora(int(self.__dia),int(self.__mes),int(self.__anio),int(H.gethora())+int(self.__hora),int(H.getmin())+int(self.__min),int(H.getseg())+int(self.__seg))

        elif type(H)==int:
            return FechaHora(H+int(self.__dia),int(self.__mes),int(self.__anio),int(self.__hora),int(self.__min),int(self.__seg))



    def __sub__(self,H):
        return FechaHora(int(self.__dia)-H,int(self.__mes),int(self.__anio),int(self.__hora),int(self.__min),int(self.__seg))


    def gethora(self):
        return self.__hora

    def getmin(self):
        return self.__min

    def getseg(self):
        return self.__seg