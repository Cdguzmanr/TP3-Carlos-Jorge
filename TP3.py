#######################################################
#Creado por: Carlos Guzmán, Jorge Guevara
#Fecha de creación: 30/05/2022 5:15 pm
#Última modificación: 6/6/2022 4:30 pm 
#Versión de python: 3.10.2
#######################################################

# Importación de Librerias
from http.client import FORBIDDEN
from tkinter import *
import re
import random
import pickle
import names
import datetime

# Definción de Variables Globales
listaPaises = []    # Aquí se almacenará la información de los archivos txt
diccPersonalidades = {}
listaPersonalidades = []
matrizUsuarios = []
#matrizUsuarios = [['2-0840-0626', 'Carlos Guzman', True, '("Arquitecto","INTJ")', 'Afganistán', [True, '', '']],['2-0877-0176', 'KLen Barboza', True, '("Comandante","ENTJ")', 'Afganistán', [True, '', '']] ]

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

def validarNombre(pValidar):
    """
    Funcionamiento: Validar las entradas para el ejercicio
    Entradas: pstringValidar (str) dato con el que se trabaja.
    Salidas: realimentar al usuario con la corrección de posibles errores o emitir el resultado correcto 
    """ #Encontré esta expresión regular para nombres propios en internet
    if re.match("^([a-zA-Zá-úÁ-Ú]{2,}\s[a-zA-zá-úÁ-Ú]{1,}'?-?[a-zA-Zá-úÁ-Ú]{2,}\\s?([a-zA-Zá-úÁ-Ú]{1,})?)", pValidar): 
        return True          
    else:
        return False 

def validarCedulas(pstringValidar):
    """
    Funcionamiento: Validar las entradas para el ejercicio
    Entradas: pstringValidar (str) dato con el que se trabaja.
    Salidas: realimentar al usuario con la corrección de posibles errores o emitir el resultado correcto 
    """
    if re.match("^[1-9]{1}-\d{4}-\d{4}$", pstringValidar):
        return True
    elif re.match("^\D+$", pstringValidar):   
        return False
    elif len(pstringValidar) != 11:   
        return False
    else:
        return False

def graba(nomArchGrabar,lista):
    #Función que graba un archivo con una lista de estudiantes
    try:
        f=open(nomArchGrabar,"wb")
        #print("1.Voy a grabar el archivo: ", nomArchGrabar)
        pickle.dump(lista,f)
        #print("1.Voy a cerrar el archivo: ", nomArchGrabar)
        f.close()
    except:
        print("Error al grabar el archivo: ", nomArchGrabar)
        f.close()

def lee (nomArchLeer):
    #Función que lee un archivo con una lista de estudiantes
    lista=[]
    try:
        f=open(nomArchLeer,"rb")
        #print("2. Voy a leer el archivo: ", nomArchLeer)
        lista = pickle.load(f)
        #print("2. Voy a cerrar el archivo: ", nomArchLeer)
        f.close()
    except:
        print("Error al leer el archivo: ", nomArchLeer)
        f.close()
    return lista

###################################################################################
# Funciones Principales
def generarPersonalidades():
    global listaPersonalidades
    for categoria in diccPersonalidades:
        for titulo in diccPersonalidades[categoria]:
            listaPersonalidades.append((f"{categoria}-{titulo[0]}"))
    return ""

#_________________________________________________________________________________# Boton 1
def cargarBaseDeDatos():
    # try:
    global listaPaises
    global diccPersonalidades
    listaPaises=cargarBDPaises()
    diccPersonalidades=cargarBDPersonalidades()
    generarPersonalidades()
    print(f"\n_____________________________________\nLista de paises generada: \n{listaPaises}")
    print(f"\n_____________________________________\nDiccionario de personalidades generado: \n{diccPersonalidades}")
    print(f"\n_____________________________________\nLista de personalidades generada: \n{listaPersonalidades}")
    
    #crearAviso("Base de datos generada", inicio)
    # except:
    #     crearAviso("Ocurrió un error, vuelva a intentarlo", inicio)
    # return  ""
