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
    
    def testNumeroUnico(self):
        self.assertEqual(convertirRomano('I'), 1)
        self.assertEqual(convertirRomano('V'), 5)
        self.assertEqual(convertirRomano('X'), 10)
        self.assertEqual(convertirRomano('L'), 50)
        self.assertEqual(convertirRomano('C'), 100)
        self.assertEqual(convertirRomano('D'), 500)
        self.assertEqual(convertirRomano('M'), 1000)
    
    def testSuma(self):
        self.assertEqual(convertirRomano('II'), 2)
        self.assertEqual(convertirRomano('XX'), 20)
        self.assertEqual(convertirRomano('VII'), 7)    
        self.assertEqual(convertirRomano('DCI'), 601)
     
    def testResta(self):
        self.assertEqual(convertirRomano('IV'), 4)
        self.assertEqual(convertirRomano('IX'), 9)
        self.assertEqual(convertirRomano('XL'), 40)
        self.assertEqual(convertirRomano('CM'), 900)
     
    def testMasTresRepeticionesSeguidas(self):
        self.assertRaises(AssertionError,convertirRomano,'IIII')
        self.assertRaises(AssertionError,convertirRomano, 'LXXXX')
        self.assertRaises(AssertionError,convertirRomano, 'MMMMMM')
        self.assertRaises(AssertionError,convertirRomano, 'XVVVIIII')
       
    def testRepeticionesTipo5(self):
        self.assertRaises(AssertionError,convertirRomano, 'VV')
        self.assertRaises(AssertionError,convertirRomano, 'LLL')
        self.assertRaises(AssertionError,convertirRomano, 'DD')
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    
    
    
    
    
    
    
    
    
    