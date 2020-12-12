import random
import csv
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from os import remove


def leer_contraseña(usuario, error):
    """
    Lee la contraseña del documento del usuario elegido
    :param String usuario: Nombre del usuario
    :param Label error: Widget que muestra un error
    :return:
    """
    try:
        contraseña = convertir(banco_preguntas(usuario))
        contraseña = contraseña[0]
        return contraseña
    except FileNotFoundError:
        error.place(relx=0.5, rely=0.56, anchor="c")


def inicia_aplicacion():
    """
    Inicia la ventana
    :return:
    """

    window = tk.Tk()
    window.title("Quiz Maker")
    window.geometry("1220x720")


    def verificar_inicio_sesion(clave, usuario, error):
        """
        Verifica si la clave ingresada por el usuario es la correcta
        :param String clave: Clave digitada por el usuario
        :param String usuario: Nombre de usuario
        :param Label error: widget vacio
        :return:
        """
        if leer_contraseña(usuario, error) == clave:
            limpiar_pantalla()
            global nombre_usuario
            nombre_usuario = usuario
            iniciar_menu(nombre_usuario)
        else:
            error.place(relx=0.5, rely=0.56, anchor="c")


    def log_in():
        """
        Inicialisa la pantalla de inicio de sesion, donde el usuario podra interactuar con las distintas opciones
        :return:
        """
        limpiar_pantalla()

        contorno = tk.Button(window, state="disable", width=48, height=22, bg="gray77")
        contorno.place(relx=0.5, rely=0.5, anchor="c")

        titulo = tk.Label(window, text="Introduzca el nombre de usuario y contraseña", bg="gray77")
        titulo.place(relx=0.5, rely=0.35, anchor="c")

        usuario = tk.Label(window, text="Nombre de usuario", bg="gray77")
        usuario.place(relx=0.5, rely=0.39, anchor="c")

        usuario_dato = tk.Entry(window, width=15, font=("Arial bold", 15))
        usuario_dato.place(relx=0.5, rely=0.43, anchor="c")

        clave = tk.Label(window, text="Contraseña ", bg="gray77")
        clave.place(relx=0.5, rely=0.49, anchor="c")

        clave_dato = tk.Entry(window, width=15, font=("Arial bold", 15), show="*")
        clave_dato.place(relx=0.5, rely=0.53, anchor="c")

        error = tk.Label(window, text="Contraseña o nombre de usuario equivocado", fg="red", bg="gray77")
        error.place(relx=0.5, rely=0.53, anchor="c")
        error.place_forget()

        volver = tk.Button(window, text="Volver", font=("Arial bold", 15), bg="red", command=lambda: menu_inicial())
        volver.place(relx=0.0, rely=0.0)

        ingresar_datos = tk.Button(window, text="Acceder", font=("Arial bold", 10), bg="gray64",
                                   command=lambda: verificar_inicio_sesion(clave_dato.get(),
                                                                            usuario_dato.get(),
                                                                            error))
        ingresar_datos.place(relx=0.5, rely=0.61, anchor="c")

        opcion_registrarse = tk.Button(window, text="Registrarse", font=("Arial bold", 10), bg="gray64",
                                   command=lambda: registrar())
        opcion_registrarse.place(relx=0.5, rely=0.68, anchor="c")


    def registrar():
        """
        Empieza la secuencia para crear un nuevo usuario
        :return:
        """
        limpiar_pantalla()

        volver = tk.Button(window, text="Volver", font=("Arial bold", 15), bg="red", command=lambda: menu_inicial())
        volver.place(relx=0.0, rely=0.0)

        contorno = tk.Button(window, state="disable", width=48, height=24, bg="gray77")
        contorno.place(relx=0.5, rely=0.5, anchor="c")

        titulo = tk.Label(window, text="Introduzca el nombre de usuario y contraseña", bg="gray77")
        titulo.place(relx=0.5, rely=0.32, anchor="c")

        usuario_nuevo = tk.Label(window, text="Nombre de usuario", bg="gray77")
        usuario_nuevo.place(relx=0.5, rely=0.36, anchor="c")

        usuario_nuevo_dato = tk.Entry(window, width=15, font=("Arial bold", 15))
        usuario_nuevo_dato.place(relx=0.5, rely=0.40, anchor="c")

        clave_nueva = tk.Label(window, text="Contraseña (minimo 6 caracteres, maximo 15)", bg="gray77")
        clave_nueva.place(relx=0.5, rely=0.46, anchor="c")

        clave_nueva_dato = tk.Entry(window, width=15, font=("Arial bold", 15), show="*")
        clave_nueva_dato.place(relx=0.5, rely=0.50, anchor="c")

        confirmar_clave_nueva = tk.Label(window, text="Confirmar contraseña", bg="gray77")
        confirmar_clave_nueva.place(relx=0.5, rely=0.54, anchor="c")

        confirmar_clave_nueva_dato = tk.Entry(window, width=15, font=("Arial bold", 15), show="*")
        confirmar_clave_nueva_dato.place(relx=0.5, rely=0.58, anchor="c")

        confirmar_clave_error = tk.Label(window, text="La contraseña no coincide", fg="red", bg="gray77")
        confirmar_clave_error.place(relx=0.5, rely=0.7, anchor="c")
        confirmar_clave_error.place_forget()

        confirmar_usuario_error = tk.Label(window, text="Nombre de usuario ya en uso", fg="red", bg="gray77")
        confirmar_usuario_error.place(relx=0.5, rely=0.43, anchor="c")
        confirmar_usuario_error.place_forget()

        crear_cuenta = tk.Button(window, text="Crear Cuenta Nueva", font=("Arial bold", 15), bg="gray64",
                                 command=lambda: crear_cuenta_nueva(usuario_nuevo_dato.get(),
                                                                      clave_nueva_dato.get(),
                                                                      confirmar_clave_nueva_dato.get(),
                                                                      confirmar_clave_error,
                                                                      confirmar_usuario_error,
                                                                      crear_cuenta))
        crear_cuenta.place(relx=0.5, rely=0.67, anchor="c")



    def crear_cuenta_nueva(usuario, clave1, clave2, clave_error, usuario_error, boton):
        """
        Crea una cuenta nueva con los datos suministrados
        :param String usuario: Nombre de usuario para la nueva cuenta
        :param String clave1: Clave del nuevo usuario
        :param String clave2: Clave verificadora
        :param Label clave_error: widget que indica si hay un error con la clave
        :param Label usuario_error: widget que indica si hay un error con el usuario
        :param Button boton: Boton utilizado para registrarse
        :return:
        """
        if comprobar_usuario(usuario):
            usuario_error.place(relx=0.5, rely=0.435, anchor="c")
        else :
            usuario_error.place_forget()
        if clave1 != clave2:
            clave_error.place(relx=0.5, rely=0.62, anchor="c")
            clave_error.configure(text="La contraseña no coincide")
        if clave1 == clave2:
            clave_error.place_forget()
        if len(clave1) < 6 or len(clave1) > 15:
            clave_error.place(relx=0.5, rely=0.62, anchor="c")
            clave_error.configure(text="Contraseña no valida")
        if clave1 == clave2 and (len(clave1) >= 6 and len(clave1) <= 15):
            clave_error.place_forget()
        if clave1 == clave2 and comprobar_usuario(usuario) == False and (len(clave1) >= 6 and len(clave1) <= 15):
            clave_error.place_forget()
            usuario_error.place_forget()
            crear_documento(usuario, clave1)
            boton.destroy()
            añadir_usuario(usuario)
            creacion = tk.Label(window, text="Cuenta creada con exito", font=("Arial bold", 20), bg="gray77")
            creacion.place(relx=0.5, rely=0.67, anchor="c")

            creacion = tk.Button(window, text="Iniciar Sesion",
                                 font=("Arial bold", 25), bg="green", command=lambda:log_in())
            creacion.place(relx=0.5, rely=0.85, anchor="c")


    def comprobar_usuario(nombre_de_usuario):

        """
        Comprueba si el nombre de usuario suministrado no esta en uso
        :param String nombre_de_usuario:
        :return:
        """
        usuarios = convertir(banco_preguntas("usuarios"))
        lista_aux = ()
        for x in usuarios:
            if x != '"' and x != " " and x != "" and x != "administrador":
                lista_aux = lista_aux + (x,)
        for x in range(len(lista_aux)):
            if lista_aux[x] == nombre_de_usuario:
                return True
        return False


    def añadir_usuario(usuario):
        """
        Añade el nombre de usuario al documento que contiene todos los nombres de usuarios
        :param String usuario: Nombre de usuario
        :return: """


        lista = convertir(banco_preguntas("usuarios"))
        nuevos_usuarios = ""
        for c in range(len(lista)):
            nuevos_usuarios = nuevos_usuarios + str(lista[c]) + "\n"
        nuevos_usuarios = nuevos_usuarios.strip("\n")
        datos = [nuevos_usuarios], [usuario]
        with open("../Recursor/usuarios.csv", "w", newline="") as f:
            escribir = csv.writer(f, delimiter=" ", lineterminator="\n")
            escribir.writerows(datos)


    def crear_documento(usuario, contraseña):
        """
        Crea el documento donde se almacenaran las preguntas del nuevo usuario
        :param String usuario: Nombre de usuario
        :param String contraseña: Contraseña del usuario
        :return:
        """
        nuevo_usuario = "../Recursor/" + usuario + ".csv"
        preguntas_iniciales = aux_anadir_preguntas(preguntas_nuevo_usuario())
        datos = [contraseña], [0, 0, 0], [preguntas_iniciales]
        with open(nuevo_usuario, "w", newline="") as f:
            escribir = csv.writer(f, delimiter=" ", lineterminator="\n")
            escribir.writerows(datos)


    def preguntas_nuevo_usuario():
        """
        Añade las preguntas iniciales en base al documento general
        :return:
        """
        lista_preguntas = lista_preguntas_totales(11)
        lista_preguntas_totales_string = list(map(str, lista_preguntas))
        lista_aux = convertir(banco_preguntas("administrador"))
        lista_inicial = []
        for x in range(2, len(lista_aux)):
            if lista_aux[x] in lista_preguntas_totales_string:
                if lista_aux[x] != str(11):
                    while lista_aux[x] != "A" and lista_aux[x] != "B" and lista_aux[x] != "C" and lista_aux[x] != "D":
                        lista_inicial.append(str(lista_aux[x]))
                        x = x + 1
                        if lista_aux[x] == "A" or lista_aux[x] == "B" or lista_aux[x] == "C" or lista_aux[x] == "D":
                            lista_inicial.append(lista_aux[x])
                else:
                    break
        return lista_inicial


    def menu_inicial():
        """
        Inicializa el menu donde el usuario se registra o inicia sesion
        :return:
        """
        limpiar_pantalla()

        iniciar_sesion = tk.Button(window, text="INICIAR SESION", font=("Arial bold", 10),
                                   width=30, height=4, bg="orange", command=lambda: log_in())
        iniciar_sesion.place(relx=0.5, rely=0.45, anchor="c")

        registrarse = tk.Button(window, text="REGISTRARSE", font=("Arial bold", 10), width=30,
                                height=4, bg="gray", command=lambda: registrar())
        registrarse.place(relx=0.5, rely=0.6, anchor="c")

        opcion_salir = tk.Button(window, text="Salir",
                                 font=("Arial bold", 25), command=lambda: cerrar_aplicacion(), bg="red")
        opcion_salir.place(relx=0.5, rely=0.875, width=300, height=50, anchor="c")


    def responder_preguntas():
        """
        Inicializa el menu donde el usuario elije cuantas preguntas desea responder
        :return:
        """
        limpiar_pantalla()

        regresar_menu = tk.Button(window, text="Volver al menu",
                                  font=("Arial bold", 25), command=lambda: volver_a_menu(), bg="red")
        regresar_menu.place(relx=0.5, rely=0.75, anchor="c")

        cantidad_total = cantidad_total_preguntas(banco_preguntas(nombre_usuario))

        menu_opciones = tk.Label(window, text=f"¿Qué quiz desea realizar? hay {cantidad_total} preguntas ",
                                 font=("Arial bold", 25), bg="gray88").place(relx=0.5, rely=0.1, anchor="c")

        opcion_1 = tk.Button(window, text="10 (Quiz)", font=("Arial bold", 25),
                             command=lambda:opcional(10), bg="gray64")
        opcion_1.place(relx=0.4, y=240, width=245, height=100, anchor="c")

        opcion_2 = tk.Button(window, text="5  (Mini Quiz)",
                                 font=("Arial bold", 25), command=lambda: opcional(5), bg="gray64")
        opcion_2.place(relx=0.6, y=240, width=245, height=100, anchor="c")


    def volver_a_menu():
        """
        Vuelve al menu principal
        :return:
        """
        limpiar_pantalla()
        iniciar_menu(nombre_usuario)


    def opcional(cantidad_preguntas_usuario):
        """
        Inicia la secuencia de preguntas en base a la cantidad elegida por el usuario
        :param Int cantidad_preguntas_usuario: Cantidad de preguntas que el usuario elije
        :return:
        """
        limpiar_pantalla()
        orden_preguntas = aleatoriedad(cantidad_preguntas_usuario)
        interfaz_respuestas(cantidad_preguntas_usuario, orden_preguntas)
        secuencia_mostrar_preguntas(cantidad_preguntas_usuario, orden_preguntas)


    def secuencia_mostrar_preguntas(cantidad_preguntas, orden, pregunta=0, validador=0):
        """
        Muestra las preguntas en un orden aleatorio, permite avanzar y retroceder el numero de la pregunta
        :param Int cantidad_preguntas: Cantidad de preguntas que el usuario eligio
        :param List orden: Lista con el orden de las preguntas que se van a mostrar
        :param Int pregunta: Número de la pregunta que se esta mostrando
        :param Int validador: Numero que verifica si ya se respondieron las preguntas
        :return:
        """
        label = tk.Label(window)
        boton = tk.Button(window)

        lista_eliminar = window.place_slaves()
        for x in lista_eliminar:
            if type(x) == type(boton):
                x.destroy()

        if cantidad_preguntas == 5 and validador == 0:

            opcion_a = tk.Label(window, text="A", bg="gray86").place(relx=0.385, rely=0.6)
            opcion_b = tk.Label(window, text="B", bg="gray86").place(relx=0.385, rely=0.65)
            opcion_c = tk.Label(window, text="C", bg="gray86").place(relx=0.385, rely=0.7)
            opcion_d = tk.Label(window, text="D", bg="gray86").place(relx=0.385, rely=0.75)

            for x in range(cantidad_preguntas):
                numero_pregunta = tk.Label(window, text=f"{x + 1}", bg="gray86")
                numero_pregunta.place(relx=0.403 + x * 0.05, rely=0.58)


        if cantidad_preguntas == 10 and validador == 0:

            opcion_a = tk.Label(window, text="A", bg="gray86").place(relx=0.260, rely=0.6)
            opcion_b = tk.Label(window, text="B", bg="gray86").place(relx=0.260, rely=0.65)
            opcion_c = tk.Label(window, text="C", bg="gray86").place(relx=0.260, rely=0.7)
            opcion_d = tk.Label(window, text="D", bg="gray86").place(relx=0.260, rely=0.75)

            for x in range(cantidad_preguntas):
                numero_pregunta = tk.Label(window, text=f"{x + 1}", bg="gray86")
                numero_pregunta.place(relx=0.279 + x * 0.05, rely=0.58)


        if validador ==1:

            preguntar_otra_vez = tk.Button(window, text="Hacer otro quiz", bg="green",
                                           font=("Arial bold", 15), command=lambda: opcional(cantidad_preguntas))
            preguntar_otra_vez.place(relx=0.5, rely=0.9, anchor="c")

        preguntas = tk.Button(window,
                             text=leer_pregunta(banco_preguntas(nombre_usuario), orden[pregunta], pregunta+1)[0],
                             font=("Arial bold", 15), bg="gray76")
        preguntas.place(relx=0.5, rely=0.3, anchor="c")

        siguiente_pre = tk.Button(window)
        siguiente_pre.place(relx=0.95, rely=0.9, anchor="c")
        siguiente_pre.place_forget()

        numero_pregunta = tk.Label(window, text=f"Pregunta {pregunta + 1} / {cantidad_preguntas}",
                                  font=("Arial bold", 14))
        numero_pregunta.place(relx=0.5, rely=0.05, anchor="c")

        volver = tk.Button(window, text="Volver", font=("Arial bold", 15),
                           bg="red", command=lambda: responder_preguntas())
        volver.place(relx=0.0, rely=0.0)

        if pregunta != cantidad_preguntas-1:
            siguiente_pre.place(relx=0.92, rely=0.9, anchor="c")
            siguiente_pre.configure(font=("Arial bold", 15), text="Siguiente Pregunta",
                                      command=lambda: siguiente_pregunta(pregunta, orden, preguntas,
                                                                         validador, cantidad_preguntas),
                                      bg="green")


    def siguiente_pregunta(pregunta, orden, posicion, validador, cantidad_preguntas):
        """
        Muestra la siguiente pregunta en la secuencia
        :param Int pregunta: Numero de la pregunta que se esta respondiendo
        :param List orden: Lista con el orden de las preguntas
        :param Int posicion: Numero de la posicion de la pregunta
        :param Int validador: Numero que verifica si ya se respondieron las preguntas
        :param Int cantidad_preguntas: Cantidad de preguntas que el usuario eligio
        :return:
        """
        secuencia_mostrar_preguntas(cantidad_preguntas, orden, pregunta+1, validador)
        pregunta_ant = tk.Button(window, text="Pregunta Anterior", font=("Arial bold", 15),
                             command=lambda: pregunta_anterior(pregunta, orden, posicion,
                                                               validador, cantidad_preguntas),
                                 bg="green")
        pregunta_ant.place(relx=0.07, rely=0.9, anchor="c")


    def pregunta_anterior(pregunta, orden, posicion, validador, cantidad_preguntas):
        """
        Muestra la pregunta anterior en la secuencia de preguntas
        :param Int pregunta: Numero de la pregunta que se esta respondiendo
        :param List orden: Lista con el orden de las preguntas
        :param Int posicion: Numero de la posicion de la pregunta
        :param Int validador: Numero que verifica si ya se respondieron las preguntas
        :param Int cantidad_preguntas: Cantidad de preguntas que el usuario eligio
        :return:
        """
        posicion.destroy()
        secuencia_mostrar_preguntas(cantidad_preguntas, orden, pregunta, validador)


        if pregunta != 0:
            pregunta_ant = tk.Button(window, text="Pregunta Anterior", font=("Arial bold", 15),
                                     command=lambda: pregunta_anterior(pregunta-1, orden, posicion,
                                                                       validador, cantidad_preguntas),
                                     bg="green")
            pregunta_ant.place(relx=0.07, rely=0.9, anchor="c")


    def interfaz_respuestas(cantidad_preguntas, orden):
        """
        Inicializa la interfaz para responder las preguntas
        :param Int cantidad_preguntas: Cantidad total de preguntas que se estan respondiendo
        :param List orden: Lista con el orden de las preguntas
        :return:
        """

        for x in range(10):
            espacios = tk.Label(window, font=("Arial bold", 35), width=2)
            espacios.grid(column=1 + x * 1, row=0 + x * 1)

        recuadro_cuadernillo = tk.Button(window, bg="gray86", width=200, height=10, state="disable")
        recuadro_cuadernillo.grid(column=0, row=7)

        error = tk.Label(window, text="")
        error.place(relx=0.5, rely=0.5)
        error.place_forget()
        if cantidad_preguntas == 5:
            opcion1 = tk.StringVar()
            circulorespuesta1 = tk.Radiobutton(window, variable=opcion1, value="A", bg="gray86").place(relx=0.4,
                                                                                                       rely=0.6)
            circulorespuesta1 = tk.Radiobutton(window, variable=opcion1, value="B", bg="gray86").place(relx=0.4,
                                                                                                       rely=0.65)
            circulorespuesta1 = tk.Radiobutton(window, variable=opcion1, value="C", bg="gray86").place(relx=0.4,
                                                                                                       rely=0.7)
            circulorespuesta1 = tk.Radiobutton(window, variable=opcion1, value="D", bg="gray86").place(relx=0.4,
                                                                                                       rely=0.75)

            opcion2 = tk.StringVar()
            circulorespuesta2 = tk.Radiobutton(window, variable=opcion2, value="A", bg="gray86").place(relx=0.45,
                                                                                                       rely=0.6)
            circulorespuesta2 = tk.Radiobutton(window, variable=opcion2, value="B", bg="gray86").place(relx=0.45,
                                                                                                       rely=0.65)
            circulorespuesta2 = tk.Radiobutton(window, variable=opcion2, value="C", bg="gray86").place(relx=0.45,
                                                                                                       rely=0.7)
            circulorespuesta2 = tk.Radiobutton(window, variable=opcion2, value="D", bg="gray86").place(relx=0.45,
                                                                                                       rely=0.75)

            opcion3 = tk.StringVar()
            circulorespuesta3 = tk.Radiobutton(window, variable=opcion3, value="A", bg="gray86").place(relx=0.5,
                                                                                                       rely=0.6)
            circulorespuesta3 = tk.Radiobutton(window, variable=opcion3, value="B", bg="gray86").place(relx=0.5,
                                                                                                       rely=0.65)
            circulorespuesta3 = tk.Radiobutton(window, variable=opcion3, value="C", bg="gray86").place(relx=0.5,
                                                                                                       rely=0.7)
            circulorespuesta3 = tk.Radiobutton(window, variable=opcion3, value="D", bg="gray86").place(relx=0.5,
                                                                                                       rely=0.75)

            opcion4 = tk.StringVar()
            circulorespuesta4 = tk.Radiobutton(window, variable=opcion4, value="A", bg="gray86").place(relx=0.55,
                                                                                                       rely=0.6)
            circulorespuesta4 = tk.Radiobutton(window, variable=opcion4, value="B", bg="gray86").place(relx=0.55,
                                                                                                       rely=0.65)
            circulorespuesta4 = tk.Radiobutton(window, variable=opcion4, value="C", bg="gray86").place(relx=0.55,
                                                                                                       rely=0.7)
            circulorespuesta4 = tk.Radiobutton(window, variable=opcion4, value="D", bg="gray86").place(relx=0.55,
                                                                                                       rely=0.75)

            opcion5 = tk.StringVar()
            circulorespuesta5 = tk.Radiobutton(window, variable=opcion5, value="A", bg="gray86").place(relx=0.6,
                                                                                                       rely=0.6)
            circulorespuesta5 = tk.Radiobutton(window, variable=opcion5, value="B", bg="gray86").place(relx=0.6,
                                                                                                       rely=0.65)
            circulorespuesta5 = tk.Radiobutton(window, variable=opcion5, value="C", bg="gray86").place(relx=0.6,
                                                                                                       rely=0.7)
            circulorespuesta5 = tk.Radiobutton(window, variable=opcion5, value="D", bg="gray86").place(relx=0.6,
                                                                                                       rely=0.75)

            finalizar_boton = tk.Button(window, text="Finalizar", bg="green", font=("Arial bold", 15),
                                        command=lambda: finalizar(finalizar_boton, error, cantidad_preguntas, orden,
                                                                  opcion1.get(),
                                                                  opcion2.get(),
                                                                  opcion3.get(),
                                                                  opcion4.get(),
                                                                  opcion5.get(), ))
            finalizar_boton.grid(column=0, row=8)

        if cantidad_preguntas == 10:
            opcion1 = tk.StringVar()
            circulorespuesta1 = tk.Radiobutton(window, variable=opcion1, value="A", bg="gray86").place(relx=0.275,
                                                                                                       rely=0.6)
            circulorespuesta1 = tk.Radiobutton(window, variable=opcion1, value="B", bg="gray86").place(relx=0.275,
                                                                                                       rely=0.65)
            circulorespuesta1 = tk.Radiobutton(window, variable=opcion1, value="C", bg="gray86").place(relx=0.275,
                                                                                                       rely=0.7)
            circulorespuesta1 = tk.Radiobutton(window, variable=opcion1, value="D", bg="gray86").place(relx=0.275,
                                                                                                       rely=0.75)

            opcion2 = tk.StringVar()
            circulorespuesta2 = tk.Radiobutton(window, variable=opcion2, value="A", bg="gray86").place(relx=0.325,
                                                                                                       rely=0.6)
            circulorespuesta2 = tk.Radiobutton(window, variable=opcion2, value="B", bg="gray86").place(relx=0.325,
                                                                                                       rely=0.65)
            circulorespuesta2 = tk.Radiobutton(window, variable=opcion2, value="C", bg="gray86").place(relx=0.325,
                                                                                                       rely=0.7)
            circulorespuesta2 = tk.Radiobutton(window, variable=opcion2, value="D", bg="gray86").place(relx=0.325,
                                                                                                       rely=0.75)

            opcion3 = tk.StringVar()
            circulorespuesta3 = tk.Radiobutton(window, variable=opcion3, value="A", bg="gray86").place(relx=0.375,
                                                                                                       rely=0.6)
            circulorespuesta3 = tk.Radiobutton(window, variable=opcion3, value="B", bg="gray86").place(relx=0.375,
                                                                                                       rely=0.65)
            circulorespuesta3 = tk.Radiobutton(window, variable=opcion3, value="C", bg="gray86").place(relx=0.375,
                                                                                                       rely=0.7)
            circulorespuesta3 = tk.Radiobutton(window, variable=opcion3, value="D", bg="gray86").place(relx=0.375,
                                                                                                       rely=0.75)

            opcion4 = tk.StringVar()
            circulorespuesta4 = tk.Radiobutton(window, variable=opcion4, value="A", bg="gray86").place(relx=0.425,
                                                                                                       rely=0.6)
            circulorespuesta4 = tk.Radiobutton(window, variable=opcion4, value="B", bg="gray86").place(relx=0.425,
                                                                                                       rely=0.65)
            circulorespuesta4 = tk.Radiobutton(window, variable=opcion4, value="C", bg="gray86").place(relx=0.425,
                                                                                                       rely=0.7)
            circulorespuesta4 = tk.Radiobutton(window, variable=opcion4, value="D", bg="gray86").place(relx=0.425,
                                                                                                       rely=0.75)

            opcion5 = tk.StringVar()
            circulorespuesta5 = tk.Radiobutton(window, variable=opcion5, value="A", bg="gray86").place(relx=0.475,
                                                                                                       rely=0.6)
            circulorespuesta5 = tk.Radiobutton(window, variable=opcion5, value="B", bg="gray86").place(relx=0.475,
                                                                                                       rely=0.65)
            circulorespuesta5 = tk.Radiobutton(window, variable=opcion5, value="C", bg="gray86").place(relx=0.475,
                                                                                                       rely=0.7)
            circulorespuesta5 = tk.Radiobutton(window, variable=opcion5, value="D", bg="gray86").place(relx=0.475,
                                                                                                       rely=0.75)
            opcion6 = tk.StringVar()
            circulorespuesta6 = tk.Radiobutton(window, variable=opcion6, value="A", bg="gray86").place(relx=0.525,
                                                                                                       rely=0.6)
            circulorespuesta6 = tk.Radiobutton(window, variable=opcion6, value="B", bg="gray86").place(relx=0.525,
                                                                                                       rely=0.65)
            circulorespuesta6 = tk.Radiobutton(window, variable=opcion6, value="C", bg="gray86").place(relx=0.525,
                                                                                                       rely=0.7)
            circulorespuesta6 = tk.Radiobutton(window, variable=opcion6, value="D", bg="gray86").place(relx=0.525,
                                                                                                       rely=0.75)

            opcion7 = tk.StringVar()
            circulorespuesta7 = tk.Radiobutton(window, variable=opcion7, value="A", bg="gray86").place(relx=0.575,
                                                                                                       rely=0.6)
            circulorespuesta7 = tk.Radiobutton(window, variable=opcion7, value="B", bg="gray86").place(relx=0.575,
                                                                                                       rely=0.65)
            circulorespuesta7 = tk.Radiobutton(window, variable=opcion7, value="C", bg="gray86").place(relx=0.575,
                                                                                                       rely=0.7)
            circulorespuesta7 = tk.Radiobutton(window, variable=opcion7, value="D", bg="gray86").place(relx=0.575,
                                                                                                       rely=0.75)

            opcion8 = tk.StringVar()
            circulorespuesta8 = tk.Radiobutton(window, variable=opcion8, value="A", bg="gray86").place(relx=0.625,
                                                                                                       rely=0.6)
            circulorespuesta8 = tk.Radiobutton(window, variable=opcion8, value="B", bg="gray86").place(relx=0.625,
                                                                                                       rely=0.65)
            circulorespuesta8 = tk.Radiobutton(window, variable=opcion8, value="C", bg="gray86").place(relx=0.625,
                                                                                                       rely=0.7)
            circulorespuesta8 = tk.Radiobutton(window, variable=opcion8, value="D", bg="gray86").place(relx=0.625,
                                                                                                       rely=0.75)

            opcion9 = tk.StringVar()
            circulorespuesta9 = tk.Radiobutton(window, variable=opcion9, value="A", bg="gray86").place(relx=0.675,
                                                                                                       rely=0.6)
            circulorespuesta9 = tk.Radiobutton(window, variable=opcion9, value="B", bg="gray86").place(relx=0.675,
                                                                                                       rely=0.65)
            circulorespuesta9 = tk.Radiobutton(window, variable=opcion9, value="C", bg="gray86").place(relx=0.675,
                                                                                                       rely=0.7)
            circulorespuesta9 = tk.Radiobutton(window, variable=opcion9, value="D", bg="gray86").place(relx=0.675,
                                                                                                       rely=0.75)

            opcion10 = tk.StringVar()
            circulorespuesta10 = tk.Radiobutton(window, variable=opcion10, value="A", bg="gray86").place(relx=0.725,
                                                                                                        rely=0.6)
            circulorespuesta10 = tk.Radiobutton(window, variable=opcion10, value="B", bg="gray86").place(relx=0.725,
                                                                                                        rely=0.65)
            circulorespuesta10 = tk.Radiobutton(window, variable=opcion10, value="C", bg="gray86").place(relx=0.725,
                                                                                                        rely=0.7)
            circulorespuesta10 = tk.Radiobutton(window, variable=opcion10, value="D", bg="gray86").place(relx=0.725,
                                                                                                        rely=0.75)
            finalizar_boton = tk.Button(window, text="Finalizar", bg="green", font=("Arial bold", 15),
                                        command=lambda: finalizar(finalizar_boton, error, cantidad_preguntas, orden,
                                                                  opcion1.get(),
                                                                  opcion2.get(),
                                                                  opcion3.get(),
                                                                  opcion4.get(),
                                                                  opcion5.get(),
                                                                  opcion6.get(),
                                                                  opcion7.get(),
                                                                  opcion8.get(),
                                                                  opcion9.get(),
                                                                  opcion10.get()))
            finalizar_boton.grid(column=0, row=8)


    def finalizar(boton, error, cantidad_preguntas, orden, *respuestas):
        """
        Entrega las respuestas que el usuario entrego para su verificacion
        :param Button boton: Boton con el cual el usuario finaliza
        :param Label error: Widget Que aparece si el usuario no ha respondido totas las preguntas
        :param Int cantidad_preguntas: Cantidad total de preguntas
        :param List orden: Lista con el orden de las preguntas
        :param Tuple respuestas: Respuestas ingresadas por el usuario
        :return:
        """
        if "" in respuestas:
            error.configure(text="Todavia hay preguntas sin responder", fg="red", bg="gray90", font=("Arial bold", 12))
            error.place(relx=0.4, rely=0.86)
        else:
            respuestas_s = " ".join(respuestas)
            boton.destroy()
            boton_aux = tk.Button(window)
            label_aux = tk.Label(window)
            eliminar_cuadernillo = window.place_slaves()
            for x in eliminar_cuadernillo:
                if type(x) != type(boton_aux):
                    x.destroy()
            calificar(cantidad_preguntas, orden, respuestas)


    def calificar(cantidad_preguntas, orden_preguntas, respuestas):
        """
        Califica el quiz resuelto por el usuario
        :param Int cantidad_preguntas: Cantidad total de preguntas
        :param List orden_preguntas: Lista con el orden de las preguntas
        :param Tuple respuestas: Respuestas ingresadas por el usuario
        :return:
        """
        secuencia_mostrar_preguntas(cantidad_preguntas, orden_preguntas, 0, 1)
        contador_aciertos = 0
        for x in range(cantidad_preguntas):
            if respuestas[x] == leer_pregunta(banco_preguntas(nombre_usuario), orden_preguntas[x], x)[1]:
                contador_aciertos = contador_aciertos + 1

        if contador_aciertos == 1:

            mostrar_resultado = tk.Label(window, text="Acerto 1 pregunta ", font=("Arial bold", 15), bg="gray89")
            mostrar_resultado.place(relx=0.5, rely=0.55, anchor="c")


        elif contador_aciertos == cantidad_preguntas:

            mostrar_resultado = tk.Label(window, text="Felicidades, Acerto todas las preguntas" +
                                                      "\n" + "(" + str(contador_aciertos) + " de 5)",
                                         font=("Arial bold", 15), bg="gray89")
            mostrar_resultado.place(relx=0.5, rely=0.53, anchor="c")

        elif contador_aciertos == 0:

            mostrar_resultado = tk.Label(window, text="No acerto ninguna pregunta ",
                                         font=("Arial bold", 15), bg="gray89")
            mostrar_resultado.place(relx=0.5, rely=0.55, anchor="c")

        else:
            mostrar_resultado = tk.Label(text="Acerto " + str(contador_aciertos) + " Preguntas ",
                                         font=("Arial bold", 15), bg="gray89")
            mostrar_resultado.place(relx=0.5, rely=0.55, anchor="c")

        if cantidad_preguntas == 5:
            for x in range(cantidad_preguntas):
                respuestas_finales = tk.Label(
                    window,
                    text=f"La respuesta de la pregunta # {x + 1} es"
                         f" {leer_pregunta(banco_preguntas(nombre_usuario), orden_preguntas[x], x)[1]}"
                         f" | Su respuesta fue: {respuestas[x]}",
                    font=("Arial bold", 10), bg="gray86")

                respuestas_finales.place(relx=0.5, y=435 + (28 * x), anchor="c")

                simbolito = tk.Label(window, text=revisar_respuesta(x, respuestas, orden_preguntas)[0] + " ",
                                     font=("Arial bold", 10), bg="gray86",
                                     fg=revisar_respuesta(x, respuestas, orden_preguntas)[1])
                simbolito.place(relx=0.35, y=435 + (28 * x), anchor="c")
                
            calificacion = tk.Label(window, text=f"Su calificacion es {contador_aciertos * 10}/50",
                                    font=("Arial bold", 20), bg="gray89")
            calificacion.place(relx=0.5, rely=0.85, anchor="c")

        elif cantidad_preguntas == 10:
            z = 0
            for x in range(cantidad_preguntas):
                if x < 5:

                    respuestas_finales = tk.Label(
                        window,
                        text=f"La respuesta de la pregunta # {x + 1} es"
                             f" {leer_pregunta(banco_preguntas(nombre_usuario), orden_preguntas[x], x)[1]}"
                             f" | Su respuesta fue: {respuestas[x]}",
                        font=("Arial bold", 10), bg="gray86")

                    respuestas_finales.place(relx=0.3, y=435 + (28 * x), anchor="c")

                    simbolito = tk.Label(window, text=revisar_respuesta(x, respuestas, orden_preguntas)[0] + " ",
                                         font=("Arial bold", 10), bg="gray86",
                                         fg=revisar_respuesta(x, respuestas, orden_preguntas)[1])
                    simbolito.place(relx=0.15, y=435 + (28 * x), anchor="c")


                else:

                    respuestas_finales = tk.Label(
                        window,
                        text=f"La respuesta de la pregunta # {x + 1} es"
                             f" {leer_pregunta(banco_preguntas(nombre_usuario), orden_preguntas[x], x)[1]}"
                             f" | Su respuesta fue: {respuestas[x]}",
                        font=("Arial bold", 10), bg="gray86")

                    respuestas_finales.place(relx=0.65, y=435 + (28 * z), anchor="c")

                    simbolito = tk.Label(window, text=revisar_respuesta(x, respuestas, orden_preguntas)[0] + " ",
                                         font=("Arial bold", 10), bg="gray86",
                                         fg=revisar_respuesta(x, respuestas, orden_preguntas)[1])
                    simbolito.place(relx=0.50, y=435 + (28 * z), anchor="c")

                    z = z + 1

            calificacion = tk.Label(window, text=f"Su calificacion es {contador_aciertos * 10}/100",
                                            font=("Arial bold", 20), bg="gray89")
            calificacion.place(relx=0.5, rely=0.85, anchor="c")





        preguntar_otra_vez = tk.Button(window, text="Hacer otro quiz", bg="green",
                                       font=("Arial bold", 15), command=lambda: opcional(cantidad_preguntas))
        preguntar_otra_vez.place(relx=0.5, rely=0.9, anchor="c")

        errores = cantidad_preguntas - contador_aciertos
        guardar_estadisticas(cantidad_preguntas, contador_aciertos, errores)


    def revisar_respuesta(numero, valores_ingresados, orden):
        """
        Verifica si la respuesta es correcta
        :param Int numero: Numero de la pregunta
        :param List valores_ingresados: Lista con las respuestas deñ usuario
        :param List orden: Lista con el orden de las preguntas
        :return: Simbolo y un color dependiendo del resultado
        """
        if leer_pregunta(banco_preguntas(nombre_usuario), orden[numero], numero)[1] == valores_ingresados[numero]:
            return "✓", "green"
        else:
            return "X", "red"


    def guardar_estadisticas(preguntas, aciertos, errores):
        """
        Guarda las estadisticas del quiz que obtuvo el usuario
        :param Int preguntas: Cantidad de preguntas respondidas
        :param Int ciertos: Cantidad de aciertos
        :param Int errores: Cantidad de Fallos
        :return:
        """
        parte_inicial, parte_final = aux_estadisticas()
        lista = convertir(banco_preguntas(nombre_usuario))
        lista = lista[1].split(" ")
        lista_aux = lista
        lista_aux[0] = preguntas + int(lista[0])
        lista_aux[1] = aciertos + int(lista[1])
        lista_aux[2] = errores + int(lista[2])
        datos = ""
        for x in range(len(lista)):
            datos = datos + str(lista_aux[x]) + " "
        datos_nuevos = [parte_inicial], [datos], [parte_final]
        with open(banco_preguntas(nombre_usuario), 'w', newline="") as f:
            escribir = csv.writer(f, delimiter=" ", lineterminator="\n")
            escribir.writerows(datos_nuevos)


    def limpiar_pantalla():
        """
        Elimina todos los Widgets en la pantalla
        :return:
        """
        lista_eliminar = window.place_slaves()
        for x in lista_eliminar:
            x.destroy()
        lista_eliminar2 = window.grid_slaves()
        for x in lista_eliminar2:
            x.destroy()
        lista_eliminar3 = window.pack_slaves()
        for x in lista_eliminar3:
            x.destroy()


    def reemplazar_preguntas():
        """
        Inicia la secuencia para reemplazar preguntas
        :return:
        """
        limpiar_pantalla()
        if (cantidad_total_preguntas(banco_preguntas(nombre_usuario))) == 0:
            aviso = tk.Button(window, text="NO HAY NINGUNA PREGUNTA PARA REEMPLAZAR, PRUEBA\n"
                                           "CREAR UNA NUEVA EN LA OPCION FORMULAR",
                                font=("Arial bold", 25), state="disable", bg="Dark Orange1")
            aviso.place(relx=0.5, rely=0.5, anchor="c")
        else:
            cantidad_preguntas = cantidad_total_preguntas(banco_preguntas(nombre_usuario))
            lista_preguntas = lista_preguntas_totales(cantidad_total_preguntas(banco_preguntas(nombre_usuario)))
            lista_nueva = ""
            for x in range(len(lista_preguntas)):
                lista_nueva = lista_nueva + str(lista_preguntas[x] + 1) + " "

            preguntar_numero_label = \
                tk.Label(window,
                         text=f"Digite el numero de la pregunta que desea cambiar (1 - {cantidad_preguntas})",
                         font=("Arial bold", 30), bg="gray89")
            preguntar_numero_label.place(x=150, y=50)

            seleccionar_cuadro = tk.Entry(window, width=10, bg="black", fg="white")
            seleccionar_cuadro.place(relx=0.5, rely=0.175, height=20, anchor="c")

            seleccionar = tk.Button(window, text="Ingresar", font=("Arial bold", 15), bg="blue", fg="white",
                                    command=lambda: click_seleccionar(seleccionar_cuadro.get()))
            seleccionar.place(relx=0.5, rely=0.24, width=120, height=30, anchor="c")

            mostrar_pregunta = tk.Button(window, font=("Arial bold", 15), bg="gray82")
            mostrar_pregunta.place(relx=0.5, rely=0.35, anchor="c")
            mostrar_pregunta.place_forget()

            def click_seleccionar(numero):
                """
                Verifica el numero ingresado por el usuario
                :param Int numero: Numero ingresado por el usuario
                :return:
                """
                verificar_numero = tk.Label(window, text="", font=("Arial bold", 15),
                                            fg="red")
                verificar_numero.place(relx=0.25, rely=0.158)
                lista_preguntas.append(cantidad_preguntas)
                try:
                    if int(numero) in lista_preguntas:
                        pregunta_a_cambiar = leer_pregunta(banco_preguntas(nombre_usuario), numero, numero)[0]
                        verificar_numero.configure(text="          Pregunta encontrada    ", font=("Arial bold", 15),
                                                   fg="green", bg="gray82")
                        mostrar_pregunta.configure(text=pregunta_a_cambiar, bg="gray82")
                        mostrar_pregunta.place(relx=0.48, rely=0.42, anchor="c")

                        confirmar_pregunta_seleccionada = tk.Button(window, text="Confirmar pregunta",
                                                                    font=("Arial bold", 15),
                                                                    bg="green",
                                                                    fg="white",
                                                                    command=lambda: confirmar_pregunta(numero))
                        confirmar_pregunta_seleccionada.place(relx=0.5, rely=0.59, anchor="c")

                    else:
                        verificar_numero.configure(
                            text=f"Ingrese un valor valido (1 - {cantidad_total_preguntas(banco_preguntas(nombre_usuario))}) ",
                            font=("Arial bold", 15), fg="red", bg="gray89")


                except ValueError:
                    verificar_numero.configure(
                        text=f"Ingrese un valor valido (1 - {cantidad_total_preguntas(banco_preguntas(nombre_usuario))}) ",
                        font=("Arial bold", 15), fg="red", bg="gray89")

            def confirmar_pregunta(numero):
                """
                Confirma el numero de pregunta ingresado por el usuario
                :param Int numero: Numero de la pregunta
                :return:
                """
                limpiar_pantalla()

                regresar_menu = tk.Button(window, text="Volver al menu",
                                          font=("Arial bold", 25), command=lambda: volver_a_menu(), bg="red")
                regresar_menu.place(relx=0.9, rely=0.95, anchor="c")

                pregunta_label = tk.Label(window, text="Ingrese la pregunta :",
                                          font=("Arial bold", 15), bg="gray89").pack()

                ingresar_pregunta = ScrolledText(window, width=50, height=5)
                ingresar_pregunta.pack()

                respuesta_a = tk.Label(window, text="Ingrese la respuesta para A :",
                                       font=("Arial bold", 15), bg="gray89").place(x=0, y=150)
                ingresar_respuesta_a = tk.Entry(window, width=30, font=("Arial bold", 15))
                ingresar_respuesta_a.place(x=265, y=155)

                respuesta_b = tk.Label(window, text="Ingrese la respuesta para B :",
                                       font=("Arial bold", 15), bg="gray89").place(x=0, y=200)
                ingresar_respuesta_b = tk.Entry(window, width=30, font=("Arial bold", 15))
                ingresar_respuesta_b.place(x=265, y=206)

                respuesta_c = tk.Label(window, text="Ingrese la respuesta para C :",
                                       font=("Arial bold", 15), bg="gray89").place(x=0, y=250)
                ingresar_respuesta_c = tk.Entry(window, width=30, font=("Arial bold", 15))
                ingresar_respuesta_c.place(x=265, y=260)

                respuesta_d = tk.Label(window, text="Ingrese la respuesta para D :",
                                       font=("Arial bold", 15), bg="gray89").place(x=0, y=300)
                ingresar_respuesta_d = tk.Entry(window, width=30, font=("Arial bold", 15))
                ingresar_respuesta_d.place(x=265, y=300)

                respuesta_correcta = tk.Label(window,
                                              text="Ingrese la respuesta correcta (A, B, C o D) :",
                                              font=("Arial bold", 15), bg="gray89").place(x=0, y=350)
                ingresar_respuesta_correcta = tk.Entry(window, width=30, font=("Arial bold", 15))
                ingresar_respuesta_correcta.place(x=400, y=350)

                error = tk.Label(window, font=("Arial bold", 15))
                error.place(x=710, y=350)

                pregunta_nueva = tk.Button(window, text="",
                                           font=("Arial bold", 15))
                pregunta_nueva.place(x=0, y=400)
                pregunta_nueva.place_forget()


                longitud_error = tk.Label(window,
                                          text="Pregunta no valida, minimo 5\ncaracteres y maximo 40 caracteres",
                                          font=("Arial bold", 12), fg="red", bg="gray89")
                longitud_error.place(x=850, y=80)
                longitud_error.place_forget()

                respuesta_a_error = tk.Label(window, font=("Arial bold", 15), fg="red", bg="gray89")
                respuesta_a_error.place(x=700, y=155)

                respuesta_b_error = tk.Label(window, text="", font=("Arial bold", 15), fg="red", bg="gray89")
                respuesta_b_error.place(x=700, y=206)

                respuesta_c_error = tk.Label(window, font=("Arial bold", 15), fg="red", bg="gray89")
                respuesta_c_error.place(x=700, y=260)

                respuesta_d_error = tk.Label(window, font=("Arial bold", 15), fg="red", bg="gray89")
                respuesta_d_error.place(x=700, y=300)



                cambiar = tk.Button(window, text="Cambiar", font=("Arial bold", 15), bg="blue", fg="white",
                                    command=lambda: mostrar_nueva_pregunta(ingresar_pregunta.get(1.0, tk.END),
                                                                           ingresar_respuesta_a.get(),
                                                                           ingresar_respuesta_b.get(),
                                                                           ingresar_respuesta_c.get(),
                                                                           ingresar_respuesta_d.get(),
                                                                           ingresar_respuesta_correcta.get(),
                                                                           numero,
                                                                           pregunta_nueva,
                                                                           error,
                                                                           cambiar,
                                                                           longitud_error,
                                                                           respuesta_a_error,
                                                                           respuesta_b_error,
                                                                           respuesta_c_error,
                                                                           respuesta_d_error))

                cambiar.place(relx=0.5, rely=0.6, anchor="c")

            def mostrar_nueva_pregunta(pregunta,
                                       respuesta_a,
                                       respuesta_b,
                                       respuesta_c,
                                       respuesta_d,
                                       respuesta_correcta,
                                       numero,
                                       mostrar_pregunta,
                                       error,
                                       cambiar,
                                       longitud_error,
                                       respuesta_a_error,
                                       respuesta_b_error,
                                       respuesta_c_error,
                                       respuesta_d_error):

                """
                Muestra la pregunta que se va a cambiar
                :param String pregunta: Enunciado de la pregunta
                :param String respuesta_a: Posible respuesta
                :param String respuesta_b: Posible respuesta
                :param String respuesta_c: Posible respuesta
                :param String respuesta_d: Posible respuesta
                :param String respuesta_correcta: Respuesta correcta
                :param Int numero: Numero de la pregunta
                :param Label mostrar_pregunta: Widget que muestra la pregunta
                :param Label error: Widget que muestra un error 
                :param Button cambiar: Boton usado para cambiar la pregunta
                :param Label longitud_error: Widget que muestra un error 
                :param Label respuesta_a_error: Widget que muestra un error 
                :param Label respuesta_b_error: Widget que muestra un error 
                :param Label respuesta_c_error: Widget que muestra un error 
                :param Label respuesta_d_error: Widget que muestra un error 
                :return:
                """

                pregunta = longitud_preguntas(pregunta.strip("\n"))

                datos_pregunta_nueva = solicitar_datos_pregunta(pregunta,
                                                                respuesta_a,
                                                                respuesta_b,
                                                                respuesta_c,
                                                                respuesta_d,
                                                                respuesta_correcta,)

                if len(pregunta) > 285 or len(pregunta) < 5:
                    longitud_error.place(x=850, y=60)
                    longitud_error.configure(text="Pregunta no valida, minimo 5\ncaracteres y maximo 285 caracteres")

                if len(pregunta) <= 285 and len(pregunta) >= 5:
                    longitud_error.place_forget()

                if len(respuesta_a) == 0 or len(respuesta_a) > 40:
                    respuesta_a_error.place(x=700, y=155)
                    respuesta_a_error.configure(text="Respuesta no valida")

                else:
                    res_a = True
                    respuesta_a_error.place_forget()

                if len(respuesta_b) == 0 or len(respuesta_b) > 40:
                    respuesta_b_error.place(x=700, y=206)
                    respuesta_b_error.configure(text="Respuesta no valida")

                else:
                    res_b = True
                    respuesta_b_error.place_forget()

                if len(respuesta_c) == 0 or len(respuesta_c) > 40:
                    respuesta_c_error.place(x=700, y=260)
                    respuesta_c_error.configure(text="Respuesta no valida")

                else:
                    respuesta_c_error.place_forget()
                    res_c = True

                if len(respuesta_d) == 0 or len(respuesta_d) > 40:
                    respuesta_d_error.place(x=700, y=300)
                    respuesta_d_error.configure(text="Respuesta no valida")

                else:
                    respuesta_d_error.place_forget()
                    res_d = True

                if not (respuesta_correcta == "B" or respuesta_correcta == "C" or respuesta_correcta == "D"
                        or respuesta_correcta == "A"):
                    error.configure(text="Valor no valido, porfavor ingrese : A, B, C o D ",
                                    font=("Arial bold", 15),
                                    fg="red", bg="gray89")
                if (respuesta_correcta == "B" or respuesta_correcta == "C" or respuesta_correcta == "D"
                        or respuesta_correcta == "A"):
                    error.configure(text="Valor Valido", font=("Arial bold", 15), fg="green", bg="gray89")

                if respuesta_correcta == "B" or respuesta_correcta == "C" or respuesta_correcta == "D" \
                        or respuesta_correcta == "A" and (len(pregunta) <= 285 and len(pregunta) >= 5) and \
                        (res_a and res_b and res_c and res_d):

                    mostrar_pregunta_nueva = tk.Button(window, text=aux_anadir_preguntas(datos_pregunta_nueva),
                                                       font=("Arial bold", 15), bg="gray82")
                    mostrar_pregunta_nueva.place(relx=0.2, rely=0.7, anchor="c")
                    confirmar_cambio = tk.Button(window, text="Comfirmar cambio", font=("Arial bold", 15),
                                                 command=lambda: cambiar_pregunta(pregunta,
                                                                                  respuesta_a,
                                                                                  respuesta_b,
                                                                                  respuesta_c,
                                                                                  respuesta_d,
                                                                                  respuesta_correcta,
                                                                                  numero,
                                                                                  mostrar_pregunta_nueva,
                                                                                  cambiar,
                                                                                  confirmar_cambio),
                                                 bg="green")
                    confirmar_cambio.place(relx=0.9, rely=0.85, anchor="c")

            def cambiar_pregunta(pregunta,
                                 respuesta_a,
                                 respuesta_b,
                                 respuesta_c,
                                 respuesta_d,
                                 respuesta_correcta,
                                 numero,
                                 mostrar_pregunta_nueva,
                                 cambiar,
                                 boton_confirmar):
                """
                Cambia la pregunta por la nueva
                :param String pregunta: Enunciado de la pregunta
                :param String respuesta_a: Posible respuesta
                :param String respuesta_b: Posible respuesta
                :param String respuesta_c: Posible respuesta
                :param String respuesta_d: Posible respuesta
                :param String respuesta_correcta: Respuesta correcta
                :param Int numero: Numero de la pregunta
                :param Label mostrar_pregunta: Widget que muestra la pregunta
                :param Button cambiar: Boton usado para cmabiar la nueva pregunta 
                :param Button boton_confirmar: Boton que confirma el nuevo cambio
                :return: 
                """
                datos_pregunta_nueva = solicitar_datos_pregunta(pregunta,
                                                                respuesta_a,
                                                                respuesta_b,
                                                                respuesta_c,
                                                                respuesta_d,
                                                                respuesta_correcta, )
                parte_inicial = aux_anadir_preguntas(reemplazar_parte_inicial_parte_final(int(numero))[0])
                parte_final = aux_anadir_preguntas(reemplazar_parte_inicial_parte_final(int(numero))[1])
                datos_pregunta_añadir = [parte_inicial], \
                                 [str(numero)], \
                                 [aux_anadir_preguntas(datos_pregunta_nueva)], \
                                 [parte_final]
                with open(banco_preguntas(nombre_usuario), 'w', newline="") as f:
                    escribir = csv.writer(f, delimiter=" ", lineterminator="\n")
                    escribir.writerows(datos_pregunta_añadir)

                mostrar_pregunta_nueva.configure(text=f"{leer_pregunta(banco_preguntas(nombre_usuario), numero, numero)[0]}", bg="gray86")

                confirmacion_label = tk.Label(window, text="Pregunta cambiada satisfactoriamente",
                                              font=("Arial bold", 20), fg="green", bg="gray89")
                confirmacion_label.place(relx=0.5, rely=0.9, anchor="c")

                confirmacion_button = tk.Button(window, text="Cambiar otra pregunta", font=("Arial bold", 15),
                                                command=lambda: reemplazar_preguntas())

                confirmacion_button.place(relx=0.9, rely=0.85, anchor="c")
                boton_confirmar.destroy()
                cambiar.destroy()


        regresar_menu = tk.Button(window, text="Volver al menu",
                                  font=("Arial bold", 12), command=lambda: volver_a_menu(), bg="red")
        regresar_menu.place(relx=0.05, rely=0.03, anchor="c")


    def formular_preguntas():
        """
        Inicia el menu para crear una nueva pregunta
        :return: 
        """
        limpiar_pantalla()

        regresar_menu = tk.Button(window, text="Volver al menu",
                                  font=("Arial bold", 25), command=lambda: volver_a_menu(), bg="red")
        regresar_menu.place(relx=0.9, rely=0.95, anchor="c")

        pregunta_numero = tk.Label(window, text=f"Pregunta # {cantidad_total_preguntas(banco_preguntas(nombre_usuario))+1} ",
                                  font=("Arial bold", 15), bg="gray89").pack()

        pregunta_label = tk.Label(window, text="Ingrese la pregunta :",
                                  font=("Arial bold", 15), bg="gray89").pack()

        ingresar_pregunta = ScrolledText(window, width=50, height=5)
        ingresar_pregunta.pack()



        respuesta_a = tk.Label(window, text="Ingrese la respuesta para A :",
                               font=("Arial bold", 15), bg="gray89").place(x=0, y=150)
        ingresar_respuesta_a = tk.Entry(window, width=30, font=("Arial bold", 15))
        ingresar_respuesta_a.place(x=265, y=155)

        respuesta_b = tk.Label(window, text="Ingrese la respuesta para B :",
                               font=("Arial bold", 15), bg="gray89").place(x=0, y=200)
        ingresar_respuesta_b = tk.Entry(window, width=30, font=("Arial bold", 15))
        ingresar_respuesta_b.place(x=265, y=206)

        respuesta_c = tk.Label(window, text="Ingrese la respuesta para C :",
                               font=("Arial bold", 15), bg="gray89").place(x=0, y=250)
        ingresar_respuesta_c = tk.Entry(window, width=30, font=("Arial bold", 15))
        ingresar_respuesta_c.place(x=265, y=260)

        respuesta_d = tk.Label(window, text="Ingrese la respuesta para D :",
                               font=("Arial bold", 15), bg="gray89").place(x=0, y=300)
        ingresar_respuesta_d = tk.Entry(window, width=30, font=("Arial bold", 15))
        ingresar_respuesta_d.place(x=265, y=300)

        respuesta_correcta = tk.Label(window,
                                      text="Ingrese la respuesta correcta (A, B, C o D) :",
                                      font=("Arial bold", 15), bg="gray89").place(x=0, y=350)
        ingresar_respuesta_correcta = tk.Entry(window, width=30, font=("Arial bold", 15))
        ingresar_respuesta_correcta.place(x=400, y=350)

        error = tk.Label(window, font=("Arial bold", 15))
        error.place(x=710, y=350)

        pregunta_nueva = tk.Button(window, text="",
                         font=("Arial bold", 15))
        pregunta_nueva.place(x=0, y=400)
        pregunta_nueva.place_forget()

        numero = cantidad_total_preguntas(banco_preguntas(nombre_usuario))

        longitud_error = tk.Label(window, text="Pregunta no valida, minimo 5\ncaracteres y maximo 40 caracteres",
                                  font=("Arial bold", 12), fg="red", bg="gray89")
        longitud_error.place(x=850, y=80)
        longitud_error.place_forget()

        respuesta_a_error = tk.Label(window, font=("Arial bold", 15), fg="red", bg="gray89")
        respuesta_a_error.place(x=700, y=155)

        respuesta_b_error = tk.Label(window, text="", font=("Arial bold", 15), fg="red", bg="gray89")
        respuesta_b_error.place(x=700, y=206)

        respuesta_c_error = tk.Label(window, font=("Arial bold", 15), fg="red", bg="gray89")
        respuesta_c_error.place(x=700, y=260)

        respuesta_d_error = tk.Label(window, font=("Arial bold", 15), fg="red", bg="gray89")
        respuesta_d_error.place(x=700, y=300)

        crear = tk.Button(window, text="Crear pregunta", font=("Arial bold", 20), bg="blue", fg="white",
                            command=lambda: crear_nueva_pregunta(ingresar_pregunta.get(1.0, tk.END),
                                                                 ingresar_respuesta_a.get(),
                                                                 ingresar_respuesta_b.get(),
                                                                 ingresar_respuesta_c.get(),
                                                                 ingresar_respuesta_d.get(),
                                                                 ingresar_respuesta_correcta.get(),
                                                                 numero,
                                                                 error,
                                                                 pregunta_nueva,
                                                                 crear,
                                                                 longitud_error,
                                                                 respuesta_a_error,
                                                                 respuesta_b_error,
                                                                 respuesta_c_error,
                                                                 respuesta_d_error))

        crear.place(relx=0.5, y=440, anchor="c")
        def crear_nueva_pregunta(pregunta,
                                 respuesta_a,
                                 respuesta_b,
                                 respuesta_c,
                                 respuesta_d,
                                 respuesta_correcta,
                                 numero,
                                 label,
                                 pregunta_nueva,
                                 crear,
                                 longitud_error,
                                 respuesta_a_error,
                                 respuesta_b_error,
                                 respuesta_c_error,
                                 respuesta_d_error):
            """
            :param String pregunta: Enunciado de la pregunta
            :param String respuesta_a: Posible respuesta
            :param String respuesta_b: Posible respuesta
            :param String respuesta_c: Posible respuesta
            :param String respuesta_d: Posible respuesta
            :param String respuesta_correcta: Respuesta correcta
            :param Int numero: Numero de la pregunta
            :param Label label: Widget que muestra un error 
            :param Label pregunta_nueva: Widget que muestra la nueva pregunta
            :param Label label: Widget que muestra un error 
            :param Button crear: Boton usado para crear la pregunta
            :param Label longitud_error: Widget que muestra un error 
            :param Label respuesta_a_error: Widget que muestra un error 
            :param Label respuesta_b_error: Widget que muestra un error 
            :param Label respuesta_c_error: Widget que muestra un error 
            :param Label respuesta_d_error: Widget que muestra un error 
            :return: 
            """


            if len(pregunta) > 285 or len(pregunta) < 5:
                longitud_error.place(x=850, y=80)
                longitud_error.configure(text="Pregunta no valida, minimo 5\ncaracteres y maximo 285 caracteres")

            if len(pregunta) <= 285 and len(pregunta) >= 5:
                longitud_error.place_forget()

            if len(respuesta_a) == 0 or len(respuesta_a) > 40:
                respuesta_a_error.place(x=700, y=155)
                respuesta_a_error.configure(text="Respuesta no valida")

            else:
                res_a = True
                respuesta_a_error.place_forget()

            if len(respuesta_b) == 0 or len(respuesta_b) > 40:
                respuesta_b_error.place(x=700, y=206)
                respuesta_b_error.configure(text="Respuesta no valida")

            else:
                res_b = True
                respuesta_b_error.place_forget()

            if len(respuesta_c) == 0 or len(respuesta_c) > 40:
                respuesta_c_error.place(x=700, y=260)
                respuesta_c_error.configure(text="Respuesta no valida")

            else:
                respuesta_c_error.place_forget()
                res_c = True

            if len(respuesta_d) == 0 or len(respuesta_d) > 40:
                respuesta_d_error.place(x=700, y=300)
                respuesta_d_error.configure(text="Respuesta no valida")

            else:
                respuesta_d_error.place_forget()
                res_d = True

            if not (respuesta_correcta == "B" or respuesta_correcta == "C" or respuesta_correcta == "D"
                    or respuesta_correcta == "A"):
                error.configure(text="Valor no valido, porfavor ingrese : A, B, C o D ",
                                font=("Arial bold", 15),
                                fg="red", bg="gray89")
            if (respuesta_correcta == "B" or respuesta_correcta == "C" or respuesta_correcta == "D"
                    or respuesta_correcta == "A"):
                error.configure(text="Valor Valido", font=("Arial bold", 15), fg="green", bg="gray89")


            if respuesta_correcta == "B" or respuesta_correcta == "C" or respuesta_correcta == "D"\
                    or respuesta_correcta == "A" and(len(pregunta) <= 285 and len(pregunta) >= 5) and\
                    (res_a and res_d and res_b and res_c):
                crear.place_forget()
                pregunta = longitud_preguntas(pregunta.strip("\n"))
                datos_pregunta_nueva = solicitar_datos_pregunta(pregunta,
                                                                respuesta_a,
                                                                respuesta_b,
                                                                respuesta_c,
                                                                respuesta_d,
                                                                respuesta_correcta)
                hacer_preguntas(numero, datos_pregunta_nueva)
                pregunta_nueva.configure(text=f"{leer_pregunta(banco_preguntas(nombre_usuario), numero + 1, numero + 1)[0]}", bg="gray86")
                pregunta_nueva.place(relx=0.4, rely=0.7, anchor="c")

                confirmar_creacion = tk.Button(window, text="Crear otra pregunta", font=("Arial bold", 15),
                                             command=lambda: crear_otra_pregunta(),
                                             bg="green")

                confirmar_creacion.place(relx=0.9, rely=0.85, anchor="c")

            def crear_otra_pregunta():
                """
                Reinicia el proceso de crear preguntas
                :return: 
                """
                formular_preguntas()


    def longitud_preguntas(pregunta):
        """
        Divide la pregunta en varias lineas dependiendo de la longitud
        :param String pregunta: Enunciado de la pregunta 
        :return: String divido en varias lineas
        """
        pregunta = pregunta.split(" ")
        nuevo_texto = ""
        z = 0
        x = 0
        for palabra in pregunta:
            z = len(palabra) + z
            if z < 95 :
                nuevo_texto = nuevo_texto + palabra + " "
                nuevo_texto.strip(" ")
                if z == 95:
                    nuevo_texto = nuevo_texto.strip(" ")
                if z != 95:
                    z = z + 1
            if z >= 95:
                z = 0
                nuevo_texto = nuevo_texto + "\n" + palabra + " "
                z = len(palabra) + z + 1
        nuevo_texto.strip(" ")
        return nuevo_texto


    def estadisticas(usuario):
        """
        Muestra las estadisticas totales del usuario
        :param String usuario: Nombre del usuario  
        :return: 
        """
        limpiar_pantalla()

        contorno = tk.Button(window, state="disable", width=48, height=20, bg="green3")
        contorno.place(relx=0.5, rely=0.4, anchor="c")

        lista = convertir(banco_preguntas(usuario))
        lista = lista[1].split(" ")
        string_p = "Total preguntas realizadas"
        string_a = "Total Aciertos"
        string_e = "Total fallos"
        s_promed = "Porcentaje de aciertos"


        if int(lista[0]) == 0:
            promedio = 0
        else:
            promedio = (int(lista[1]) * 100) // int(lista[0])

        estadistica_preguntas = tk.Label(window, text=f"{string_p:<30}",
                                         font=("Arial bold", 12), bg="green3")
        estadistica_preguntas.place(relx=0.4, rely=0.3)

        estadistica_preguntasn = tk.Label(window, text=f": {lista[0]}",
                                          font=("Arial bold", 12), bg="green3")
        estadistica_preguntasn.place(relx=0.57, rely=0.3)


        estadistica_aciertos = tk.Label(window, text=f"{string_a:<30}",
                                        font=("Arial bold", 12), bg="green3")
        estadistica_aciertos.place(relx=0.4, rely=0.34)

        estadistica_aciertosn = tk.Label(window, text=f": {lista[1]}",
                                         font=("Arial bold", 12), bg="green3")
        estadistica_aciertosn.place(relx=0.57, rely=0.34)

        estadistica_fallos = tk.Label(window, text=f"{string_e:<30}",
                                      font=("Arial bold", 12), bg="green3")
        estadistica_fallos.place(relx=0.4, rely=0.38)

        estadistica_fallosn = tk.Label(window, text=f": {lista[2]}",
                                       font=("Arial bold", 12), bg="green3")
        estadistica_fallosn.place(relx=0.57, rely=0.38)

        estadistica_porcentaje_aciertos = tk.Label(window, text=f"{s_promed:<30}",
                                                   font=("Arial bold", 12), bg="green3")
        estadistica_porcentaje_aciertos.place(relx=0.4, rely=0.42)

        estadistica_porcentaje_aciertosn = tk.Label(window, text=f": {promedio}%",
                                                    font=("Arial bold", 12), bg="green3")
        estadistica_porcentaje_aciertosn.place(relx=0.57, rely=0.42)

        regresar_menu = tk.Button(window, text="Volver al menu",
                                  font=("Arial bold", 12), command=lambda: volver_a_menu(), bg="red")
        regresar_menu.place(relx=0.05, rely=0.03, anchor="c")


    def cambiar_contraseña(usuario):
        """
        Cambia la contraseña del usuario actual
        :param String usuario: Nombre del usuario 
        :return: 
        """

        limpiar_pantalla()

        contraseña = convertir(banco_preguntas(usuario))
        contraseña_original = contraseña[0]

        volver = tk.Button(window, text="Volver", font=("Arial bold", 15), bg="red", command=lambda: volver_a_menu())
        volver.place(relx=0.0, rely=0.0)

        contorno = tk.Button(window, state="disable", width=48, height=20, bg="gray77")
        contorno.place(relx=0.5, rely=0.5, anchor="c")

        contraseña_antigua = tk.Label(window, text="Contraseña Antigua", bg="gray77")
        contraseña_antigua.place(relx=0.5, rely=0.36, anchor="c")

        contraseña_antigua_dato = tk.Entry(window, width=15, font=("Arial bold", 15), show="*")
        contraseña_antigua_dato.place(relx=0.5, rely=0.40, anchor="c")


        titulo = tk.Label(window, text="Introduzca su contraseña antigua y la nueva contraseña", bg="gray77")
        titulo.place(relx=0.5, rely=0.32, anchor="c")

        clave_nueva = tk.Label(window, text="Contraseña ", bg="gray77")
        clave_nueva.place(relx=0.5, rely=0.46, anchor="c")

        clave_nueva_dato = tk.Entry(window, width=15, font=("Arial bold", 15), show="*")
        clave_nueva_dato.place(relx=0.5, rely=0.50, anchor="c")

        confirmar_clave_nueva = tk.Label(window, text="Confirmar contraseña", bg="gray77")
        confirmar_clave_nueva.place(relx=0.5, rely=0.54, anchor="c")

        confirmar_clave_nueva_dato = tk.Entry(window, width=15, font=("Arial bold", 15), show="*")
        confirmar_clave_nueva_dato.place(relx=0.5, rely=0.58, anchor="c")

        confirmar_clave_error = tk.Label(window, text="La contraseña no coincide", fg="red", bg="gray77")
        confirmar_clave_error.place(relx=0.5, rely=0.62, anchor="c")
        confirmar_clave_error.place_forget()

        confirmar_clave_antigua_error = tk.Label(window, text="Contraseña incorrecta", fg="red", bg="gray77")
        confirmar_clave_antigua_error.place(relx=0.5, rely=0.43, anchor="c")
        confirmar_clave_antigua_error.place_forget()

        verificar_contraseña_cambio = tk.Button(window, text="Cambiar", font=("Arial bold", 15), bg="gray64",
                                 command=lambda: verificar_contraseña_cambiar(contraseña_original,
                                                                              contraseña_antigua_dato.get(),
                                                                              clave_nueva_dato.get(),
                                                                              confirmar_clave_nueva_dato.get(),
                                                                              confirmar_clave_error,
                                                                              confirmar_clave_antigua_error,
                                                                              usuario))
        verificar_contraseña_cambio.place(relx=0.5, rely=0.67, anchor="c")


    def verificar_contraseña_cambiar(contraseña_antigua, contraseña_usuario,
                                     contraseña_nueva, confirmar_contra_nueva,
                                     error_clave_nueva, error_clave_antigua, usuario):

        """
        Verifica si los datos ingresados son correctas y si la nueva contraseña cumple con los parametros
        :param String contraseña_antigua: Contraseña antigual del usuario
        :param String contraseña_usuario: Contraseña antigua que el usuario digita
        :param String contraseña_nueva: Contraseña nueva
        :param String confirmar_contra_nueva: Verifica la contraseña nueva
        :param Label error_clave_nueva: Widget que aparece si hay en error 
        :param Label error_clave_antigua: Widget que aparece si hay en error 
        :param String usuario: Nombre del usuario
        :return: 
        """

        if contraseña_antigua == contraseña_usuario:
            error_clave_antigua.place_forget()

            if contraseña_nueva == confirmar_contra_nueva:
                error_clave_nueva.place_forget()

                if len(contraseña_nueva) < 6 or len(contraseña_nueva) > 15:
                    error_clave_antigua.place(relx=0.5, rely=0.62, anchor="c")
                    error_clave_antigua.configure(text="Contraseña no valida")

                if len(contraseña_nueva) >= 6 and len(contraseña_nueva) <= 15:
                    contraseña_actualizada = contraseña_nueva

                    cambiar_clave(contraseña_actualizada, usuario)

                    if contraseña_nueva == leer_contraseña(usuario, error_clave_antigua):
                        creacion = tk.Label(window, text="Contraseña cambia satisfactoriamente",
                                            font=("Arial bold", 20), fg="green")
                        creacion.place(relx=0.5, rely=0.8, anchor="c")

                        iniciar_sesion = tk.Button(window, text="Iniciar Sesion",
                                                   font=("Arial bold", 25), bg="green", command=lambda: log_in())
                        iniciar_sesion.place(relx=0.5, rely=0.87, anchor="c")


            else:
                error_clave_nueva.place(relx=0.5, rely=0.62, anchor="c")

        else:
            error_clave_antigua.place(relx=0.5, rely=0.435, anchor="c")
            error_clave_antigua = tk.Label(window, text="Contraseña incorrecta", fg="red", bg="gray77")


    def cambiar_clave(nueva_contraseña, usuario):
        """
        Cambia la clave que esta en el documento
        :param String nueva_contraseña: Nueva contrasela 
        :param String usuario: Nombre del usuario 
        :return: 
        """
        usuario_cambio = banco_preguntas(usuario)
        lista = convertir(usuario_cambio)
        lista_final = []
        for x in range(1, len(lista)):
            lista_final.append(lista[x])
        lista_final = aux_anadir_preguntas(lista_final)
        datos = [nueva_contraseña], [lista_final]
        with open(usuario_cambio, "w", newline="") as f:
            escribir = csv.writer(f, delimiter=" ", lineterminator="\n")
            escribir.writerows(datos)


    def eliminar_preguntas():
        """
        Inicia el menu para eliminar preguntas
        :return: 
        """
        limpiar_pantalla()
        if (cantidad_total_preguntas(banco_preguntas(nombre_usuario))) == 0:

            aviso_fondo = tk.Button(window, bg="misty rose", width=200, height=100)
            aviso_fondo.place(relx=0.5, rely=0.5, anchor="c")

            aviso = tk.Button(window, text="NO HAY NINGUNA PREGUNTA PARA ELIMINAR, CLICK AQUI\n PARA CREAR UNA NUEVA PREGUNTA",
                                font=("Arial bold", 25), fg="white", bg="red4", command=lambda:formular_preguntas())
            aviso.place(relx=0.5, rely=0.5, anchor="c")
        else:
            cantidad_preguntas = cantidad_total_preguntas(banco_preguntas(nombre_usuario))
            lista_preguntas = lista_preguntas_totales(cantidad_total_preguntas(banco_preguntas(nombre_usuario)))
            lista_nueva = ""
            for x in range(len(lista_preguntas)):
                lista_nueva = lista_nueva + str(lista_preguntas[x] + 1) + " "

            preguntar_numero_label = \
                tk.Label(window,
                         text=f"Digite el numero de la pregunta que desea eliminar (1 - {cantidad_preguntas})",
                         font=("Arial bold", 30), bg="gray89")
            preguntar_numero_label.place(x=150, y=50)

            seleccionar_cuadro = tk.Entry(window, width=10, bg="black", fg="white")
            seleccionar_cuadro.place(relx=0.5, rely=0.175, height=20, anchor="c")

            seleccionar = tk.Button(window, text="Ingresar", font=("Arial bold", 15), bg="blue", fg="white",
                                    command=lambda: click_eliminar(seleccionar_cuadro.get()))
            seleccionar.place(relx=0.5, rely=0.24, width=120, height=30, anchor="c")

            mostrar_pregunta = tk.Button(window, font=("Arial bold", 15))
            mostrar_pregunta.place(relx=0.5, rely=0.340, anchor="c")
            mostrar_pregunta.place_forget()

            def click_eliminar(numero):
                """
                Verifica el numero de la pregunta ingresada 
                :param Int numero: Numero de la pregunta
                :return: 
                """
                verificar_numero = tk.Label(window, text="", font=("Arial bold", 15),
                                            fg="red")
                verificar_numero.place(relx=0.25, rely=0.158)
                try:
                    if int(numero) in lista_preguntas:
                        pregunta_a_cambiar = leer_pregunta(banco_preguntas(nombre_usuario), numero, numero)[0]
                        verificar_numero.configure(text="          Pregunta encontrada    ", font=("Arial bold", 15),
                                                   fg="green", bg="gray82")
                        mostrar_pregunta.configure(text=f"Esta eliminando la {pregunta_a_cambiar}", bg="gray82")
                        mostrar_pregunta.place(relx=0.48, rely=0.42, anchor="c")

                        eliminar_pregunta_seleccionada = tk.Button(window, text="Eliminar pregunta",
                                                                   font=("Arial bold", 15),
                                                                   bg="green",
                                                                   fg="white",
                                                                   command=lambda: eliminar_pregunta(numero, ))
                        eliminar_pregunta_seleccionada.place(relx=0.5, rely=0.59, anchor="c")

                    if int(numero) not in lista_preguntas:
                        verificar_numero.configure(
                            text=f"Ingrese un valor valido (1 - {cantidad_total_preguntas(banco_preguntas(nombre_usuario))}) ",
                            font=("Arial bold", 15), fg="red")

                except ValueError:
                    verificar_numero.configure(
                        text=f"Ingrese un valor valido (1 - {cantidad_total_preguntas(banco_preguntas(nombre_usuario))}) ",
                        font=("Arial bold", 15), fg="red")

        regresar_menu = tk.Button(window, text="Volver al menu",
                                  font=("Arial bold", 12), command=lambda: volver_a_menu(), bg="red")
        regresar_menu.place(relx=0.05, rely=0.03, anchor="c")


        def eliminar_pregunta(numero):
            """
            Llama a la funcion que Elimina la pregunta del documento y reinicia el proceso
            :param Int numero: Numero de la pregunta a eliminar 
            :return: 
            """
            eliminar_pregunta_especifica(int(numero))
            eliminar_preguntas()


    def ver_preguntas(pagina=0):
        """
        Inicia el proceso para ver las preguntas totales almacenadas
        :param Int pagina: Numero de la pagina 
        :return: 
        """
        limpiar_pantalla()
        if (cantidad_total_preguntas(banco_preguntas(nombre_usuario))) == 0:
            aviso = tk.Button(window, text="NO HAY NINGUNA PREGUNTA PARA MOSTRAR, PRUEBA\n CREAR UNA NUEVA EN LA OPCION FORMULAR",
                                font=("Arial bold", 25), state="disable")
            aviso.place(relx=0.5, rely=0.5, anchor="c")

        else:
            paginas, cantidad_paginas, sobras = aux_mostrar_preguntas()
            if sobras > 0:
                if pagina < cantidad_paginas:
                    for x in range(3):
                        preguntas_recuadro = tk.Button(window, state="disable", width=120, height=10, bg="gray86")
                        preguntas_recuadro.place(x=225, y=(160 * x) + 55)

                        preguntas = tk.Label(window,
                                             text=leer_pregunta(banco_preguntas(nombre_usuario),
                                                                paginas[pagina][x], (pagina * 3 + x) + 1)[0],
                                             font=("Arial bold", 12), bg="gray86")
                        preguntas.place(x=235, y=(160 * x) + 60)

                        respuesta_recuadro = tk.Button(window, state="disable", width=25, height=10, bg="gray86")
                        respuesta_recuadro.place(x=1075, y=(160 * x) + 55)

                        correcta = tk.Label(window, text=leer_pregunta(banco_preguntas(nombre_usuario),
                                                                paginas[pagina][x], (pagina * 3 + x))[1],
                                            font=("Arial bold", 25), bg="gray86")
                        correcta.place(x=1150, y=(160 * x) + 100)

                else:
                    for x in range(0, sobras):
                        preguntas_recuadro = tk.Button(window, state="disable", width=120, height=10, bg="gray86")
                        preguntas_recuadro.place(x=225, y=(160 * x) + 55)

                        preguntas = tk.Label(window,
                                             text=leer_pregunta(banco_preguntas(nombre_usuario),
                                                                paginas[pagina][x], (cantidad_paginas * 3 + x) + 1)[0],
                                             font=("Arial bold", 12), bg="gray86")
                        preguntas.place(x=235, y=(160 * x) + 60)

                        respuesta_recuadro = tk.Button(window, state="disable", width=25, height=10, bg="gray86")
                        respuesta_recuadro.place(x=1075, y=(160 * x) + 55)

                        correcta = tk.Label(window, text=leer_pregunta(banco_preguntas(nombre_usuario),
                                                                       paginas[pagina][x], (pagina * 3 + x))[1],
                                            font=("Arial bold", 25), bg="gray86")
                        correcta.place(x=1150, y=(160 * x) + 100)

                if pagina != cantidad_paginas:
                    siguiente = tk.Button(window, text="Siguiente", font=("Arial bold", 15),
                                          command=lambda: pagina_siguiente(pagina), bg="green")
                    siguiente.place(relx=0.9, rely=0.9, anchor="c")

                numero_paginas = tk.Label(window, text=f"Página {pagina + 1} / {cantidad_paginas + 1}",
                                          font=("Arial bold", 14))
                numero_paginas.place(relx=0.5, rely=0.95, anchor="c")

            elif sobras == 0:
                for x in range(3):
                    preguntas_recuadro = tk.Button(window, state="disable", width=120, height=10, bg="gray86")
                    preguntas_recuadro.place(x=225, y=(160 * x) + 55)

                    preguntas = tk.Label(window,
                                         text=leer_pregunta(banco_preguntas(nombre_usuario),
                                                            paginas[pagina][x], (pagina * 3 + x) + 1)[0],
                                         font=("Arial bold", 12), bg="gray86")
                    preguntas.place(x=235, y=(160 * x) + 60)

                    respuesta_recuadro = tk.Button(window, state="disable", width=25, height=10, bg="gray86")
                    respuesta_recuadro.place(x=1075, y=(160 * x) + 55)

                    correcta = tk.Label(window, text=leer_pregunta(banco_preguntas(nombre_usuario),
                                                                   paginas[pagina][x], (pagina * 3 + x))[1],
                                        font=("Arial bold", 25), bg="gray86")
                    correcta.place(x=1150, y=(160 * x) + 100)

                if pagina + 1 != cantidad_paginas:
                    siguiente = tk.Button(window, text="Siguiente", font=("Arial bold", 15),
                                          command=lambda: pagina_siguiente(pagina), bg="green")
                    siguiente.place(relx=0.95, rely=0.9, anchor="c")

                numero_paginas = tk.Label(window, text=f"Página {pagina + 1} / {cantidad_paginas}",
                                          font=("Arial bold", 14))
                numero_paginas.place(relx=0.5, rely=0.95, anchor="c")

        regresar_menu = tk.Button(window, text="Volver al menu",
                                  font=("Arial bold", 12), command=lambda: volver_a_menu(), bg="red")
        regresar_menu.place(relx=0.05, rely=0.03, anchor="c")


    def pagina_siguiente(pagina):
        """
        Muestra la siguiente pagina
        :param Int pagina: Numero de la pagina actual 
        :return: 
        """
        ver_preguntas(pagina+1)
        anterior = tk.Button(window, text="Atras", font=("Arial bold", 15),
                             command=lambda: pagina_anterior(pagina), bg="green")
        anterior.place(relx=0.05, rely=0.9, anchor="c")


    def pagina_anterior(pagina):
        """
        Muestra la pagina anterior
        :param Int pagina: Numero de la pagina actual 
        :return: 
        """
        ver_preguntas(pagina)
        if pagina != 0:
            anterior = tk.Button(window, text="Atras", font=("Arial bold", 15),
                                 command=lambda: pagina_anterior(pagina-1), bg="green")
            anterior.place(relx=0.05, rely=0.9, anchor="c")


    def administar_usuarios():
        """
        Inicializa el menu que permite modificar ciertas cosas de los usuarios
        :return: 
        """
        lista_aux = ("Nombre usuario",)
        limpiar_pantalla()
        usuarios = convertir(banco_preguntas("usuarios"))
        for x in usuarios:
            if x != '"' and x != " " and x !="" and x != "administrador":
                lista_aux = lista_aux + (x,)
        titulo = tk.Label(window, text="Seleccione el nombre de usuario", font=("Arial bold", 20), bg="gray89")
        titulo.place(relx=0.5, rely=0.1, anchor="c")

        elegir = ttk.Combobox(window)
        elegir["values"] = lista_aux
        elegir.current(0)
        elegir.place(relx=0.5, rely=0.2, anchor="c")

        ver_datos = tk.Label(window)
        ver_datos.place(relx=0.5, rely=0.5)
        ver_datos.place_forget()

        seleccion_elimiar = tk.Button(window, text="Eliminar", bg="red", font=("Arial bold", 20),
                                      command=lambda: selec_eliminar_usuario(elegir.get(), lista_aux, ver_datos))
        seleccion_elimiar.place(relx=0.4, y=240, width=245, height=100, anchor="c")

        seleccion_ver_clave = tk.Button(window, text="Ver contraseña", bg="blue", font=("Arial bold", 20),
                                        command=lambda: selec_ver_clave(elegir.get(), ver_datos))
        seleccion_ver_clave.place(relx=0.6, y=240, width=245, height=100, anchor="c")



        regresar_menu = tk.Button(window, text="Volver al menu",
                                  font=("Arial bold", 12), command=lambda: volver_a_menu(), bg="red")
        regresar_menu.place(relx=0.05, rely=0.03, anchor="c")

        seleccion_ver_estadisticas = tk.Button(window, text="Ver estadisticas", bg="gray82", font=("Arial bold", 20),
                                        command=lambda: selec_ver_estadisticas(elegir.get(), ver_datos))
        seleccion_ver_estadisticas.place(relx=0.4, y=360, width=245, height=100, anchor="c")

        seleccion_reiniciar_estadisticas = tk.Button(window, text="Reiniciar Estadisticas", bg="gray70", font=("Arial bold", 19),
                                        command=lambda: selec_reiniciar_estadisticas(elegir.get(), ver_datos))
        seleccion_reiniciar_estadisticas.place(relx=0.6, y=360, width=245, height=100, anchor="c")


    def selec_eliminar_usuario(nombre_de_usuario, lista, mensaje):
        """
        Elimina el usuario elegido
        :param String nombre_de_usuario: Nombre del usuario que va a ser eliminado  
        :param List lista: Lista con el nombre de todos los usuarios
        :param Label mensaje: Widget que da informacion 
        :return: 
        """
        if nombre_de_usuario == "Nombre usuario":
            mensaje.place(relx=0.5, rely=0.6, anchor="c")
            mensaje.configure(text="Por favor elija un nombre de usuario",
                                   font=("Arial bold", 15), bg="gray88")
        else:
            nuevos_usuarios = []
            for x in range(len(lista)):
                if lista[x] != "Nombre usuario" and lista[x] != "administrador" and lista[x] != nombre_de_usuario:
                    nuevos_usuarios.append(lista[x])

            nueva_lista = ""
            for x in range(len(nuevos_usuarios)):
                nueva_lista = nueva_lista + str(nuevos_usuarios[x]) + "\n"
            nueva_lista = nueva_lista.strip("\n")

            datos_nuevo_documento = ["administrador"], [nueva_lista]

            direccion = "../Recursor/" + nombre_de_usuario + ".csv"
            remove(direccion)

            with open("../Recursor/usuarios.csv", "w", newline="") as f:
                escribir = csv.writer(f, delimiter=" ", lineterminator="\n")
                escribir.writerows(datos_nuevo_documento)
            administar_usuarios()


    def selec_ver_clave(usuario, v_contraseña):
        """
        Permite ver la clave del usuaio elegido
        :param String usuario: Nombre del usuario 
        :param Label v_contraseña: Widget que muestra la contraseña del usuario elegido 
        :return: 
        """
        if usuario == "Nombre usuario":
            v_contraseña.place(relx=0.5, rely=0.65, anchor="c")
            v_contraseña.configure(text="Por favor elija un nombre de usuario",
                                   font=("Arial bold", 15), bg="gray88")
        else:
            contraseña = leer_contraseña(usuario, v_contraseña)

            v_contraseña.place(relx=0.5, rely=0.65, anchor="c")
            v_contraseña.configure(text=f"La contraseña del usuario {usuario} es: {contraseña}",
                                  font=("Arial bold", 15), bg="gray88")


    def selec_ver_estadisticas(usuario, estadisticas_label):
        """
        Muestra las estadisticas del usuario
        :param String usuario: Nombre de usuario 
        :param Label estadisticas_label: Widget que muestra las estadisticas del usuario elegido 
        :return: 
        """
        try:
            lista = convertir(banco_preguntas(usuario))
            estadisticas_usuario = lista[1].split(" ")
            print(estadisticas_usuario)
            cantidad_total = f"Cantidad total de preguntas : {estadisticas_usuario[0]}"
            aciertos =f"Cantidad de aciertos : {estadisticas_usuario[1]}"
            fallos = f"Cantidad de fallos : {estadisticas_usuario[2]}"
            estadisticas_label.configure(text=f"Estadisticas de {usuario} \n {cantidad_total} \n {aciertos} \n {fallos}",
                                         font=("Arial bold", 15), bg="gray88")
            estadisticas_label.place(relx=0.5, rely=0.65, anchor="c")
        except FileNotFoundError:
            estadisticas_label.configure(text="Porfavor Seleccione un nombre de usuario",
                                         font=("Arial bold", 15), bg="gray88")
            estadisticas_label.place(relx=0.5, rely=0.65, anchor="c")


    def selec_reiniciar_estadisticas(usuario, estadisticas_label):
        """
        Reinicia las estadisticas del usuario
        :param String usuario: Nombre del usuario
        :param Label estadisticas_label: Widget que verifica el reinicio de las estadisticas 
        :return: 
        """
        try:
            parte_inicial, parte_final = aux_estadisticas()
            lista = convertir(banco_preguntas(usuario))
            lista = lista[1].split(" ")
            lista_aux = lista
            lista_aux[0] = 0
            lista_aux[1] = 0
            lista_aux[2] = 0
            datos = ""
            for x in range(len(lista)):
                datos = datos + str(lista_aux[x]) + " "
            datos_nuevos = [parte_inicial], [datos], [parte_final]

            with open(banco_preguntas(usuario), 'w', newline="") as f:
                escribir = csv.writer(f, delimiter=" ", lineterminator="\n")
                escribir.writerows(datos_nuevos)

            estadisticas_label.configure(text="Estadisticas Reiniciadas Correctamente",
                                         font=("Arial bold", 15), bg="gray88")
            estadisticas_label.place(relx=0.5, rely=0.65, anchor="c")

        except FileNotFoundError:
            estadisticas_label.configure(text="Porfavor Seleccione un nombre de usuario",
                                         font=("Arial bold", 15), bg="gray88")
            estadisticas_label.place(relx=0.5, rely=0.65, anchor="c")


    def cerrar_aplicacion():
        """
        Cierra la aplicacion
        :return: 
        """
        window.destroy()

    def iniciar_menu(nombre_sesion):
        """
        Inicializa el menu principal donde el usuario puede interactuar con las principales caracteristicas del programa
        :param String nombre_sesion: Nombre del usuario 
        :return: 
        """

        titulo_aplicacion = tk.Label(window, text="Quiz Maker", font=("Arial bold", 32), bg="gray88")
        titulo_aplicacion.place(x=600, y=100,)

        opcion_responder = tk.Button(window, text="Responder Preguntas",
                                     font=("Arial bold", 25), command=responder_preguntas, bg="gray50")
        opcion_responder.place(x=510, y=180, width=400, height=50)

        opcion_formular = tk.Button(window, text="Formular preguntas",
                                    font=("Arial bold", 25), bg="gray50", command=lambda: formular_preguntas())
        opcion_formular.place(x=510, y=230, width=400, height=50)

        opcion_reemplazar = tk.Button(window, text="Reemplazar preguntas",
                                      font=("Arial bold", 25), bg="gray50", command=lambda: reemplazar_preguntas())
        opcion_reemplazar.place(x=510, y=280, width=400, height=50)

        opcion_eliminar = tk.Button(window, text="Eliminar preguntas",
                                    font=("Arial bold", 25), bg="gray50", command= lambda: eliminar_preguntas())
        opcion_eliminar.place(x=510, y=330, width=400, height=50)

        opcion_ver_preguntas = tk.Button(window, text="Ver todas las preguntas",
                                         font=("Arial bold", 25), bg="gray50", command=lambda: ver_preguntas())
        opcion_ver_preguntas.place(x=510, y=380, width=400, height=50)

        opcion_estadisticas = tk.Button(window, text="Estadisticas",
                                        font=("Arial bold", 25), bg="gray50", command=lambda: estadisticas(nombre_usuario))
        opcion_estadisticas.place(x=510, y=430, width=400, height=50)

        opcion_salir = tk.Button(window, text="Salir",
                                 font=("Arial bold", 25), command=lambda: cerrar_aplicacion(), bg="red")
        opcion_salir.place(x=510, y=550, width=400, height=50)

        recuadro_sesion = tk.Button(window, state="disable", width=36, height=12, bg="gray60")
        recuadro_sesion.place(relx=0.9, rely=0.1, anchor="c")

        nombre_sesion_actual = tk.Button(window,
                                         text=f"Bienvenido\n{nombre_sesion}", font=("Arial bold", 20), state="disable")
        nombre_sesion_actual.place(relx=0.9, rely=0.05, anchor="c")

        opcion_cerrar_sesion = tk.Button(window, text="Cerrar sesion",
                                         font=("Arial bold", 10), command=lambda: log_in(), bg="green")
        opcion_cerrar_sesion.place(relx=0.9, rely=0.20, anchor="c")

        opcion_cambiar_contraseña = tk.Button(window, text="Cambiar Clave",
                                         font=("Arial bold", 10), command=lambda: cambiar_contraseña(nombre_usuario), bg="green")
        opcion_cambiar_contraseña.place(relx=0.9, rely=0.15, anchor="c")

        if nombre_sesion == "administrador":
            recuadro_sesion.configure(width=36, height=17)
            opcion_administar = tk.Button(window, text="Administrar Usuarios",
                                             font=("Arial bold", 10), command=lambda: administar_usuarios(), bg="green")
            opcion_administar.place(relx=0.9, rely=0.25, anchor="c")


    menu_inicial()
    #iniciar_menu()
    window.configure(bg="gray89")
    window.mainloop()