def cargarBDPaises(): 
    #leerPaises=lee("paises.txt")
    f=open("paises.txt","r", encoding="utf-8")
    listaPais=[]
    listaQuince=[]
    for linea in f.readlines():
        listaPais.append(linea[:-1])
    i=0
    while i <15:
        pais=random.choice(listaPais)
        if pais not in listaQuince:
            listaQuince.append(pais)
            i+=1
    f.close()
    return listaQuince

def cargarBDPersonalidades():
   #personalidadPrincipal=[]
    personalidadSecundaria=[]
    f=open("personalidades.txt","r", encoding="utf-8")
    diccioPersonali={}
    for linea in f.readlines()[::-1]:
        if linea[0]=="-":
            diccioPersonali.update({linea[1:-1]:personalidadSecundaria})
            personalidadSecundaria=[]
        elif linea[0]=="*":
            personalidadSecundaria.append((linea[1:-6],linea[-5:-1]))
    f.close()
    return diccioPersonali
print(cargarBaseDeDatos())
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

    def asignarCedula(self, pcedula):
        """
        Funcionamiento: Asigna la cédula a un usuario
        Entradas: pcedula (str)
        Salidas: Asigna la cédula al atributo "cedula"
        """
        self.cedula= pcedula
        return
    def mostrarCedula(self):
        """
        Funcionamiento: Muestra la cédula a un usuario
        Entradas: self (str)
        Salidas: muestra la cédula del usuario
        """
        return self.cedula 
    def asignarNombre(self, pnombre):
        """
        Funcionamiento: Asigna el nombre a un usuario
        Entradas: pnombre (str)
        Salidas: Asigna el nombre al atributo "nombre"
        """        
        self.nombre= pnombre
        return
    def mostrarNombre(self):
        """
        Funcionamiento: Muestra el nombre a un usuario
        Entradas: self (str)
        Salidas: muestra el nombre del usuario
        """
        return self.nombre        
    def asignarGenero(self, pgenero):
        """
        Funcionamiento: Asigna el genero a un usuario
        Entradas: pgenero (str)
        Salidas: Asigna el genero al atributo "genero"
        """              
        if pgenero == 1:
            self.genero= True
        else:
            self.genero= False            
        return
    def mostrarGenero(self):
        """
        Funcionamiento: Muestra el genero a un usuario
        Entradas: self (str)
        Salidas: muestra el genero del usuario
        """
        return self.genero          
    def asignarPersonalidad(self, ppersonalidad):
        """
        Funcionamiento: Asigna la personalidad a un usuario
        Entradas: ppersonalidad (str)
        Salidas: Asigna la personalidad al atributo "personalidad"
        """                  
        self.personalidad= ppersonalidad
        return
    def mostrarPersonalidad(self):
        """
        Funcionamiento: Muestra la personalidad a un usuario
        Entradas: self (str)
        Salidas: muestra la personalidad del usuario
        """
        return self.personalidad          
    def asignarPais(self, ppais):
        """
        Funcionamiento: Asigna el pais a un usuario
        Entradas: ppais (str)
        Salidas: Asigna el pais al atributo "pais"
        """                 
        self.pais= ppais
        return
    def mostrarPais(self):
        """
        Funcionamiento: Muestra el pais a un usuario
        Entradas: self (str)
        Salidas: muestra el pais del usuario
        """
        return self.pais          
    def asignarEstado(self, pestado):
        """
        Funcionamiento: Asigna el estado a un usuario
        Entradas: pestado (str)
        Salidas: Asigna el estado al atributo "estado"
        """           
        self.estado= pestado
        return          
    def mostrarEstado(self):
        """
        Funcionamiento: Muestra el estado a un usuario
        Entradas: self (str)
        Salidas: muestra el estado del usuario
        """
        return self.estado                                
    def exportarUsuario(self): # Impresión general
        """
        Funcionamiento: Exporta los datos ingresados del usuario en formato de lista
        Entradas: ppais (str)
        Salidas: Lista con los datos del usuario
        """             
        return [self.cedula,self.nombre,self.genero,self.personalidad,self.pais,self.estado]

