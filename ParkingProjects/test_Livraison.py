import unittest
from Livraison import Livraison
from Services import Services
from voiturier import Voiturier

class TestLivraison(unittest.TestCase):
    def setUp(self):
        livraison = Livraison()
        self.assertIsNone(livraison)