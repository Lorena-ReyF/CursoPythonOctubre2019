# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 09:46:43 2019

@author: eduar
"""

from tkinter import *  #* importar todas las instrucciones aunque no las utilice
import serial, time
from funciones_proyecto import *

#//////////////////////////////////////////////////

botonPresionado = False

lista=[]

root= Tk()

root.title("Comunicación con Arduino")
root.geometry("300x150")

try:
    frame = Frame(root)
    frame.pack(side=TOP) #Donde se va a colocar con respecto al siguiente elemento
    
    etiqueta1 = Label(frame, text='Numero de datos')
    etiqueta1.pack(side=TOP)
    
    textoEntrada1 = StringVar()
    #entrada1 = Entry(frame)
    entrada1 = Entry(frame, textvariable = textoEntrada1)
    entrada1.pack(side=TOP)
    
    valorBoton1 = StringVar()
    
    #boton1 = Button(frame, text= 'Leer datos', command = lambda: preionado(textoEntrada1.get()))
    #boton1 = Button(frame, text = 'Leer Datos', command = lambda: valorBoton1.set(preionado(textoEntrada1.get())))
    boton1 = Button(frame, text = 'Leer datos', command = lambda: valorBoton1.set(leerArduino(textoEntrada1.get())))
#    boton1 = Botton(frame, text = 'Leer Datos')
#    valor = boton1.bind('<Button-1>', preionado(textoEntrada1.get()))
    boton1.pack(side=TOP)
    
    
    etiqueta2 = Label(frame, text='Archivo')
    etiqueta2.pack(side=TOP)
    
   
    textoEntrada2 = StringVar()
    
    entrada2 = Entry(frame, textvariable = textoEntrada2)
    entrada2.pack(side=TOP)
    
    #boton2 = Button(frame, text= 'Guardar', command= botonPresionado)
    boton2 = Button(frame, text= 'Guardar', command = lambda: guardar(textoEntrada2.get(),valorBoton1.get()))
    #boton2.bind('<Button-1>', guardar(nombreArchivo))
    boton2.pack(side=TOP)
    
    
#    boton3 = Button(frame, text= 'Mostrar')
#    boton3.pack(side=TOP)
    
    
    
except:
    messagebox.showerror(message = "Ha ocurrido un error.")

#********************************************************************
root.mainloop() # Un loop para mantener visible la ventana


