import unittest 
from Services import Services

class TestServices(unittest.TestCase):
    def setUp(self):
        service = Services(12/12/2024,14/12/2024,"livraison de voiture")
        self.assertEqual(service.dateDemande,12/12/2024)
        self.assertEqual(service.dateServices,14/12/2024)
        self.assertEqual(service.rapport,"livraison de voiture")
        