def aux_mostrar_preguntas():
    """
    Funcion auxiliar de la funcion Mostrar_preguntas, divide la cantidad de preguntas en sublistas del mismo tamaño
    :return: La cantidad de paginas totales, Una lista con el orden de las pregutnas y una lista con las 
    preguntas sobrantes
    """
    cantidad_total = []

    try:
        for x in range(cantidad_total_preguntas(banco_preguntas(nombre_usuario))):
            cantidad_total.append(x)
        aux = len(cantidad_total) // 3
        aux2 = len(cantidad_total) % 3
        matriz = []
        for x in range(aux):
            sublista = []
            for z in range(1, 4):
                sublista.append((x * 3) + z)
            matriz.append(sublista)
        if aux2 > 0:
            sublista2 = []
            for x in range(1 ,aux2 + 1):
                sublista2.append((3 * aux) + x)
            matriz.append(sublista2)
        return matriz, aux, aux2

    except NameError:
        print("Salida inexperada")


def aux_estadisticas():
    """
    Funcion auxiliar de la funcion mostrar_estadisticas, divide el documento en dos listas donde una de ellas contiene
    las estadisticas
    :return: dos listas donde una de ellas contiene las estadisticas y la otra contiene las preguntas
    """
    parte_inicial = []
    lista = convertir(banco_preguntas(nombre_usuario))
    for x in range(0, 1):
        parte_inicial.append(lista[x])
    parte_final = []
    for x in range(2, len(lista)):
        parte_final.append(lista[x])
    return aux_anadir_preguntas(parte_inicial), aux_anadir_preguntas(parte_final)


