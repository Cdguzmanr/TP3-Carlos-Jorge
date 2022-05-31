#######################################################
#Creado por: Carlos Guzmán, Jorge Guevara
#Fecha de creación: 30/05/2022 5:15 pm
#Última modificación: 31/05/2022 4:50 pm 
#Versión de python: 3.10.2
#######################################################

# Importación de Librerias
from tkinter import *

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
def registrarUsuario(): 
    print("\nRegistrar nuevo usuario")
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
boton1 = Button(inicio, text="Cargar Bases de Datos", width=65, height=3, bg="#deb1bf", command=cargarBD)
boton2 = Button(inicio, text="Registrar usuario nuevo", width=65, height=3, bg='#deb1bf', command=registrarUsuario)
boton3 = Button(inicio, text="Registro dinámico", width=65, height=3, bg='#b8daba', command=registrarDinamico)
boton4 = Button(inicio, text="Modificar datos de usuario", width=65, height=3, bg='#b8daba', command=modificarUsuario)
boton5 = Button(inicio, text="Eliminar usuario", width=65, height=3, bg='#c5e2f6', command=eliminarUsuario)
boton6 = Button(inicio, text="Exportar XML", width=65, height=3, bg='#c5e2f6', command=exportarXML) 
boton7 = Button(inicio, text="Reportes", width=65, height=3, bg='#ffffbf', command=reportes)
boton8 = Button(inicio, text="Salir", width=65, height=3, bg='#ffffbf', command=inicio.destroy) # "inicio.destroy" Permite cerrar la inicio
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





