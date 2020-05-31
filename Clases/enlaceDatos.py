import socket, os


class enlaceDatos:

    def __init__(self, nombre):
        self.nombre = nombre

    def Convertir_A_String(bits):
        chars = []
        for b in range(len(bits) / 8):
            byte = bits[b*8:(b+1)*8]
            chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))    
        return ''.join(chars)
            