def banco_preguntas(nombre_documento):
    """
    Convierte el nombre del usuario en una direccion de archivvo
    :return: La direccion del archivo
    """
    nombre_documento ="../Recursor/"+nombre_documento+".csv"
    return nombre_documento


def cantidad_total_preguntas(documento):
    """
    Calcula la cantidad total de preguntas en el documento
    :param string documento: string que indica el nombre del documento del cual se va
    a calcular la cantidad total de preguntas
    :return: Numero entero
    """
    lista = convertir(banco_preguntas(nombre_usuario))
    lista_numeros = []
    for x in range(2, len(lista)):
        valor = lista[x]
        try:
            valor = int(valor)
        except:
            continue
        if type(valor) == int :
            lista_numeros.append(valor)
    return lista_numeros[-1]


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


def leer_pregunta(documento, numero, contador=0):
    """
    Funcion que lee las preguntas
    :param strin documento: string con el nombre del documento
    :param int numero: Numero que indica el numero de la pregunta a leer
    :param int contador: Indica el numero de pregunta
    :return: None
    """
    num = numero
    lista_aux = convertir(documento)
    pregunta_respuesta = "Pregunta #" + str(contador) + " "
    lista_preguntas = ""
    lista_respuestas = ""
    respuesta_correcta = ""
    for x in range(2, len(lista_aux)):
        if lista_aux[x] == str(numero):
            aux_valor = lista_aux[x][0]
            while aux_valor != "A" and aux_valor != "B" and aux_valor != "C" and aux_valor != "D":
                x = x + 1
                if str(lista_aux[x]) == "A" or str(lista_aux[x]) == "B" or str(lista_aux[x]) == "C" or str(lista_aux[x]) == "D":
                        respuesta_correcta = (lista_aux[x])
                        break
                pregunta_respuesta = pregunta_respuesta + str(lista_aux[x]) + "\n"
    return pregunta_respuesta, respuesta_correcta


