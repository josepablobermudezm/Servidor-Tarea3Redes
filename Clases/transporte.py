import socket, os
from .enlaceDatos import enlaceDatos

class transporte:

    def __init__(self, nombre):
        self.nombre = nombre

    def recibirMensaje(self,c):
        mensaje = c.recv(1024)
        cantTramas = int(mensaje)
        cont=0
        bits=""
        while cont<cantTramas:
            mensaje = c.recv(1024)
            print("Trama Recibida: "+ mensaje.decode('utf8') +" en la capa de Transporte")
            trama = enlaceDatos.Convertir_A_String(None,mensaje.decode('utf8')) 
            print("Trama codificada: "+trama)
            bits+=trama
            #llama a la capa de Enlace de Datos que convierte el mensaje de bits a String
        return bits