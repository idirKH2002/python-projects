import unittest 
from Abonnement import Abonnement

class TestAbonnement(unittest.TestCase):
    def test_initialisation(self):
        ab = Abonnement("livraison",10,True)
        self.assertEqual(ab.libellé,"livraison")
        self.assertEqual(ab.prix,10)
        self.assertTrue(ab.estPackGar)
        