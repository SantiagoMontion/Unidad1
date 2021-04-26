from ManejadorIntegrantes import ManejadorIntegrantes
from ManejadorProyectos import ManejadorProyecto


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