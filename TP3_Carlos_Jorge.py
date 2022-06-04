#######################################################
#Creado por: Carlos Guzmán, Jorge Guevara
#Fecha de creación: 30/05/2022 5:15 pm
#Última modificación: 3/6/2022 4:50 pm 
#Versión de python: 3.10.2
#######################################################

# Importación de Librerias
from tkinter import *
from turtle import width

# Definción de Variables Globales
listaPaises = [""]    # Aquí se almacenará la información de los archivos txt
diccPersonalidades = {}

###################################################################################
# Definición de funciones

    #Funnciones Generales
def refrescarVentana(ventana, comando):
    """
    Funcionamiento: Permite refrescar una ventana
    Entrada: ventana (ventana a cerrar), comando (función a llamar)
    """
    ventana.destroy()
    comando()

def crearAviso(msg, ventanaPrincipal):
    """
    Funcionamiento: Permite crear una ventana de aviso
    Entrada: msg (mensaje de aviso), ventanaPrincipal (Ventana donde se devuelve al usuario)   
    """
    ventanaAviso = Toplevel(ventanaPrincipal)
    ventanaAviso.grab_set()
    ventanaAviso.title('Aviso')
    ventanaAviso.geometry('500x100')
    ventanaAviso.configure(bg='white')
    ventanaAviso.resizable(False, False)
    encabezadoAviso = Label(ventanaAviso, text=msg, font=("Calibri 12"),bg='white')
    encabezadoAviso.pack()
    botonSalir = Button(ventanaAviso, text="Entendido", width=40, height=3, bg='lightblue', command= lambda:ventanaAviso.destroy())
    botonSalir.pack()


###################################################################################
# Funciones Principales

#_________________________________________________________________________________# Boton 1
def cargarBD(): 
    print("\nCargar bases de datos") 
    return

#_________________________________________________________________________________# Boton 2
class Usuario:
    """ Definición de atributos """
    cedula=""
    nombre=""
    genero=True
    personalidad=0
    pais=""
    estado=[]
    """ Definición de atributos """
    def __init__(self):
        self.cedula=""
        self.nombre=""
        self.genero=True
        self.personalidad=0
        self.pais=""
        self.estado=[]



