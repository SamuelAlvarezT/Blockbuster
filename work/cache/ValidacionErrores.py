def validar_opcion(enunciando,minimo,maximo):
    while True:
        try:
            opcion =int(input(enunciando))
            if opcion>=minimo and opcion<=maximo:
                return opcion
            else:
                print(f"Opción no está entre el intervalo de ({minimo}-{maximo})")
        except ValueError:
            print("Por favor, introduce un número válido. ")
            



