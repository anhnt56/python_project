'''py'''
import unittest
from translator import englishtofrench, frenchtoenglish, englishtogerman

class TestEnglishToFrench(unittest.TestCase):
    """ This is where you test english translate to french """
    def test1(self):
        """ This is the 1st test """
        self.assertEqual(englishtofrench("Hello"),"Bonjour")
        self.assertEqual(englishtofrench("Welcome"),"Bienvenue")
        self.assertEqual(englishtofrench("Love"),"Amour")
        #self.assertEqual(englishtofrench(""),"error")
    def test2(self):
        """ This is the 2nd test """
        self.assertNotEqual(englishtofrench("A"),"Bonjour")
        #self.assertEqual(englishtofrench(""),"error")    

class TestFrenchToEnglish(unittest.TestCase):
    """ This is where you test french translate to english """
    def test1(self):
        """ This is the 1st test """
        self.assertEqual(frenchtoenglish("Bonjour"),"Hello")
        self.assertEqual(frenchtoenglish("Bienvenue"),"Welcome")
        self.assertEqual(frenchtoenglish("Amour"),"Love")
        #self.assertEqual(englishtofrench(""),"error")
    def test2(self):
        """ This is the 2nd test """
        self.assertNotEqual(frenchtoenglish("A"),"Hello")    

class TestEnglishToGerman(unittest.TestCase):
    """This is where you test english translate to german"""
    def test3(self):
        """ This is the 1st test """
        self.assertEqual(englishtogerman("Hello"),"Hallo")
        self.assertEqual(englishtogerman("Welcome"),"Begrüßung")
        self.assertEqual(englishtogerman("Love"),"Liebe")

unittest.main()
