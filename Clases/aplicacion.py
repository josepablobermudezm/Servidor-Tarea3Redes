import msvcrt
import os

class aplicacion:

    
    def __init__(self, c):
        self.c = c

    def mostrarMensaje(self, Mensaje):
        print("El mensaje es: " + Mensaje + " mostrado en la capa de Aplicacion")
        print("--------------------------------------------------------------------------")