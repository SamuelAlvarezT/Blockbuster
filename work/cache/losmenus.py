from cache.ValidacionErrores import validar_opcion
def MenuPrincipal ():
    print("------SISTEMA GESTOR DE PELICULAS BLOCKBUSTER------")
    print("1.Administrador de Generos")
    print("2.Administrador de Actores" )
    print("3.Administrador de Foramtos")
    print("4.Gestor de Informes ")
    print("5.Gestor peliculas ")
    print("6.Salir")
    op=validar_opcion("Opcion: ",1,6)
    return op
    

def MenuGeneros():
    print("------GESTOR DE GENEROS------")
    print("1.Crear genero")
    print("2.Listar generos")
    print("3.Ir a menu principal")
    op=validar_opcion("Opcion: ",1,3)
    return op


def MenuActores():
    print ("------GESTOR DE ACTORES------")
    print("1.Crear Actor")
    print("2.Listar Actor")
    print("3.Ir menu principal")
    op=validar_opcion("Opcion: ",1,3)
    return op

def MenuFormatos():
    print("------GESTOR DE FORMATOS------")
    print("1.Crear formatos")
    print("2.listar formatos")
    print("3.Ir Menu Principal")
    op=validar_opcion("Opcion: ",1,3)
    return op

def MenuPelicualas():
    print("------GESTOR DE PELICULAS------")
    print("1.Agregar pelicula")
    print("2.Editar pelicula")
    print("3.eliminar pelicula")   
    print("4.Eliminar Actor")
    print("5.Buscar Pelicula")
    print("6.Listar toda las pelicualas")
    print("7.Menu Principal")
    op=validar_opcion("Opcion: ",1,7)
    return op


def GestorInformes():
    print("------GESTOR DE INFORMES------")
    print("1.Listar peliculas de un genero especifico")
    print("2.Listar las peliculas donde el protagonista sea Silvestre Stalone")
    print("3.Buscar pelicula y mostrar la sinopsis y los actores")
    print("4.Ir  menu principal")
    op=validar_opcion("Opcion: ",1,4)
    return op