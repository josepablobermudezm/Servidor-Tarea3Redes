import socket, os
from .enlaceDatos import enlaceDatos

class transporte:

    def __init__(self, nombre):
        self.nombre = nombre

    def recibirMensaje(self,c):
        mensaje = c.recv(1024)
        print("Mensaje Recibido: "+ mensaje.decode('utf8') +" en la capa de Transporte")

        mensajeConvertidoAString = enlaceDatos.Convertir_A_String(mensaje.decode('utf8'))
        #llama a la capa de Enlace de Datos que convierte el mensaje de bits a String
        print("Mensaje convertido de bits a String en capa de Enlace de Datos " + mensajeConvertidoAString )
        return mensajeConvertidoAString