def convertir(documento):
    """
    Funcion que convierte el documennto en una lista con sublistas para la funcion leer_pregunta()
    :param String documento: Documento que se va a convertir
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
    f.close()


def aleatoriedad(cantidad_usuario):
    """
    Crea un orden aleatorio de las preguntas almacenadas
    :return:cantidad de preguntas que se van a leer, Lista con el orden de las preguntas aleatorias
    """
    orden_aleatorio = []
    indicador = 1
    while indicador != 0:
        valor_aleatorio = random.randrange(1, (cantidad_total_preguntas(banco_preguntas(nombre_usuario))+1), 1)
        if valor_aleatorio not in orden_aleatorio:
            orden_aleatorio.append(valor_aleatorio)
        if len(orden_aleatorio) == cantidad_total_preguntas(banco_preguntas(nombre_usuario)):
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
    for x in range(1, cantidad_total_preguntas + 1):
        lista_preguntas.append(x)
    return lista_preguntas


def solicitar_datos_pregunta(pregunta,
                             posibles_respuesta_a,
                             posibles_respuesta_b,
                             posibles_respuesta_c,
                             posibles_respuesta_d,
                             respuesta_correcta):
    """
    Solicita datos de la nueva pregunta y los almacena en una lista
    :return: Una lista con los datos de la nueva pregunta
    """


    datos_pregunta_nueva = [[pregunta], ["   A) "+posibles_respuesta_a],
                                        ["   B) "+posibles_respuesta_b],
                                        ["   C) "+posibles_respuesta_c],
                                        ["   D) "+posibles_respuesta_d],
                            [respuesta_correcta]]
    return datos_pregunta_nueva


def hacer_preguntas(cantidad_total_preguntas, datos_pregunta_nueva):
    """
    Añade la nueva pregunta al documento
    :param int cantidad_total_preguntas: Indica la cantidad total de preguntas almacenadas
    :param String: String con los datos de la nueva pregunta
    :return: None
    """
    datos_pregunta = [aux_anadir_preguntas(lista_documento(banco_preguntas(nombre_usuario)))],\
                     [str(cantidad_total_preguntas + 1)],\
                     [aux_anadir_preguntas(datos_pregunta_nueva)]
    with open(banco_preguntas(nombre_usuario), 'w', newline="") as f:
        escribir = csv.writer(f, delimiter=" ", lineterminator="\n")
        escribir.writerows(datos_pregunta)


def reemplazar_parte_inicial_parte_final(posicion_pregunta):
    """
    Da los datos anteriores y posteriores a la pregunta elegida
    :param int posicion:Posicion de la pregunta que va a ser reemplazada
    :return: Lista con los datos anteriores y posteriores a la pregunta elegida
    """
    posicion = posicion_pregunta
    lista_preguntas_totales_string = \
        pasar_lista_a_string(lista_preguntas_totales(cantidad_total_preguntas(banco_preguntas(nombre_usuario))))
    lista_aux = convertir(banco_preguntas(nombre_usuario))
    lista_inicial = []
    lista_final = []
    x = 0
    if cantidad_total_preguntas(banco_preguntas(nombre_usuario)) != 0:
        for x in range(2, len(lista_aux)):
            if lista_aux[x] == str(posicion):
                index_p = lista_aux.index(lista_aux[x])
                for z in range(index_p, len(lista_aux)):
                    if lista_aux[z] == "A" or lista_aux[z] == "B" or lista_aux[z] == "C" or lista_aux[z] == "D":
                        index_f = z
                        break
        for x in range(0, 2):
            lista_inicial.append(str(lista_aux[x]))
        x = 0
        for x in range(2, len(lista_aux)):
            if lista_aux[x] in lista_preguntas_totales_string:
                if lista_aux[x] != str(posicion):
                    while lista_aux[x] != "A" and lista_aux[x] != "B" and lista_aux[x] != "C" and lista_aux[x] != "D":
                        lista_inicial.append(str(lista_aux[x]))
                        x = x + 1
                        if lista_aux[x] == "A" or lista_aux[x] == "B" or lista_aux[x] == "C" or lista_aux[x] == "D":
                            lista_inicial.append(lista_aux[x])
                else:
                    break
        for x in range(index_f + 1, len(lista_aux)):
            lista_final.append(lista_aux[x])


    return lista_inicial, lista_final



def eliminar_pregunta_especifica(posicion):
    """
    Elimina la pregunta elegida por el usuario
    :param int posicion: Numero de la pregunta que se va a eliminar
    :return:
    """
    nuevos_datos = [aux_eliminar_pregunta_especifica(posicion)], []
    with open(banco_preguntas(nombre_usuario), "w", newline="") as f:
        escribir = csv.writer(f, delimiter=" ", lineterminator="\n")
        escribir.writerows(nuevos_datos)


def aux_eliminar_pregunta_especifica(posicion_pregunta):
    """
    Aux de la funcion eliminar_pregunta_especifica, A las siguientes preguntas les cambia el numero haciendo
    que el orden se mantenga
    :param int posicion_pregunta: Numero de la pregunta que el usuario va a eliminar
    :return: Lista sin la pregunta elegida
    """
    posicion = posicion_pregunta
    lista_preguntas_totales_string = \
        pasar_lista_a_string(lista_preguntas_totales(cantidad_total_preguntas(banco_preguntas(nombre_usuario))))
    lista_aux = convertir(banco_preguntas(nombre_usuario))
    lista_final = []
    x = 0
    if cantidad_total_preguntas(banco_preguntas(nombre_usuario)) != 0:

        for x in range(0, 2):
            lista_final.append(str(lista_aux[x]))

        for x in range(2, len(lista_aux)):
            if lista_aux[x] != str(posicion) and lista_aux[x] in lista_preguntas_totales_string:
                while lista_aux[x] != "A" and lista_aux[x] != "B" and lista_aux[x] != "C" and lista_aux[x] != "D":
                    try:
                        if int(lista_aux[x]) > posicion:
                            lista_aux[x] = int(lista_aux[x]) - 1
                    except:
                        lista_aux[x] = lista_aux[x]
                    lista_final.append(str(lista_aux[x]))
                    x = x + 1
                lista_final.append(lista_aux[x])

    return aux_anadir_preguntas(lista_final)


def pasar_lista_a_string(lista_preguntas_totales):
    """
    Convierte a string los valores dentro de la lista de preguntas
    :param list[int] lista_preguntas_totales: Lista con el numero de totas las preguntas del documento
    :return:
    """
    lista_preguntas_totales_string = list(map(str, lista_preguntas_totales))
    return lista_preguntas_totales_string


def main():
    """
    Inicializa el menu
    :return:
    """
    inicia_aplicacion()

main()
