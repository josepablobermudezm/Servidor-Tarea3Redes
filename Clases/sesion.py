import socket, os
from .transporte import transporte
from .presentacion import presentacion
class sesion:

    def __init__(self, nombre):
        self.nombre = nombre

    def iniciarServidor(self,host, puerto):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host,puerto))
        s.listen(5) #hasta 5 repeticiones
        while True:
            # establecer conexión
            (c, addr) = s.accept()
            print("Se estableció conexión con: %s " % str(addr))
            msg = transporte.recibirMensaje(None, c)#llama a la capa de transporte y retorna el mensaje después de recibir el mensaje
            presentacion.desencriptar(None,msg)#desencriptamos el mensaje
            c.close()
