import unittest 
from Voiture import Voiture
from voiturier import Voiturier

class TestVoiture(unittest.TestCase):
    def test_init(self):
        v = Voiturier(1242)
        self.assertEqual(v.numvoiturirer, 1242)