def registrarUsuario(): 
    """
    Interfaz gráfica de la ventana respectiva
    """
    print("\nRegistrar nuevo usuario")
    # Check de si cargó BD
    # if not listaPaises or not diccPersonalidades:
    #     return crearAviso('Debe cargar las bases de datos', inicio)
    # Setup de ventana
    ventanaInsertar = Toplevel(inicio)
    ventanaInsertar.grab_set()
    ventanaInsertar.resizable(False, False)
    ventanaInsertar.title('Registrar un nuevo usuario')
    ventanaInsertar.geometry('550x350')
    ventanaInsertar.configure(bg='white')
    # Encabezado
    encabezadoInsertar = Label(ventanaInsertar, text="Registrar un nuevo usuario", font=("Calibri 20"),bg='white')
    encabezadoInsertar.grid(row=0, column=0, columnspan=2 ,padx=20, pady=5)
    cedulaTexto = Label(ventanaInsertar,text="Cédula  ",font="Calibri 16",bg='white')
    # Entrada de cédula
    cedulaTexto = Label(ventanaInsertar,text="Cédula",font="Calibri 16",bg='white')
    cedulaTexto.grid(row=1,column=0,padx=5,pady=5)                           
    cedulaEntrada = Text(ventanaInsertar,height=1,width=40,bg = 'lightblue') # command=lambda: seleccionarTipo(ventanaInsertar, fechaEntrada, botonAdulto, botonVoluntario)
    cedulaEntrada.grid(row=1,column=1,padx=10,pady=5)
    #Nombre Completo
    nombreTexto = Label(ventanaInsertar,text="Nombre completo",font="Calibri 16",bg='white')
    nombreTexto.grid(row=2,column=0,padx=0,pady=5)
    nombreEntrada = Text(ventanaInsertar,height=1,width=40,bg = 'lightblue')
    nombreEntrada.grid(row=2,column=1,padx=0,pady=5)   
    
    # Genero
    generoTexto = Label(ventanaInsertar,text="Género",font="Calibri 16",bg='white')
    generoTexto.grid(row=3,column=0, padx=0,pady=5)
    # Botones de Masculino / Femenino
    genero = IntVar()
    botonMasculino = Radiobutton(ventanaInsertar,text="Masculino",variable=genero, value=1, bg="white") # state = disabled
    botonFemenino = Radiobutton(ventanaInsertar,text='Femenino',variable=genero, value=2, bg="white")
    botonMasculino.place(x=200, y=145)
    botonFemenino.place(x=350, y=145)  
    
    # Personalidad
    personalidadTexto = Label(ventanaInsertar,text="Personalidad",font="Calibri 16",bg='white')
    personalidadTexto.grid(row=5,column=0,padx=5,pady=10)      
    personalidad = StringVar()
    personalidadSelect = OptionMenu(ventanaInsertar,personalidad, diccPersonalidades)
    personalidadSelect.config(width=50)
    personalidadSelect.grid(row=5,column=1,padx=0,pady=5)
    
    # Pais
    paisTexto = Label(ventanaInsertar,text="País",font="Calibri 16",bg='white')
    paisTexto.grid(row=6,column=0,padx=5,pady=5)      
    pais = StringVar()
    paisSelect = OptionMenu(ventanaInsertar,pais,*listaPaises)
    paisSelect.config(width=50)
    paisSelect.grid(row=6,column=1,padx=0,pady=10)
    insertar = Button(ventanaInsertar, text="Insertar", width=20, height=2, bg='#ffffbf') # , command=lambda: insertarDatos(ventanaInsertar, fechaEntrada, tipoEntrada, codigo, nombreEntrada, hobbyUno, hobbyDos, hobbyTres, profesion, correo, pais, descripcionEntrada)
    limpiar = Button(ventanaInsertar, text="Limpiar", width=20, height=2, bg='#b8daba', command=lambda: refrescarVentana(ventanaInsertar, lambda:registrarUsuario()))
    regresar = Button(ventanaInsertar, text="Regresar", width=20, height=2, bg='#deb1bf', command=lambda: ventanaInsertar.destroy())
    insertar.place(x = 25, y = 300)
    limpiar.place(x = 200, y = 300)
    regresar.place(x = 375, y = 300)   

    # # Ajustar Cambios - Radio Button
    # fechaEntrada.bind('<FocusOut>', lambda evento: seleccionarTipo(fechaEntrada, botonAdulto, botonVoluntario, codigo))
    # # Id de participante
    # codigoTexto = Label(ventanaInsertar,text="Identificador de participante",font="Calibri 16",bg='white')
    # codigoTexto.grid(row=4,column=0,padx=0,pady=5)
    # codigo.grid(row=4,column=1,padx=0,pady=5)
    # #Nombre Completo
    # nombreTexto = Label(ventanaInsertar,text="Nombre completo",font="Calibri 16",bg='white')
    # nombreTexto.grid(row=5,column=0,padx=0,pady=5)
    # nombreEntrada = Text(ventanaInsertar,height=1,width=40,bg = 'lightblue')
    # nombreEntrada.grid(row=5,column=1,padx=0,pady=5)
    # correo = Label(ventanaInsertar,text="",font="Calibri 16",bg='white')
    # nombreEntrada.bind('<Key>', lambda evento: actualizarCorreo(correo, nombreEntrada, matrizVoluntarios))
    # # Hobbies
    # hobbiesTexto = Label(ventanaInsertar,text="Hobbies",font="Calibri 16",bg='white')
    # hobbiesTexto.grid(row=6,column=0,padx=0,pady=5)
    # hobbyUno = StringVar()
    # hobbyUnoSelect = OptionMenu(ventanaInsertar,hobbyUno,*hobbiesLista)
    # hobbyUnoSelect.grid(row=6,column=1,padx=0,pady=5)
    # hobbyDos = StringVar()
    # hobbyDosSelect = OptionMenu(ventanaInsertar,hobbyDos,*hobbiesLista)
    # hobbyDosSelect.grid(row=7,column=1,padx=0,pady=5)
    # hobbyTres = StringVar()
    # hobbyTresSelect = OptionMenu(ventanaInsertar,hobbyTres,*hobbiesLista)
    # hobbyTresSelect.grid(row=8,column=1,padx=0,pady=5)
    # # Profesión
    # profesionTexto = Label(ventanaInsertar,text="Profesión u oficio",font="Calibri 16",bg='white')
    # profesionTexto.grid(row=9,column=0,padx=0,pady=5)
    # profesion = Label(ventanaInsertar,text=str(profesionRandom()),font="Calibri 16",bg='white')
    # profesion.grid(row=9,column=1,padx=0,pady=5)
    # # Correo electrónico
    # correoTexto = Label(ventanaInsertar,text="Correo electrónico",font="Calibri 16",bg='white')
    # correoTexto.grid(row=10,column=0,padx=0,pady=5)
    # correo.grid(row=10,column=1,padx=0,pady=5)
    # # País de Origen
    # paisTexto = Label(ventanaInsertar,text="País de Origen",font="Calibri 16",bg='white')
    # paisTexto.grid(row=11,column=0,padx=0,pady=5)
    # pais = Label(ventanaInsertar,text=str(conseguirPais(diccPaises, True)),font="Calibri 16",bg='white')
    # pais.grid(row=11,column=1,padx=0,pady=5)
    # # Estado
    # estadoTexto = Label(ventanaInsertar,text="Estado",font="Calibri 16",bg='white')
    # estadoTexto.grid(row=12,column=0,padx=0,pady=5)
    # estado = Label(ventanaInsertar,text="Activo",font="Calibri 16",bg='white')
    # estado.grid(row=12,column=1,padx=0,pady=5)
    # # Descripción
    # descripcionTexto = Label(ventanaInsertar,text="Descripción",font="Calibri 16",bg='white')
    # descripcionTexto.grid(row=13,column=0,padx=0,pady=5)
    # descripcionEntrada = Text(ventanaInsertar,height=2,width=40,bg = 'lightblue')
    # descripcionEntrada.grid(row=13,column=1,padx=0,pady=5)
    # # Botones
    # insertar = Button(ventanaInsertar, text="Insertar", width=25, height=2, bg='lightblue', command=lambda: insertarDatos(ventanaInsertar, fechaEntrada, tipoEntrada, codigo, nombreEntrada, hobbyUno, hobbyDos, hobbyTres, profesion, correo, pais, descripcionEntrada))
    # limpiar = Button(ventanaInsertar, text="Limpiar", width=25, height=2, bg='lightblue', command=lambda: refrescarInsertar(ventanaInsertar, lambda:insertarParticipante()))
    # regresar = Button(ventanaInsertar, text="Regresar", width=25, height=2, bg='lightblue', command=lambda: ventanaInsertar.destroy())
    # insertar.place(x = 10, y = 620)
    # limpiar.place(x = 205, y = 620)
    # regresar.place(x = 400, y = 620)    

    return