def ingresarCedula(ventana, cedula):
    if not validarCedulas(cedula):
        crearAviso("Cédula inválida, debe seguir el formato #-####-####", ventana)
        return False   
    elif cedula in [dato[0] for dato in matrizUsuarios]:
        crearAviso("Esta cédula ya se encuentra registrada", ventana)
        return False        
    return True

def ingresarNombre(ventana, nombre):
    if not validarNombre(nombre):
        crearAviso("Nombre inválido", ventana)
        return False      
    return True



def almacernarDatos(ventana, cedula, nombre, genero, personalidad, pais):
    if not ingresarCedula(ventana, cedula):
        return ""      
    elif not validarNombre(nombre):
        crearAviso("Nombre inválido", ventana)
        return ""
    elif genero == 0:
        crearAviso("Debe seleccionar un genero", ventana)
        return ""        
    elif repr(personalidad) == "''":
        crearAviso("Debe seleccionar una personalidad", ventana)
    elif  repr(pais) == "''":
        crearAviso("Debe seleccionar un pais", ventana)    
    else:        
        try:
            usuario=Usuario()
            usuario.asignarCedula(cedula)
            usuario.asignarNombre(nombre)
            usuario.asignarGenero(genero)
            usuario.asignarPersonalidad(personalidad)
            usuario.asignarPais(pais)
            usuario.asignarEstado([True, "", ""])
            matrizUsuarios.append(usuario)
            print(f"\n_________________________________________________________________________________\nUsuarios almacenados: {matrizUsuarios}")
            ventana.destroy()
            crearAviso("Información almacenada con éxito", inicio)
        except:
            crearAviso("Ocurrió un error, vuelva a intentarlo", ventana)
    return
def registroDinamico():
    ParticipanteOpp=Usuario()
    cedula=""
    nombre=""
    genero=False
    estado=[]
    cedula=random.randint(1,9),"-",random.randint(0,9999).zfill(4),"-",random.randint(0,9999).zfill(4)
    nombre=names.get_first_name()," ",names.get_last_name(),"-",names.get_last_name()
    genero=random.randint(0,1)
    if genero==1:
        genero=False
    else:
        genero=True
    estado=[False,"",""]
    ParticipanteOpp.asignarCedula(cedula)
    ParticipanteOpp.asignarNombre(nombre)
    ParticipanteOpp.asignarGenero(genero)
    #ParticipanteOpp.asignarPersonalidad(personalidad)
    #ParticipanteOpp.asignarPais(pais)
    ParticipanteOpp.asignarEstado([True, "", ""])
    matrizUsuarios.append(ParticipanteOpp)





    return


