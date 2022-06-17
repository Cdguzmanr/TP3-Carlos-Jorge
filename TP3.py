#######################################################
#Creado por: Carlos Guzmán, Jorge Guevara
#Fecha de creación: 30/05/2022 5:15 pm
#Última modificación: 16/6/2022 12:00 pm 
#Versión de python: 3.10.2
#######################################################

# Importación de Librerias
from logging import root
from tkinter import *
import re
import random
import pickle
import names
import xml.etree.cElementTree as ET
from http.client import FORBIDDEN
import datetime
import dominate
from dominate.tags import*

# Definción de Variables Globales
listaPaises = []    # Aquí se almacenará la información de los archivos txt
diccPersonalidades = {}
listaPersonalidades = []
matrizUsuarios = []
descripcionPersonalidad = []
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

def validarNombre(nombre):
  return re.match('^[A-ZÀ-Ú]{1}[a-zà-ú]{1,}$', nombre)
def validarNombreCompleto(cadenaNombres):
  listaNombres = cadenaNombres.split()
  if not (len(listaNombres) == 3  or len(listaNombres) == 4):
    return False
  for nombre in listaNombres:
    if not validarNombre(nombre):
      return False
  return True

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

#_________________________________________________________________________________# Boton 1
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
        else:
            descripcionPersonalidad.append(linea[:-1])            
    f.close()        
    return diccioPersonali

def generarPersonalidades():
    global listaPersonalidades
    for categoria in diccPersonalidades:
        for titulo in diccPersonalidades[categoria]:
            listaPersonalidades.append((f"{categoria}-{titulo[0]}"))
    return ""

def cargarBaseDeDatos():
    try:
        global listaPaises
        if listaPaises:
            crearAviso("Las bases de datos ya han sido generadas", None)
            return           
        global diccPersonalidades
        listaPaises=cargarBDPaises()
        diccPersonalidades=cargarBDPersonalidades()
        generarPersonalidades()
        print(f"\n_____________________________________\nLista de paises generada: \n{listaPaises}")
        print(f"\n_____________________________________\nDiccionario de personalidades generado: \n{diccPersonalidades}")
        print(f"\n_____________________________________\nLista de personalidades generada: \n{listaPersonalidades}")
        print(f"\n_____________________________________\nDescripción de las personalidades: \n{descripcionPersonalidad}")
        crearAviso("Base de datos generada", inicio)
    except:
        crearAviso("Ocurrió un error, vuelva a intentarlo", inicio)
    return  ""    


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

def buscarCedula(cedula):
    if cedula in [dato.mostrarCedula() for dato in matrizUsuarios]:
        return True    
    return False

def ingresarCedula(ventana, cedula):
    if not validarCedulas(cedula):
        crearAviso("Cédula inválida, debe seguir el formato #-####-####", ventana)
        return False   
    elif buscarCedula(cedula):
        crearAviso("Esta cédula ya se encuentra registrada", ventana)
        return False        
    return True

def ingresarNombre(ventana, nombre):
    if not validarNombreCompleto(nombre):
        crearAviso("Nombre inválido", ventana)
        return False      
    return True

def ingresarPersonalidad(personalidad):
    conjunto = personalidad.split("-")
    contador = 0
    for categoria in diccPersonalidades:
        if categoria == conjunto[0]:
            contador2=0
            for tipo in diccPersonalidades[categoria]:
                if tipo[0] == conjunto[1]:
                    return (contador, contador2)
                contador2+=1
        contador+=1
    return ""        

