'''
Created on 8/2/2015

@author: Jonnathan
'''
import unittest
from romanos import convertirRomano

class Test(unittest.TestCase):

    def testRomanoExiste(self):
        numero = convertirRomano('I')
    
    def testNumeroUno(self):
        numero = convertirRomano('I')
        self.assertEqual(numero, 1)
    
    def testNumeroCinco(self):
        numero = convertirRomano('V')
        self.assertEqual(numero, 5)
           
    def testNumeroDiez(self):
        numero = convertirRomano('X')
        self.assertEqual(numero, 10)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()