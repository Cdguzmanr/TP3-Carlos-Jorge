#######################################################
#Creado por: Carlos Guzmán, Jorge Guevara
#Fecha de creación: 30/05/2022 5:15 pm
#Última modificación: 30/05/2022 00:00 pm 
#Versión de python: 3.10.2
#######################################################
from tkinter import *

# Definición de funciones
    # Cargar países


#_________________________________________________________________________________# 
# Interfaz gráfica
ventana = Tk()
ventana.geometry("600x700")
ventana.title("PAMTEC")
ventana.configure(bg='white')

# Encabezado
titulo = Label(ventana, text="Adoptemos un adulto mayor", font=("Calibri 20"),bg='white')
titulo.grid(row=0, column=0, padx=80, pady=10)
# Botones
boton1 = Button(ventana, text="Cargar BD de países", width=65, height=3, bg='lightblue')
boton2 = Button(ventana, text="Insertar un participante", width=65, height=3, bg='lightblue')
boton3 = Button(ventana, text="Insertar n participantes", width=65, height=3, bg='lightblue')
boton4 = Button(ventana, text="Enlazar con abuelos", width=65, height=3, bg='lightblue')
boton5 = Button(ventana, text="Dar de baja", width=65, height=3, bg='lightblue')
boton6 = Button(ventana, text="Escribe una carta a su correo", width=65, height=3, bg='lightblue')
boton7 = Button(ventana, text="Reportes", width=65, height=3, bg='lightblue')
boton8 = Button(ventana, text="Salir", width=65, height=3, bg='lightblue', command=ventana.destroy) # "ventana.destroy" Permite cerrar la ventana
# Edición de los botones
boton1.grid(row=1, column=0, padx=20, pady=5)
boton2.grid(row=2, column=0, padx=20, pady=5)
boton3.grid(row=3, column=0, padx=20, pady=5)
boton4.grid(row=4, column=0, padx=20, pady=5)
boton5.grid(row=5, column=0, padx=20, pady=5)
boton6.grid(row=6, column=0, padx=20, pady=5)
boton7.grid(row=7, column=0, padx=20, pady=5)
boton8.grid(row=8, column=0, padx=20, pady=5)

# Programa principal
mainloop()