def registrarUsuario(): 
    """
    Interfaz gráfica de la ventana respectiva
    """
    # Check de si cargó BD    
    if not listaPaises or not diccPersonalidades:
        crearAviso('Bases de Datos no cargadas.', inicio)
        return ''        
    ventanaInsertar = Toplevel(inicio)      
    ventanaInsertar.grab_set()
    ventanaInsertar.resizable(False, False)
    ventanaInsertar.title('Registrar un nuevo usuario')
    ventanaInsertar.geometry('550x350')
    ventanaInsertar.configure(bg='white')
    # Encabezado
    encabezadoInsertar = Label(ventanaInsertar, text="Registrar un nuevo usuario", font=("Calibri 20"),bg='white')
    encabezadoInsertar.grid(row=0, column=0, columnspan=2 ,padx=20, pady=5)
    # Entrada de cédula
    cedulaTexto = Label(ventanaInsertar,text="Cédula",font="Calibri 16",bg='white')
    cedulaTexto.grid(row=1,column=0,padx=5,pady=5)                           
    cedulaEntrada = Text(ventanaInsertar,height=1,width=40,bg = 'lightblue') # command=lambda: seleccionarTipo(ventanaInsertar, fechaEntrada, botonAdulto, botonVoluntario)
    cedulaEntrada.grid(row=1,column=1,padx=10,pady=5)
    cedulaEntrada.bind('<FocusOut>', lambda evento: ingresarCedula(ventanaInsertar, cedulaEntrada.get('1.0', 'end-1c')))
    #Nombre Completo
    nombreTexto = Label(ventanaInsertar,text="Nombre completo",font="Calibri 16",bg='white')
    nombreTexto.grid(row=2,column=0,padx=0,pady=5)
    nombreEntrada = Text(ventanaInsertar,height=1,width=40,bg = 'lightblue')
    nombreEntrada.grid(row=2,column=1,padx=0,pady=5)   
    #nombreEntrada.bind('<FocusOut>', lambda evento:ingresarNombre(ventanaInsertar, nombreEntrada.get('1.0', 'end-1c')))
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
    personalidadSelect = OptionMenu(ventanaInsertar,personalidad, *listaPersonalidades)
    personalidadSelect.config(width=50)
    personalidadSelect.grid(row=5,column=1,padx=0,pady=5)

    # Pais
    paisTexto = Label(ventanaInsertar,text="País",font="Calibri 16",bg='white')
    paisTexto.grid(row=6,column=0,padx=5,pady=5)      
    pais = StringVar()
    paisSelect = OptionMenu(ventanaInsertar,pais,*listaPaises)
    paisSelect.config(width=50)
    paisSelect.grid(row=6,column=1,padx=0,pady=10)

    # Botones
    insertar = Button(ventanaInsertar, text="Insertar", width=20, height=2, bg='#ffffbf', command=lambda: almacernarDatos(ventanaInsertar, cedulaEntrada.get('1.0', 'end-1c'), nombreEntrada.get('1.0', 'end-1c'), genero.get(), personalidad.get(), pais.get()))
    limpiar = Button(ventanaInsertar, text="Limpiar", width=20, height=2, bg='#b8daba', command=lambda: refrescarVentana(ventanaInsertar, lambda:registrarUsuario()))
    regresar = Button(ventanaInsertar, text="Regresar", width=20, height=2, bg='#deb1bf', command=lambda: ventanaInsertar.destroy())
    insertar.place(x = 25, y = 300)
    limpiar.place(x = 200, y = 300)
    regresar.place(x = 375, y = 300)   
    return

#_________________________________________________________________________________# Boton 3
def registrarDinamico(participantesGenerados): 
    # Check de si cargó BD    
    if not listaPaises or not diccPersonalidades:
        crearAviso('Bases de Datos no cargadas.', inicio)
        return ''        
    for i in range(participantesGenerados):
        ParticipanteOpp=Usuario()
        cedula=""
        nombre=""
        genero=False
        estado=[]
        cedula=str(random.randint(1,9)),"-",str(random.randint(0,9999)).zfill(4),"-",str(random.randint(0,9999)).zfill(4)
        nombre=names.get_first_name()," ",names.get_last_name(),"-",names.get_last_name()
        genero=random.randint(0,1)
        if genero==1:
            genero=False
        else:
            genero=True
        personalidad=(random.randint(0,3),random.randint(0,3))
        pais=random.randint(0,193)
        ParticipanteOpp.asignarCedula(cedula)
        ParticipanteOpp.asignarNombre(nombre)
        ParticipanteOpp.asignarGenero(genero)
        ParticipanteOpp.asignarPersonalidad(personalidad)
        ParticipanteOpp.asignarPais(pais)
        ParticipanteOpp.asignarEstado([True, "", ""])
        
        print(ParticipanteOpp.exportarUsuario())
        matrizUsuarios.append(ParticipanteOpp)
        
    return

#_________________________________________________________________________________# Boton 4

   

