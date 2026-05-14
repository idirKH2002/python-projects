import unittest 
import Voiture
import Abonnement 
from Client import Client

class TestClient(unittest.TestCase):
    def setUp(self):
        client = Client("CLIENT","BRUXELLES",True,True,True)
        c1  = Client("riad","paris",True,True,True)
        self.assertEqual(c1.name,"riad")
        self.assertEqual(c1.addresse,"paris")
        self.assertTrue(c1.abonne)
        self.assertTrue(c1.Superabonne)
        self.assertTrue(c1.abonnement)
    def test_sAbonner(self):
        c1 = Client("riad","paris",True,True,True)
        self.assertTrue(c1.abonne)
    def test_nouvelleVoiture(self):
        self.client.nouvelleVoiture(immatriculation="ABC123", hauteur=2.0, longeur=4.0)
        self.assertEqual(self.client.voiture.immatriculation, "ABC123")
        self.assertEqual(self.client.voiture.hauteur, 2.0)
        self.assertEqual(self.client.voiture.longeur, 4.0)

    def test_seDesabonner(self):
        self.c1.abonne = True
        self.c1.sedésabonner()
        self.assertFalse(self.c1.abonne)
    def test_demandeMaintenance_superabonne(self):
        self.client.Superabonne = True
        self.client.demandeMaintenance()
        self.assertTrue(self.client.Superabonne)

    def test_demandeMaintenance_abonne(self):
        self.client.abonne = True
        self.client.demandeMaintenance()
        self.assertTrue(self.client.abonne)

    def test_demandeMaintenance_non_abonne(self):
        self.client.demandeMaintenance()
        self.assertFalse(self.client.abonne)
        self.assertFalse(self.client.Superabonne)

    def test_demanderlivraison_superabonne(self):
        self.client.Superabonne = True
        self.client.demanderlivraison("universite toulouse 2 Jean Jaures", "23/12/2024", "12:00")
        self.assertTrue(self.client.Superabonne)

    def test_demanderlivraison_abonne(self):
        self.client.abonne = True
        self.client.demanderlivraison("5 All. Antonio Machado, 31100 Toulouse", "01/01/2025", "00:00")
        self.assertTrue(self.client.abonne)

    def test_demanderlivraison_non_abonne(self):
        self.client.demanderlivraison("5 All. Antonio Machado", "23/12/2024", "10:00")
        self.assertFalse(self.client.abonne)
        self.assertFalse(self.client.Superabonne)

    def test_demanderEntretien_superabonne(self):
        self.client.Superabonne = True
        self.client.demanderEntretien()
        self.assertTrue(self.client.Superabonne)

    def test_demanderEntretien_abonne(self):
        self.client.abonne = True
        self.client.demanderEntretien()
        self.assertTrue(self.client.abonne)

    def test_demanderEntretien_non_abonne(self):
        self.client.demanderEntretien()
        self.assertFalse(self.client.abonne)
        self.assertFalse(self.client.Superabonne)