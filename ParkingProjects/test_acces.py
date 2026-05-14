import unittest 
from acces import Acces 
from Client import Client
from Parking import Parking 

class TestAcces(unittest.TestCase):
    def setUp(self):
        acces1 = Acces(1)
        acces2 = Acces(2)
        self.assertEqual(acces1.num,1)
        self.assertEqual(acces2.num,1)
    
    def test_accionnerCamera(self,client):
        client1 = Client("idir","toulouse",False,False,True)
        self.assertEqual(client1.name,"idir")
        self.assertEqual(client1.addresse,"toulouse")
        self.assertFalse(client1.abonne)
        self.assertFalse(client1.Superabonne)
        self.assertTrue(client1.abonnement)
    def test_acctionerpanneau(self):
        p1 = Parking(5,10,4,11)
        a1 = p1.Acces.acctionerpanneau()
        self.assertEqual(a1,"11")
    def test_lancerprocedureentre(self):
        client1 = Client("idir","toulouse",False,False,True)
        entree=Acces.lancerprocedureentre(client1)
        self.assertEqual(entree,"Mode de paiement (carte bancaire, espèces).")
        
        