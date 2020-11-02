import random
import csv


def banco_preguntas():
    """
    Elije el documento de donde se obtendran las preguntas
    :return: string
    """
    return "preguntas.csv"


def validar_opcion(opcion):
    """
    Revisa si la opcion ingresada es valida
    :param string opcion: Es una letra que el usuario digita
    :return: Una letra que cumpla con las condiciones
    """
    while opcion != "A" and opcion != "B" and opcion != "C" and opcion != "D":
        opcion = input("Digite una opcion valida")
    return opcion


def cantidad_total_preguntas(documento):
    """
    Calcula la cantidad total de preguntas en el documento
    :param string documento: string que indica el nombre del documento del cual se va
    a calcular la cantidad total de preguntas
    :return: Numero entero
    """
    f = open(documento)
    leer = csv.reader(f)
    lista = []
    for datos in leer:
        lista.append(datos)
    lista = verificar(banco_preguntas())
    return (len(lista) + 1)//7


def lista_documento(documento):
    """
    Reduce la lista ingresada a un formato optimo
    :param string documento: Nombre del documento donde se almacenan las preguntas
    :return: Lista con el nuevo formato
    """
    with open(documento) as f:
        lista = []
        lista_final = []
        r = csv.reader(f)
        for datos in r:
            lista.append(datos)
        for x in range(len(lista)):
            lista_final.append(lista[x])
        return lista_final


def aux_anadir_preguntas(lista):
    """
    Cambia el formato de listas con listas a un string con saltos de linea
    :param list[[string] lista: Lista con datos
    :return: Un string con toda la informacion del documento
    """
    nuevos_datos = ""
    if type(lista[0]) == str:
        for x in lista:
            nuevos_datos = nuevos_datos + str(x) + "\n"
        return nuevos_datos.strip("\n")
    datos_anteriores = list(map(cambiar_a_str, lista))
    nuevos_datos = ""
    for x in datos_anteriores:
        nuevos_datos = nuevos_datos + str(x) + "\n"
    return nuevos_datos.strip("\n")


def cambiar_a_str(lista):
    """
    Auxiliar de aux_anadir_preguntas, Cambia los valores de la lista ingresada a string
    :param lista: Lista con listas de datos
    :return:
    """
    valor = ""
    for x in lista:
        valor = str(x)
    return valor


def leer_pregunta(documento, numero, contador):
    """
    Funcion que lee las preguntas
    :param strin documento: string con el nombre del documento
    :param int numero: Numero que indica el numero de la pregunta a leer
    :param int contador: Indica el numero de pregunta
    :return: None
    """
    num = numero
    lista_aux = verificar(documento)
    print(f"Pregunta #{contador+1}")
    for x in range((num*7)+1, (num*7)+6):
        print(lista_aux[x])


def leer_respuesta(numero):
    """
    Mira la respuesta a las preguntas
    :param int numero: Numero de la pregunta a la cual se le leera la respuesta
    :return: String, La respuesta correcta a la pregunta
    """
    num = numero
    lista_aux = verificar(banco_preguntas())
    for x in range(num * 7, (num * 7) + 7):
        if lista_aux[x] == "A" or lista_aux[x] == "B" or lista_aux[x] == "C" or lista_aux[x] == "D":
            if "A" in lista_aux[x]:
                return "A"
            elif "B" in lista_aux[x]:
                return "B"
            elif "C" in lista_aux[x]:
                return "C"
            elif "D" in lista_aux[x]:
                return "D"


def verificar(documento):
    """
    Funcion que verifica si el documento tiene el formato adecuado para la funcion leer_pregunta()
    :param String documento: Documento que se va a verificar
    :return:
    """
    f = open(documento)
    leer = csv.reader(f)
    lista = []
    for datos in leer:
        if datos != []:
            lista.append(datos)
    nueva_lista = ""
    for x in range(len(lista)):
        nueva_lista = nueva_lista + str(lista[x][0]) + "\n"
    return nueva_lista.split("\n")


