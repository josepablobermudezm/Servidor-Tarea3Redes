import socket, os


class enlaceDatos:

    def Convertir_A_String(self,bits):
        return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(bits)]*8))
