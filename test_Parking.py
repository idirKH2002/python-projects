import unittest 
from Place import Place 
from Parking import Parking

class TestParking(unittest.TestCase):
    def setUp(self):
        parking = Parking(100,12,11,222)
        self.assertEqual(parking.nbPlaceParNiveau,100)
        self.assertEqual(parking.prix,12)
        self.assertEqual(parking.nbniveau,11)
        self.assertEqual(parking.nbplacelibre,222)
        
        
            