def secuencia_preguntas(cantidad_total_preguntas):
    """
    inicia la lectura de preguntas una por una
    :param int cantidad_total_preguntas: Numero entero que indica la cantida total de preguntas almacenadas
    :return: None
    """
    cantidad_total = cantidad_total_preguntas
    print("Cuantas preguntas quiere responder?\n Presione",
          "\n 1. Para responder 10"" (Quiz completo)",
          "\n 2. " "Para responder 5 (mini-quiz) ",
          f"\n 3. Para responder Todas las preguntas (Hay {cantidad_total} Preguntas) ",
          f"\n 4. Para responder otra cantidad  (Hay {cantidad_total} preguntas )")
    respuesta_cantidad = int(input())
    respuesta_cantidad = cantidad_a_responder(respuesta_cantidad)
    orden_preguntas = aleatoriedad(respuesta_cantidad)
    contador_respuestas_correctas = 0
    for x in range(respuesta_cantidad):
        leer_pregunta(banco_preguntas(), orden_preguntas[x], x)
        respuesta_usuario = input("Elija una opcion  ")
        respuesta_usuario = validar_opcion(respuesta_usuario)
        if leer_respuesta(orden_preguntas[x]) == respuesta_usuario:
            print("CORRECTO", '\n')
            contador_respuestas_correctas = contador_respuestas_correctas + 1
        else:
            print("ERROR, La respuesta correcta era", leer_respuesta(orden_preguntas[x]), '\n')
    if contador_respuestas_correctas == respuesta_cantidad:
        print(f"Felicidades, Acerto todas las preguntas ({contador_respuestas_correctas} de {respuesta_cantidad}", '\n')
    else:
        print(f"Acerto {contador_respuestas_correctas} de {respuesta_cantidad} preguntas ", '\n')


def aleatoriedad(cantidad_usuario):
    """
    Crea un orden aleatorio de las preguntas almacenadas
    :return:cantidad de preguntas que se van a leer, Lista con el orden de las preguntas aleatorias
    """
    orden_aleatorio = []
    indicador = 1
    while indicador != 0:
        valor_aleatorio = random.randrange(0, (cantidad_total_preguntas(banco_preguntas())), 1)
        if valor_aleatorio not in orden_aleatorio:
            orden_aleatorio.append(valor_aleatorio)
        if len(orden_aleatorio) == cantidad_total_preguntas(banco_preguntas()):
            break
    orden_final = []
    for x in range(cantidad_usuario):
        orden_final.append(orden_aleatorio[x])
    return orden_final


def lista_preguntas_totales(cantidad_total_preguntas):
    """
    Para poner en una lista el numero de cada pregunta que haya en el documento
    :param  int cantidad_total_preguntas: Numero total de preguntas
    :return: Lista con el numero de todas las preguntas
    """
    lista_preguntas = []
    for x in range(cantidad_total_preguntas):
        lista_preguntas.append(x)
    return lista_preguntas


def cantidad_a_responder(cantidad):
    """
    Selecciona cuantas preguntas se van a contestar
    :param cantidad:
    :return: Cantidad de preguntas que se van a realizar
    """
    if cantidad == 1:
        return 10
    elif cantidad == 2:
        return 5
    elif cantidad == 3:
        return cantidad_total_preguntas(banco_preguntas())
    elif cantidad == 4:
        cantidad_nueva = int(input("Ingrese cuantas preguntas quiere responder "))
        return cantidad_nueva


def solicitar_datos_pregunta():
    """
    Solicita datos de la nueva pregunta y los almacena en una lista
    :return: Una lista con los datos de la nueva pregunta
    """
    pregunta = input("Ingrese la pregunta: ")
    posibles_respuesta_a = input("Ingrese la opcion A: ")
    posibles_respuesta_b = input("Ingrese la opcion B: ")
    posibles_respuesta_c = input("Ingrese la opcion C: ")
    posibles_respuesta_d = input("Ingrese la opcion D: ")
    respuesta_correcta = input("Ingrese la opcion que es correcta: A, B, C o D ")
    respuesta_correcta = validar_opcion(respuesta_correcta)
    print('\n')
    datos_pregunta_nueva = [[pregunta], ["   A "+posibles_respuesta_a],
                                        ["   B "+posibles_respuesta_b],
                                        ["   C "+posibles_respuesta_c],
                                        ["   D "+posibles_respuesta_d],
                            [respuesta_correcta]]
    return datos_pregunta_nueva


def hacer_preguntas(cantidad_total_preguntas):
    """
    Añade preguntas
    :param int cantidad_total_preguntas: Indica la cantidad total de preguntas almacenadas
    :return: None
    """
    print(f"Pregunta #{cantidad_total_preguntas+1}")
    datos_pregunta = [aux_anadir_preguntas(lista_documento(banco_preguntas()))],\
                     [str(cantidad_total_preguntas + 1)],\
                     [aux_anadir_preguntas(solicitar_datos_pregunta())]
    with open(banco_preguntas(), 'w', newline="") as f:
        escribir = csv.writer(f, delimiter=" ", lineterminator="\n")
        escribir.writerows(datos_pregunta)
    print("Creacion de pregunta completada, ", end="")
    verificar_creacion()