def almacernarDatos(ventana, cedula, nombre, genero, personalidad, pais):
    if not ingresarCedula(ventana, cedula):
        return ""      
    elif not validarNombreCompleto(nombre):
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
            #npersonalidad=ingresarPersonalidad(personalidad)
            usuario=Usuario()
            usuario.asignarCedula(cedula)
            usuario.asignarNombre(nombre)
            usuario.asignarGenero(genero)
            usuario.asignarPersonalidad(ingresarPersonalidad(personalidad))
            usuario.asignarPais(listaPaises.index(pais))
            usuario.asignarEstado([True, "", ""])
            matrizUsuarios.append(usuario)
            print(f"\n_________________________________________________________________________________\nUsuarios almacenados: {matrizUsuarios}")
            ventana.destroy()
            crearAviso("Información almacenada con éxito", inicio)
        except:
            crearAviso("Ocurrió un error, vuelva a intentarlo", ventana)
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
def insertarDinamico(participantesGenerados, ventanaRegistroDinamico): 
    # Check de si cargó BD    
    if re.search('\D', participantesGenerados):
        crearAviso('Entrada debe ser numérica.', None)
        return ''
    elif int(participantesGenerados) < 25:
        crearAviso('Entrada debe ser mayor a 25.', None)
        return ''        
    elif int(participantesGenerados) > 99:
        crearAviso('Debe ingresar un valor menor a 99.', None)
        return ''
    print("\n\n_____________________________________\nLista de usuarios actualizada:")            
    try:     
        for i in range(int(participantesGenerados)):
            ParticipanteOpp=Usuario()
            cedula=""
            nombre=""
            genero=False
            estado=[True, "", ""]
            cedula=str(random.randint(1,9))+"-"+str(random.randint(0,9999)).zfill(4)+"-"+str(random.randint(0,9999)).zfill(4)
            nombre=names.get_first_name()+" "+names.get_last_name()+" "+names.get_last_name()
            genero=random.randint(0,1)
            if genero==1:
                genero=False
            else:
                genero=True
            personalidad=(random.randint(0,3),random.randint(0,3))
            pais=random.randint(0,15)
            ParticipanteOpp.asignarCedula(cedula)
            ParticipanteOpp.asignarNombre(nombre)
            ParticipanteOpp.asignarGenero(genero)
            ParticipanteOpp.asignarPersonalidad(personalidad)
            ParticipanteOpp.asignarPais(pais)
            ParticipanteOpp.asignarEstado(estado)
            matrizUsuarios.append(ParticipanteOpp)
        print(matrizUsuarios)            
        print(f"\nEjemplo del formato almacenado: \n{random.choice(matrizUsuarios).exportarUsuario()}")
        ventanaRegistroDinamico.destroy()
        crearAviso(f"Se han registrado {participantesGenerados} usuarios con éxito", inicio)
    except:
        crearAviso("Ocurrió un error, vuelva a intentarlo", None)            
    return

def registrarDinamico(): 
    # Check de si cargó BD    
    if not listaPaises or not diccPersonalidades:
        crearAviso('Bases de Datos no cargadas.', inicio)
        return ''        
    # Setup de ventana
    ventanaRegistroDinamico = Toplevel(inicio)
    ventanaRegistroDinamico.grab_set()
    ventanaRegistroDinamico.title('Registro Dinámico')
    ventanaRegistroDinamico.geometry('400x150')
    ventanaRegistroDinamico.resizable(False, False)    
    ventanaRegistroDinamico.configure(bg='white')
    encabezado = Label(ventanaRegistroDinamico, text='Ingrese cantidad a generar', font="Calibri 16",bg='white')
    encabezado.pack()
    entradaCantidad = Text(ventanaRegistroDinamico,height=1,width=40,bg = '#c5e2f6')
    entradaCantidad.pack()
    botonInsertar = Button(ventanaRegistroDinamico, text="Insertar", width=40, height=1, bg='#ffffbf', command=lambda: insertarDinamico(entradaCantidad.get('1.0', 'end-1c'), ventanaRegistroDinamico))
    botonInsertar.pack()
    botonLimpiar = Button(ventanaRegistroDinamico, text="Limpiar", width=40, height=1, bg='#b8daba', command=lambda: refrescarVentana(ventanaRegistroDinamico, lambda: registrarDinamico()))
    botonLimpiar.pack()
    botonRegresar = Button(ventanaRegistroDinamico, text='Regresar', width=40, height=1, bg='#deb1bf', command=lambda: ventanaRegistroDinamico.destroy())
    botonRegresar.pack()
    entradaCantidad.bind('<Return>', lambda evento:insertarDinamico(entradaCantidad.get('1.0', 'end-1c'), ventanaRegistroDinamico))     
    entradaCantidad.bind('<FocusOut>', lambda evento: entradaCantidad.delete('1.0', END))
    return

