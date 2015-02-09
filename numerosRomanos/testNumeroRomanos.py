'''
Created on 8/2/2015

@author: Jonnathan
'''
import unittest
from romanos import convertirRomano

class Test(unittest.TestCase):

    def testRomanoExiste(self):
        numero = convertirRomano('I')
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()