def verificar_creacion():
    """
    Pregunta al usuario si quiere continuar añadiento preguntas
    :return: None
    """
    validador = int(input("Desea continuar creando preguntas? \n1. Si \n2. No "))
    if validador == 1:
        hacer_preguntas(cantidad_total_preguntas(banco_preguntas()))
    if validador == 2:
        return


def reemplazar_preguntas(posicion):
    """
    Reemplaza una pregunta almacenada con una nueva pregunta
    :param int posicion:Indica el numero de la pregunta que va a ser reemplazada
    :return:None
    """
    parte_inicial = (aux_anadir_preguntas(reemplazar_parte_inicial(posicion)))
    parte_final = (aux_anadir_preguntas(reemplazar_parte_final(posicion)))
    print(f"Esta cambiando la pregunta #{posicion}")
    datos_pregunta = [parte_inicial],\
                     [str(posicion)],\
                     [aux_anadir_preguntas(solicitar_datos_pregunta())],\
                     [parte_final]

    with open(banco_preguntas(), 'w', newline="") as f:
        escribir = csv.writer(f, delimiter=" ", lineterminator="\n")
        escribir.writerows(datos_pregunta)
    print("Cambio de pregunta completado, ", end="")
    verificar_reemplazo()


def reemplazar_parte_inicial(posicion):
    """
    Auxiliar de la funcion Reemplazar_preguntas(), da los datos anteriores a la pregunta que se quiere cambiar
    :param int posicion:Posicion de la pregunta que va a ser reemplazada
    :return: Lista con los datos anteriores a la pregunta que se va a cambiar
    """
    num = posicion - 1
    lista_inicial = []
    lista = verificar(banco_preguntas())
    for x in range(0, (num * 7)):
        lista_inicial.append(lista[x])
    return lista_inicial


def reemplazar_parte_final(posicion):
    """
     Auxiliar de la funcion Reemplazar_preguntas(), da los datos posteriores a la pregunta que se quiere cambiar
    :param int posicion: Posicion de la pregunta que va a ser reemplazada
    :return: Lista con los datos de las preguntas posteriores a la que se va a cambiar
    """
    num = posicion - 1
    lista_final = []
    lista = verificar(banco_preguntas())
    for x in range(((num*7)+7), len(lista)):
        lista_final.append((lista[x]))
    return lista_final


def verificar_reemplazo():
    """
    Pregunta al usuario si quiere continuar reemplazando preguntas y si es asi le pregunta cual deseea cambiar
    :return:None
    """
    validador = input("Desea cambiar otra pregunta ?\n1. Si \n2. No")
    if validador == "1":
        nueva_posicion = int(input("Digite el numero de la pregunta que quiere cambiar: "))
        reemplazar_preguntas(nueva_posicion)
    elif validador == "2":
        return


def mostrar_todas_preguntas(documento):
    """
    Muestra todas las preguntas almacenadas hasta el momento
    :param string documento: Documento del cual se van a mostrar todas las preguntas
    :return: None
    """
    lista_aux = verificar(documento)
    for x in range(len(lista_aux)):
        print(lista_aux[x])


def eliminar_preguntas():
    """
    Elimina preguntas del documento
    :return:
    """
    print(f"Hay {cantidad_total_preguntas(banco_preguntas())} preguntas en total")
    eleccion = int(input("Presione 1  para eliminar la ultima pregunta realizada"
                         "\nPresione 2  para eliminar una pregunta especifica\n  "))
    while eleccion != 1 and eleccion != 2:
        eleccion = int(input("Opcion no valida, elija de nuevo (1 o 2) "))
    if eleccion == 1:
        eliminar_ultima_pregunta()
    elif eleccion == 2:
        print(f"Ingrese el numero de la pregunta (1 - {cantidad_total_preguntas(banco_preguntas())}) ")
        posicion = int(input())
        eliminar_pregunta_especifica(posicion)

    print(f"Eliminacion de pregunta completada, Ahora hay {cantidad_total_preguntas(banco_preguntas())}"
          f" Preguntas. ", end="")
    verificar_eliminacion()


