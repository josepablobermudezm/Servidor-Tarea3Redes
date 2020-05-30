import msvcrt
import os
from .presentacion import presentacion

class aplicacion:

    
    def __init__(self, c):
        self.c = c

    def mostrarMensaje(self, Mensaje):
        
        print("El mensaje decodificado es:" + Mensaje)