#_________________________________________________________________________________# Boton 4
def actualizarDatos(ventana, numeroUsuario, personalidad, personalidadMostrada):
    try:    
        global matrizUsuarios
        if personalidadMostrada==personalidad:
            crearAviso("Debe seleccionar una personalidad diferente", None)   
            return
        else:       
            print(f"\n_________________________________________________________________________________\nInformación de usuario actualizada: {matrizUsuarios[numeroUsuario].mostrarCedula()}\nAnterior personalidad: {matrizUsuarios[numeroUsuario].mostrarPersonalidad()} | {personalidadMostrada}")            
            matrizUsuarios[numeroUsuario].asignarPersonalidad(ingresarPersonalidad(personalidad))
            ventana.destroy()
            print(f"Nueva personalidad: {matrizUsuarios[numeroUsuario].mostrarPersonalidad()} | {personalidad}")
            crearAviso("Información actualizada", inicio)
    except:
        crearAviso("Ocurrió un error, vuelva a intentarlo", None)       
    return ""

def personalidadAnterior(numeroUsuario):
    personalidadBase = matrizUsuarios[numeroUsuario].mostrarPersonalidad()
    contador = 0
    for i in diccPersonalidades:
        if contador == personalidadBase[0]:
            #print(f"{i}-{diccPersonalidades[i][personalidadBase[1]][0]}")
            contador+=1        
    return f"{i}-{diccPersonalidades[i][personalidadBase[1]][0]}"

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
    cedulaEntrada.insert('1.0',matrizUsuarios[numeroUsuario].mostrarCedula())
    cedulaEntrada.config(state=DISABLED)
    cedulaEntrada.grid(row=1,column=1,padx=10,pady=5)
    #Nombre Completo
    nombreTexto = Label(ventanaModificar,text="Nombre completo",font="Calibri 16",bg='white')
    nombreTexto.grid(row=2,column=0,padx=0,pady=5)
    nombreEntrada = Text(ventanaModificar,height=1,width=40,bg = 'lightblue')
    nombreEntrada.insert('1.0',matrizUsuarios[numeroUsuario].mostrarNombre())
    nombreEntrada.config(state=DISABLED)
    nombreEntrada.grid(row=2,column=1,padx=0,pady=5)  
    # Personalidad
    personalidadTexto = Label(ventanaModificar,text="Personalidad",font="Calibri 16",bg='white')
    personalidadTexto.grid(row=5,column=0,padx=5,pady=10)      
    personalidadMostrada = personalidadAnterior(numeroUsuario)
    personalidad = StringVar(value=personalidadMostrada)    
    personalidadSelect = OptionMenu(ventanaModificar,personalidad, *listaPersonalidades)
    personalidadSelect.config(width=50)
    personalidadSelect.grid(row=5,column=1,padx=0,pady=5)
    # Botones
    insertar = Button(ventanaModificar, text="Insertar", width=20, height=2, bg='#ffffbf', command=lambda: actualizarDatos(ventanaModificar,numeroUsuario,personalidad.get(), personalidadMostrada)) # actualizarDatos(ventana, numeroUsuario, personalidad)
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
    for persona in range(len(matrizUsuarios)):
        if matrizUsuarios[persona].mostrarCedula()==cedula:
            ventana.destroy()
            print(f"\n_________________________________________________________________________________\nUsuario consultado: {matrizUsuarios[persona].exportarUsuario()}")                        
            interfazModificar(persona)                
            return ""
    crearAviso("Esta cédula no se encuentra registrada", ventana)
    return ""     

def modificarUsuario(): 
    # Check de si cargó BD    
    if not listaPaises or not diccPersonalidades:
        crearAviso('Bases de Datos no cargadas.', inicio)
        return ''        
    elif not matrizUsuarios:
        crearAviso('Debe almacenar al menos 1 usuario.', inicio)
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
def momentoEliminado():
    tiempoActual = datetime.datetime.now()
    return f"{tiempoActual.day}/{tiempoActual.month}/{tiempoActual.year}"

def eliminarUsuarios(cedula,justificar):
    global matrizUsuarios
    for participante in matrizUsuarios:
        if participante.mostrarCedula()==cedula:
            participante.asignarEstado([False,justificar,momentoEliminado()])
            print(f"\n_________________________________________________________________________________\nSe ha cambiado el estado del usuario a 'inactivo': \n{participante.exportarUsuario()}")                        
            return ""
    return ""