def eliminar_ultima_pregunta():
    """
    Auxiliar de eliminar_preguntas(), elimina la ultima pregunta del documento
    :return:
    """
    parte_inicial = aux_anadir_preguntas(reemplazar_parte_inicial(cantidad_total_preguntas(banco_preguntas())))
    datos_documento = [parte_inicial], []
    with open(banco_preguntas(), 'w', newline="") as f:
        escribir = csv.writer(f, delimiter=" ", lineterminator="\n")
        escribir.writerows(datos_documento)


def eliminar_pregunta_especifica(posicion):
    """
    Elimina la pregunta elegida por el usuario
    :param int posicion: Numero de la pregunta que se va a eliminar
    :return:
    """
    nuevos_datos = [aux_eliminar_pregunta_especifica(posicion)], []
    with open(banco_preguntas(), "w", newline="") as f:
        escribir = csv.writer(f, delimiter=" ", lineterminator="\n")
        escribir.writerows(nuevos_datos)


def aux_eliminar_pregunta_especifica(posicion_pregunta):
    """
    Aux de la funcion eliminar_pregunta_especifica, A las siguientes preguntas les cambia el numero haciendo
    que el orden se mantenga
    :param int posicion_pregunta: Numero de la pregunta que el usuario va a eliminar
    :return:
    """
    posicion = posicion_pregunta - 1
    lista_preguntas_totales_string = \
        pasar_lista_a_string(lista_preguntas_totales(cantidad_total_preguntas(banco_preguntas())))
    lista_aux = verificar(banco_preguntas())
    lista_final = []
    for datos in range(posicion*7):
        lista_final.append(lista_aux[datos])
    for datos in range((posicion_pregunta*7), len(lista_aux)):
        if (lista_aux[datos]) in lista_preguntas_totales_string:
            lista_aux[datos] = int(lista_aux[datos]) - 1
        lista_final.append(lista_aux[datos])
    return aux_anadir_preguntas(lista_final)


def pasar_lista_a_string(lista_preguntas_totales):
    """
    Convierte a string los valores dentro de la lista de preguntas
    :param list[int] lista_preguntas_totales: Lista con el numero de totas las preguntas del documento
    :return:
    """
    lista_preguntas_totales_string = list(map(str, lista_preguntas_totales))
    lista_preguntas_totales_string.append(str(cantidad_total_preguntas(banco_preguntas())))
    return lista_preguntas_totales_string


def verificar_eliminacion():
    """
    Le pregunta al usuario si quiere continuar eliminado preguntas,
    de ser Verdadero, vuelve a la funcion eliminar_preguntas
    :return:
    """
    validar = int(input("Desea seguir eliminando preguntas?"
                        "\nPresione 1 para continuar\nPresione 2 para volver al menu\n\n "))
    while validar != 1 and validar != 2:
        validar = int(input("Opcion invalida, elija una opcion valida (1 o 2)"))
    if validar == 1:
        eliminar_preguntas()
    elif validar == 2:
        return


def menu():
    """
    Funcion que controla el menu de opciones
    :return: True / False
    """
    print("Elija una opcion: ", '\n', "1. Para contestar preguntas",
                                '\n', "2. Para formular preguntas",
                                '\n', "3. Para reemplazar preguntas",
                                '\n', "4. Para eliminar preguntas",
                                "\n", "5. Para Mostrar todas las preguntas almacenadas",
                                "\n", "6. Para Salir del programa")
    opcion = input()
    while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion != "6":
        opcion = input("Opcion no valida, elija de nuevo")
    if opcion == "1":
        secuencia_preguntas(cantidad_total_preguntas(banco_preguntas()))
    elif opcion == "2":
        hacer_preguntas(cantidad_total_preguntas(banco_preguntas()))
    elif opcion == "3":
        print(f"Cual pregunta quiere reemplazar?, "
              f"hay {cantidad_total_preguntas(banco_preguntas())} preguntas almacenadas")
        reemplazar = int(input())
        while reemplazar < 0 or reemplazar > cantidad_total_preguntas(banco_preguntas()):
            reemplazar = int(input(f"Ingrese un valor valido [1 - {cantidad_total_preguntas(banco_preguntas())}] "))
        reemplazar_preguntas(reemplazar)
    elif opcion == "4":
        eliminar_preguntas()
    elif opcion == "5":
        mostrar_todas_preguntas(banco_preguntas())
    elif opcion == "6":
        return
    menu()


def main():
    """
    Inicializa el menu
    :return:
    """
    print("Bienvenido al Quiz Maker")
    menu()
    print("Gracias por usar el programa :)")


main()
