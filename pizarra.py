###     NO BORRAR      ###
from tkinter import *
import random

# def cargarPaises(): # Opción 1
#     nuevoDicc = {}
#     try:
#         archivo = open('paises.txt', 'r')
#     except:
#         return False # Si no encuentra el archivo, regresa False.
#     try:
#         for linea in archivo:
#             linea = linea.strip() # quita los reglones extra de la línea.
#             listaLinea = linea.split(': ')
#             listaLinea[1] = listaLinea[1].split(', ')
#             nuevoDicc[listaLinea[0]] = listaLinea[1]
#     except:
#         archivo.close()
#         return False # Si el archivo está en un formato incorrecto, también regresa False.
#     archivo.close()
#     return nuevoDicc

# def cargarBD(): 
#     print("\nCargar bases de datos")
#     if cargarPaises():
#         global diccPaises
#         diccPaises = cargarPaises() # Definido en funciones.py
#         crearAviso('Base de datos creada satisfactoriamente', inicio)
#     else:
#         crearAviso('Base de datos inexistente o con formato incorrecto.', inicio)    
#     return

print(help(OptionMenu))


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
        if pais not in listaPais:
            listaQuince.append(pais)
            i+=1
    f.close()
    return listaQuince