def actualizarDatos(ventana, numeroUsuario, personalidad):
    try:    
        matrizUsuarios[numeroUsuario][3]=personalidad
        ventana.destroy()
        print(f"\n_________________________________________________________________________________\nInformación de usuario actualizada: {matrizUsuarios[numeroUsuario]}")
        crearAviso("Información actualizada", inicio)
    except:
        crearAviso("Ocurrió un error, vuelva a intentarlo", None)       
    return ""

def interfazModificar(numeroUsuario):
    # Setup de ventana
    ventanaModificar = Toplevel(inicio)      
    ventanaModificar.grab_set()
    ventanaModificar.resizable(False, False)
    ventanaModificar.title('Registrar un nuevo usuario')
    ventanaModificar.geometry('550x250')
    ventanaModificar.configure(bg='white')
    # Encabezado
    encabezadoInsertar = Label(ventanaModificar, text="Modificar usuario", font=("Calibri 20"),bg='white')
    encabezadoInsertar.grid(row=0, column=0, columnspan=2 ,padx=20, pady=5)
    # Entrada de cédula
    cedulaTexto = Label(ventanaModificar,text="Cédula",font="Calibri 16",bg='white')
    cedulaTexto.grid(row=1,column=0,padx=5,pady=5)                           
    cedulaEntrada = Text(ventanaModificar,height=1,width=40,bg = 'lightblue') # command=lambda: seleccionarTipo(ventanaModificar, fechaEntrada, botonAdulto, botonVoluntario)
    cedulaEntrada.insert('1.0',matrizUsuarios[numeroUsuario][0])
    cedulaEntrada.config(state=DISABLED)
    cedulaEntrada.grid(row=1,column=1,padx=10,pady=5)
    #Nombre Completo
    nombreTexto = Label(ventanaModificar,text="Nombre completo",font="Calibri 16",bg='white')
    nombreTexto.grid(row=2,column=0,padx=0,pady=5)
    nombreEntrada = Text(ventanaModificar,height=1,width=40,bg = 'lightblue')
    nombreEntrada.insert('1.0',matrizUsuarios[numeroUsuario][1])
    nombreEntrada.config(state=DISABLED)
    nombreEntrada.grid(row=2,column=1,padx=0,pady=5)  
    # Personalidad
    personalidadTexto = Label(ventanaModificar,text="Personalidad",font="Calibri 16",bg='white')
    personalidadTexto.grid(row=5,column=0,padx=5,pady=10)      
    personalidad = StringVar(value=matrizUsuarios[numeroUsuario][3])
    personalidadSelect = OptionMenu(ventanaModificar,personalidad, *listaPersonalidades)
    personalidadSelect.config(width=50)
    personalidadSelect.grid(row=5,column=1,padx=0,pady=5)
    # Botones
    insertar = Button(ventanaModificar, text="Insertar", width=20, height=2, bg='#ffffbf', command=lambda: actualizarDatos(ventanaModificar,numeroUsuario,personalidad.get())) # actualizarDatos(ventana, numeroUsuario, personalidad)
    limpiar = Button(ventanaModificar, text="Limpiar", width=20, height=2, bg='#b8daba', command=lambda: refrescarVentana(ventanaModificar, lambda:interfazModificar(numeroUsuario)))
    regresar = Button(ventanaModificar, text="Regresar", width=20, height=2, bg='#deb1bf', command=lambda: ventanaModificar.destroy())
    insertar.place(x = 25, y = 200)
    limpiar.place(x = 200, y = 200)
    regresar.place(x = 375, y = 200)   
    return

def puenteModificar(ventana, cedula):
    """ Valida el avance hacia la ventana de moficar la personalidad del usuario """
    if not validarCedulas(cedula):
        print(f"\nDatos de ingreso: '{cedula}'")
        crearAviso("Cédula inválida, debe seguir el formato #-####-####", ventana)
        return "" 
    elif cedula not in [dato[0] for dato in matrizUsuarios]:
        crearAviso("Esta cédula no se encuentra registrada", ventana)
        return ""
    else:  
        contador = 0
        while contador<len(matrizUsuarios):
            if matrizUsuarios[contador][0]==cedula:
                ventana.destroy()
                interfazModificar(contador)                
                return ""
            contador+=1
    return ""     

