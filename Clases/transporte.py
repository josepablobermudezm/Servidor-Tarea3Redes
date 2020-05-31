import socket, os
from .enlaceDatos import enlaceDatos

class transporte:

    def __init__(self, nombre):
        self.nombre = nombre

    def recibirMensaje(self,c):
        mensaje = c.recv(1024)
        cantTramas = int(mensaje.decode('utf8'))
        print(str(cantTramas) + " cantidad de tramas")
        cont = 0
        bitsPalabra=""
        while cont < cantTramas:
            mensaje = c.recv(1024)
            if(mensaje != ""):
                print("MEEEENSAJE" + mensaje.decode('utf8'))
                print(mensaje.decode('utf8') + "   mensaje = c.recv   ")
                print("Trama Recibida: "+ mensaje.decode('utf8') +" en la capa de Transporte\n")
                trama = enlaceDatos.Convertir_A_String(None,mensaje.decode('utf8'))
                print("Trama codificada: "+ trama)
                enlaceDatos.validacionTrama(None, mensaje.decode('utf8'))
                bitsPalabra+=trama
                print(bitsPalabra + " BitsPALABRA")
            cont+=1
        return bitsPalabra