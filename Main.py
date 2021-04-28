from ManejadorIntegrantes import ManejadorIntegrantes
from ManejadorProyectos import ManejadorProyecto


def test():
    print("-------TEST-------")
    MItest=ManejadorIntegrantes()
    MPtest=ManejadorProyecto()
    MItest.CargarTest()
    MPtest.CargarTest()
    print("\n-------Reglas de negocio------")
    MPtest.CalcularPuntos(MItest)
    input("\nEnter para continuar")

    print("-------Listado de puntos--------")


    MPtest.MostrarPuntos()





if __name__ == '__main__':
    MI=ManejadorIntegrantes()
    MP=ManejadorProyecto()

    MI.CargarIntegrantes()
    MP.CargarProyectos()

    print("-------Reglas de negocio------")
    MP.CalcularPuntos(MI)

    input("\nEnter para continuar")

    print("-------Listado de puntos--------")

    MP.MostrarPuntos()


    test()
