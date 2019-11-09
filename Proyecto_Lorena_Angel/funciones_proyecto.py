# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 09:46:43 2019

@author: eduar
"""
from tkinter import *
#///////////////////////////////////////////


""" 
def preionado(mensaje):
    
    
    try:
       
        int(mensaje)
        
        messagebox.showinfo(message = str(mensaje))
        
        valor = 2254
        
        return valor
        
    except ValueError:
        messagebox.showerror(message = "El valor ingresado es erróneo")
            
 
    

def validar(valor):
    messagebox.showinfo(message = str(valor))
    print(valor)
    
"""
     

def leerArduino(dato):
    try:
        import serial, time  #importar biblioteca, time, control de tiempos
        
        arduino= serial.Serial('COM3', 9600) #Indicar comunicacion serial
        
        time.sleep(4)  # microsegundos
        #     messagebox.showerror(message=entrada1.get())
        #     entrada1.delete(0,len(entrada1.get()))
        
        dato = int(dato)
        lista = []
        for i in range(dato):
            lista.append(arduino.readline()) #agregar a lista los valores de arduino
        #    print(lista)
        
        arduino.close() # importante cerrar comunicacion COM 
        
    
        return lista
        
    except FileNotFoundError:
        messagebox.showerror(message = "No se ha establecido la conexión.")
    except ValueError:
        messagebox.showerror(message = "Se ha ingresado un valor erróneo.")
        
   
def guardar(nombreArchivo, lista):
    
    if nombreArchivo == '' or lista == '':
        
        messagebox.showwarning(message = "Aún no ha leído los datos o no ha ingresado el nombre del archivo")
    
        
    else:
        
        caracterInvalido = 0
        
        for i in range(len(nombreArchivo)):
            caracter = nombreArchivo[i]
            
            if caracter == '/' or caracter == ':' or caracter == '*' or caracter == '?' or caracter == '"' or caracter == '<' or caracter == '>' or caracter == '|':
                caracterInvalido += 1
        
        if caracterInvalido == 0:
            
            nombreArchivo = nombreArchivo + '.txt'
            archivo= open(nombreArchivo, 'a')
            archivo.close()
            archivo= open(nombreArchivo, 'w')
            print (lista) 
            informacion = str(lista) + '\n'
            #lista = ['']
            archivo.write(informacion)
            archivo.close()
            messagebox.showinfo(message = "Se ha guardado correctamente")
        else:
            messagebox.showwarning(message = "El nombre del archivo no puede contener caracteres especiales")

#//////////////////////////////////////////////////



