import socket, os
class transporte:

    def __init__(self, nombre):
        self.nombre = nombre

    def recibirMensaje(self,c):
        
        mensaje = c.recv(1024)
        print("Mensaje Recibido: "+ mensaje.decode('utf8'))

        return mensaje.decode('utf8')