#_________________________________________________________________________________# Boton 3
def registrarDinamico(): 
    print("\nRegistro dinámico")
    return

#_________________________________________________________________________________# Boton 4
def modificarUsuario(): 
    print("\nModificar información de usuario")
    return

#_________________________________________________________________________________# Boton 5
def eliminarUsuario(): 
    print("\nEliminar usuario")
    return

#_________________________________________________________________________________# Boton 6
def exportarXML(): 
    print("\nExportar XML")
    return

#_________________________________________________________________________________# Boton 7
def reportes(): 
    print("\nGenerar Reportes")
    return


###################################################################################
# Interfaz gráfica
inicio = Tk()
inicio.geometry("500x600")
inicio.resizable(False, False)
inicio.title("Equipo de trabajo MBTI")
inicio.config(bg="white")
# Encabezado
titulo = Label(inicio, text="Equipo de trabajo MBTI", font=("Calibri 20"),bg='white')
titulo.grid(row=0, column=0, padx=80, pady=10)
# Botones
boton1 = Button(inicio, text="Cargar Bases de Datos", width=65, height=3, bg="#ffffbf", command=cargarBD)
boton2 = Button(inicio, text="Registrar usuario nuevo", width=65, height=3, bg='#ffffbf', command=registrarUsuario)
boton3 = Button(inicio, text="Registro dinámico", width=65, height=3, bg='#c5e2f6', command=registrarDinamico)
boton4 = Button(inicio, text="Modificar datos de usuario", width=65, height=3, bg='#c5e2f6', command=modificarUsuario)
boton5 = Button(inicio, text="Eliminar usuario", width=65, height=3, bg='#b8daba', command=eliminarUsuario)
boton6 = Button(inicio, text="Exportar XML", width=65, height=3, bg='#b8daba', command=exportarXML) 
boton7 = Button(inicio, text="Reportes", width=65, height=3, bg='#deb1bf', command=reportes)
boton8 = Button(inicio, text="Salir", width=65, height=3, bg='#deb1bf', command=inicio.destroy) # "inicio.destroy" Permite cerrar la inicio
# Edición de los botones                                    # #ffffbf   #c5e2f6    #b8daba  #deb1bf
boton1.grid(row=1, column=0, padx=20, pady=5)
boton2.grid(row=2, column=0, padx=20, pady=5)
boton3.grid(row=3, column=0, padx=20, pady=5)
boton4.grid(row=4, column=0, padx=20, pady=5)
boton5.grid(row=5, column=0, padx=20, pady=5)
boton6.grid(row=6, column=0, padx=20, pady=5)
boton7.grid(row=7, column=0, padx=20, pady=5)
boton8.grid(row=8, column=0, padx=20, pady=5)

# Programa principal (PP)
mainloop()





