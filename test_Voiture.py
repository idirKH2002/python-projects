import unittest
from Voiture import Voiture

class TestVoiture(unittest.TestCase):
    def test_init(self):
        voiture = Voiture(1.6,2.3,"DZ006DZ",False)
        self.assertEqual(voiture.hauteur, 1.6)
        self.assertEqual(voiture.longeur, 2.3)
        self.assertEqual(voiture.immatriculation, "DZ006DZ")
        self.assertEqual(voiture.estDansParking, False)
