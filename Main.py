from ClaseEmail import Email
from ManejadorEmail import ManejadorEmail

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
        test.CrearCuenta("wicc2019unsj-cuim.edu")
        test.CrearCuenta("juan1957@yahoo.com")
    

        print("---------Archivo---------")
        dom=input("Ingrese un dominio a buscar: ")
        M=ManejadorEmail()
        M.BuscarDominio(dom)
        
            
    
    
    