def modificarUsuario(): 
    # Check de si cargó BD    
    if not listaPaises or not diccPersonalidades:
        crearAviso('Bases de Datos no cargadas.', inicio)
        return ''        
    ventanaModificar = Toplevel(inicio)      
    ventanaModificar.grab_set()
    ventanaModificar.resizable(False, False)
    ventanaModificar.title('Solicitar cedular')
    ventanaModificar.geometry('550x150')
    ventanaModificar.configure(bg='white')   
    # Encabezado
    encabezadoModificar = Label(ventanaModificar, text="Modificar usuario", font=("Calibri 20"),bg='white').place(x=180, y=10)
    # Cuadro de texto
    textoModificar = Label(ventanaModificar, text="Ingrese el número de cédula a modificar:", font=("Calibri 12"),bg='white').place(x=25, y=60)
    entradaModificar = Text(ventanaModificar,height=1,width=20,bg = 'lightblue')
    entradaModificar.place(x=315, y=64) 
    entradaModificar.bind('<Return>', lambda evento: puenteModificar(ventanaModificar, entradaModificar.get('1.0', 'end-1c')))
    entradaModificar.bind('<FocusOut>', lambda evento: entradaModificar.delete('1.0', END))
    # Botones
    insertar = Button(ventanaModificar, text="Continuar", width=20, height=2, bg='#ffffbf', command=lambda: puenteModificar(ventanaModificar, entradaModificar.get('1.0', 'end-1c')))
    limpiar = Button(ventanaModificar, text="Limpiar", width=20, height=2, bg='#b8daba', command=lambda: refrescarVentana(ventanaModificar, lambda:modificarUsuario()))
    regresar = Button(ventanaModificar, text="Regresar", width=20, height=2, bg='#deb1bf', command=lambda: ventanaModificar.destroy())
    insertar.place(x = 25, y = 100)
    limpiar.place(x = 200, y = 100)
    regresar.place(x = 375, y = 100) 
    return

#_________________________________________________________________________________# Boton 5
def eliminarUsuario(): 
    # Check de si cargó BD    
    if not listaPaises or not diccPersonalidades:
        crearAviso('Bases de Datos no cargadas.', inicio)
        return ''        
    return
def eliminarUsuarios(cedula,justificar):
    eliminar=""
    for participante in matrizUsuarios:
        if participante.mostrarCedula()==cedula:
            eliminar=input("¿Desea eliminar sus datos?")
            if eliminar=="si":
                participante.asignarEstado([False,justificar,datetime.datetime.now()])
                print("Su estado ha sido modificado.")
            else:
                print("El estado no se ha modificado.")
    return
print(eliminarUsuarios())     
#_________________________________________________________________________________# Boton 6
def exportarXML(): 
    # Check de si cargó BD    
    if not listaPaises or not diccPersonalidades:
        crearAviso('Bases de Datos no cargadas.', inicio)
        return ''        
    return

#_________________________________________________________________________________# Boton 7
def reportes(): 
    # Check de si cargó BD    
    if not listaPaises or not diccPersonalidades:
        crearAviso('Bases de Datos no cargadas.', inicio)
        return ''        
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
boton1 = Button(inicio, text="Cargar Bases de Datos", width=65, height=3, bg="#ffffbf", command=cargarBaseDeDatos)
boton2 = Button(inicio, text="Registrar usuario nuevo", width=65, height=3, bg='#ffffbf', command=registrarUsuario)
boton3 = Button(inicio, text="Registro dinámico", width=65, height=3, bg='#c5e2f6', command=lambda:registrarDinamico(5))
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




