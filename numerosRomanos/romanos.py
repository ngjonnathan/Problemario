'''
Created on 8/2/2015

@author: Jonnathan
'''
def convertirRomano(numero):
    romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    entero, i = 0, 0
    tam = len(numero)
    while i < tam:
        if (i < tam-1) and (romanos[numero[i]] < romanos[numero[i+1]]):
            entero +=  romanos[numero[i+1]] - romanos[numero[i]] 
            i+= 2
        else:
            entero += romanos[numero[i]]
            i+=1
            
    return entero













if __name__ == '__main__':
    pass