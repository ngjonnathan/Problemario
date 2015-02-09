'''
Created on 8/2/2015

@author: Jonnathan
'''
def convertirRomano(numero):
    romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    entero, i = 0, 0
    tam = len(numero)
    ocurr = 1
    while i < tam:      # Recorrer palabra
        valorActual = romanos[numero[i]]
        if (i < tam-1):
            sig  = romanos[numero[i+1]]
            if (valorActual < sig):
                assert(valorActual*10 >= sig)
                assert(sig - valorActual != valorActual)
                entero +=  sig - valorActual 
                i+= 2    # Saltar hasta 2 caracteres por la resta
                continue
            elif (valorActual == sig):
                assert(valorActual+sig not in(romanos.values()))
                ocurr += 1
            else:
                ocurr = 1
                
        entero += valorActual
        i += 1
        assert(ocurr < 4)
        
    return entero










if __name__ == '__main__':
    pass