def insertarRazonBaja(cedula):
    # Setup de ventana
    ventanaRazon = Toplevel(inicio)
    ventanaRazon.grab_set()
    ventanaRazon.title('Presentar razón de baja')
    ventanaRazon.geometry('400x150')
    ventanaRazon.resizable(False, False) 
    ventanaRazon.configure(bg='white')
    encabezado = Label(ventanaRazon, text='Presente la razón de baja.', font="Calibri 12",bg='white')
    encabezado.pack()
    razonEntrada =  Text(ventanaRazon,height=2,width=40,bg = 'lightblue')
    razonEntrada.pack()
    botonConfirmar = Button(ventanaRazon, text="Ok", width=40, height=1, bg='aliceblue', command=lambda: eliminarUsuarios(cedula, razonEntrada.get('1.0', 'end-1c')) or crearAviso('Participante desactivado exitosamente.', inicio) or ventanaRazon.destroy())
    botonConfirmar.pack()
    razonEntrada.bind('<Return>', lambda evento:eliminarUsuarios(cedula, razonEntrada.get('1.0', 'end-1c')) or crearAviso('Participante desactivado exitosamente.', inicio) or ventanaRazon.destroy())
    return ''

def confirmarBaja(cedula):
    # Setup de ventana
    ventanaConfirmar = Toplevel(inicio)
    ventanaConfirmar.grab_set()
    ventanaConfirmar.title('Confirmar elección')
    ventanaConfirmar.geometry('400x150')
    ventanaConfirmar.resizable(False, False) 
    ventanaConfirmar.configure(bg='white')
    encabezado = Label(ventanaConfirmar, text='¿Estás seguro?', font="Calibri 12",bg='white')
    encabezado.pack()
    botonAceptar = Button(ventanaConfirmar, text="Aceptar", width=40, height=1, bg='#b8daba', command=lambda:insertarRazonBaja(cedula) or ventanaConfirmar.destroy())
    botonAceptar.pack()
    botonRegresar = Button(ventanaConfirmar, text='Regresar', width=40, height=1, bg='#deb1bf', command=lambda: crearAviso('No se eliminó el participante.', inicio) or ventanaConfirmar.destroy())
    botonRegresar.pack()

def intentarBajar(cedula, ventana):
    if not validarCedulas(cedula):
        crearAviso("Cédula inválida, debe seguir el formato #-####-####", None)
        return ""  
    elif not buscarCedula(cedula):
        crearAviso('Ese participante no existe.', None)
        return ''
    confirmarBaja(cedula)
    ventana.destroy()
    return ''    

def eliminarUsuario(): 
    # Check de si cargó BD    
    if not listaPaises or not diccPersonalidades:
        crearAviso('Bases de Datos no cargadas.', inicio)
        return '' 
    # Setup de ventana
    ventanaEliminar = Toplevel(inicio)
    ventanaEliminar.grab_set()
    ventanaEliminar.title('Eliminar Usuario')
    ventanaEliminar.geometry('400x150')
    ventanaEliminar.resizable(False, False) 
    ventanaEliminar.configure(bg='white')
    encabezado = Label(ventanaEliminar, text='Numero de cédula', font="Calibri 12",bg='white')
    entradaCedula = Text(ventanaEliminar,height=1,width=40,bg = 'lightblue')
    encabezado.pack()
    entradaCedula.pack()
    botonBaja = Button(ventanaEliminar, text="Continuar", width=40, height=1, bg='#ffffbf', command=lambda: intentarBajar(entradaCedula.get('1.0', 'end-1c'), ventanaEliminar))
    botonBaja.pack()
    botonLimpiar = Button(ventanaEliminar, text="Limpiar", width=40, height=1, bg='#b8daba', command=lambda: refrescarVentana(ventanaEliminar, lambda: eliminarUsuario()))
    botonLimpiar.pack()
    botonRegresar = Button(ventanaEliminar, text='Regresar', width=40, height=1, bg='#deb1bf', command=lambda: ventanaEliminar.destroy())
    botonRegresar.pack()
    entradaCedula.bind('<Return>', lambda evento: intentarBajar(entradaCedula.get('1.0', 'end-1c'), ventanaEliminar) )               
    return

#_________________________________________________________________________________# Boton 6
def exportarXML(): 
    # Check de si cargó BD    
    if not listaPaises or not diccPersonalidades:
        crearAviso('Bases de Datos no cargadas.', inicio)
        return ''    
    root = ET.Element("personalidades")
    for columna in diccPersonalidades:
        tipo = ET.SubElement(root, "", tipo=f"{columna}") # tipo="Analista"
        contador = 1
        ET.SubElement(tipo, "descripción").text=f"{descripcionPersonalidad[contador-1]}"        
        for linea in diccPersonalidades[columna]:
            ET.SubElement(tipo, f"subtipo{contador}").text=f"{linea[0]}"
            ET.SubElement(tipo, f"codigo{contador}").text=f"{linea[1]}"
            contador+=1            
    archivo = ET.ElementTree(root)
    archivo.write("archivo.xml", encoding="utf-8")
    crearAviso('Archivo XML exportado con éxito', None)
    return

