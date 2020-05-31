import socket, os


class enlaceDatos:

    def Convertir_A_String(self,bits):
        auxBits = bits
        auxBitsSin = auxBits[:len(auxBits) - 16]
        return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(auxBitsSin)]*8))

    def validacionTrama(self, bits):
        print("CAPA DE ENLACE DE DATOS")
        print(bits + "   BIIIIIIIIIIIIIITS")
        valorAux = int(bits, 2)
        print(valorAux)
        if valorAux%65521 == 0: 
            print("MENSAJE RECIBIDO CORRECTAMENTE")
        else:
            print("INCORRECTO POR FAVOR VUELVA A ENVIAR EL MENSAJE")