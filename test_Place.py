import unittest
from Place import Place 

class TestPlace(unittest.TestCase):
    def test_place(self):
        place = Place(26,2,122,2.3,True)
        self.assertEqual(place.num, 26)
        self.assertEqual(place.niveau, 2)
        self.assertEqual(place.longeur, 122)
        self.assertEqual(place.hauteur, 2.3)
        self.assertEqual(place.estlibre, True)
        