#_________________________________________________________________________________# Boton 7
def reportes(): 
    # Check de si cargó BD    
    #if not listaPaises or not diccPersonalidades:
        #crearAviso('Bases de Datos no cargadas.', inicio)
    tiempoActual = datetime.datetime.now()
    tiempoActual = f"{tiempoActual.day}-{tiempoActual.month}-{tiempoActual.year}-{tiempoActual.hour}-{tiempoActual.minute}-{tiempoActual.second}"       
    nombreArchivo = f'Reportes-{tiempoActual}.html'
    archivo = open(nombreArchivo, "w", encoding="utf-8")
    diccPersonalidades=cargarBDPersonalidades()
    llavesDicc=list(diccPersonalidades.keys())
    print(llavesDicc)
    doc= dominate.document(title="Reportes")
    with doc.head:
        link(rel="stylesheet", href="style.css")
        script(type="text/javascript",src="script.js")
    with doc.body:
        with header(id="Tipo"):
            h1(llavesDicc[0])
            for tipo in diccPersonalidades[llavesDicc[0]]:
                p(tipo)
            h1(llavesDicc[1])
            for tipo in diccPersonalidades[llavesDicc[1]]:
                p(tipo)
            h1(llavesDicc[2])
            for tipo in diccPersonalidades[llavesDicc[2]]:
                p(tipo)
            h1(llavesDicc[3])
            for tipo in diccPersonalidades[llavesDicc[3]]:
                p(tipo)

    archivo.write(str(doc))    
    crearAviso("Se generó el reporte con éxito", None)              
    return 







#     ventanaReportes = Toplevel(inicio)
#     ventanaReportes.grab_set()
#     ventanaReportes.title('Menú de reportes')
#     ventanaReportes.geometry('400x450')
#     ventanaReportes.resizable(False, False) 
#     ventanaReportes.configure(bg='white')
#     encabezado = Label(ventanaReportes, text='Reportes', font="Calibri 16",bg='white')
#     encabezado.pack()
#     boton1=Button(ventanaReportes, text="Personalidades", width=50, height=3, bg='#ffffbf').place(x=20, y=40)
#     boton2=Button(ventanaReportes, text="Tipos de Personalidad", width=50, height=3, bg='#ffffbf').place(x=20, y=105) # 65 +
#     boton3=Button(ventanaReportes, text="Información de Usuario", width=50, height=3, bg='#c5e2f6').place(x=20, y=170)
#     boton4=Button(ventanaReportes, text="Mostrar Base de Datos", width=50, height=3, bg='#c5e2f6').place(x=20, y=235)
#     boton5=Button(ventanaReportes, text="Usuarios Retirados", width=50, height=3, bg='#b8daba').place(x=20, y=235)
#     boton6=Button(ventanaReportes, text="Paises", width=50, height=3, bg='#b8daba').place(x=20, y=300)
#     boton7=Button(ventanaReportes, text="Regresar", width=50, height=3, bg='#deb1bf', command=ventanaReportes.destroy).place(x=20, y=365)    
#     return
print(reportes())


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
boton3 = Button(inicio, text="Registro dinámico", width=65, height=3, bg='#c5e2f6', command=registrarDinamico)
boton4 = Button(inicio, text="Modificar datos de usuario", width=65, height=3, bg='#c5e2f6', command=modificarUsuario)
boton5 = Button(inicio, text="Eliminar usuario", width=65, height=3, bg='#b8daba', command=eliminarUsuario)
boton6 = Button(inicio, text="Exportar XML", width=65, height=3, bg='#b8daba', command=exportarXML) 
boton7 = Button(inicio, text="Reportes", width=65, height=3, bg='#deb1bf', command=reportes)
boton8 = Button(inicio, text="Salir", width=65, height=3, bg='#deb1bf', command=inicio.destroy) # "inicio.destroy" Permite cerrar la inicio
# Edición de los botones                                  
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

right