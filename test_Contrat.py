import unittest 
from Contrat import Contrat 

class TestContrat(unittest.TestCase):
    def test_contrat(self):
        contrat = Contrat(01/01/2024,31/12/2025,12,True)
        self.assertIsNotNone(contrat)
        self.assertEqual(contrat.date_debut,01/01/2024)
        self.assertEqual(contrat.date_fin,31/12/2025)
        self.assertEqual(contrat.duree,12)
        self.assertTrue(contrat.actif)
        
        