from ClaseEmail import Email
import csv
if __name__ == "__main__":
    E=Email()
    nombre=input("Ingrese su nombre ")
    email=input("Ingrese su email ")

    bandera=E.CrearCuenta(email)
    if bandera==True:
        print("Estimado {} te enviaremos tus mensajes a la direccion {}".format(nombre,E.RetornaEmail()))
        print("----------Modificar Contraseña---------")
        contraactual=input("Ingrese su contraseña actual ")
        E.ChequearContra(contraactual)

        print("----------Test----------")
        test=Email()
        test.CrearCuenta("informatica.fcefn@gmail.com")
        test.CrearCuenta("wicc2019@unsj-cuim.edu")
        test.CrearCuenta("juan1957@yahoo.com")
    

        print("---------Archivo---------")
        dom=input("Ingrese un dominio a buscar: ")
        archivo=open("C:/Users/Montion/Desktop/Facultad/POO/Unidad 2/Repositorio/Ejercicio1/Listado.csv")
        reader=csv.reader(archivo,delimiter=',')
        cont=0
        for i in reader:
            for j in range(10):
                E.CrearCuenta(i[j])
                dom2=str(E.getdominio())
                if dom2 == dom:
                    cont+=1
        
        print("La cantidad de cuentas con el dominio {} es de: {}".format(dom,cont))
            
        archivo.close()
    else:
        print("Datos incorrectos")
    