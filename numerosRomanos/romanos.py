'''
Created on 8/2/2015

@author: Jonnathan
'''
def convertirRomano(numero):
    romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    entero, i = 0, 0
    tam = len(numero)
    ocurr = 1
    while i < tam:
        if (i < tam-1): # Apuntador no se encuentra en la ultima posicion
            actual = romanos[numero[i]]
            sig    = romanos[numero[i+1]]
            if (actual < sig):
                entero +=  sig - actual 
                i+= 1   # Saltar el siguiente caracter
            elif (sig == actual):
                entero += actual
                ocurr += 1
            else:
                entero += actual
                ocurr = 1
        else:  # Apuntador se encuentra en ultima posicion
            entero += romanos[numero[i]]
        
        i += 1  # Pasar al siguiente caracter
        assert(ocurr < 4)        
    return entero













if __name__ == '__main__':
    pass