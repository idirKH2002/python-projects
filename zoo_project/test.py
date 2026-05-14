from wolf import Wolf 
from home import Home
from parot import Parot  # on importe les classes depuis leurs fichier
from snack import Snack 
from sheep import Sheep
from zoo import Zoo
import unittest 
import pydoc

class ZooTest(unittest.TestCase):
    def setUp(self):
        self.loup = Wolf("noir")
        self.mouton = Sheep("blanc")
        self.perroquet = Parot("vert")
        self.serpent = Snack("noir")
    
            
    def test_initialliser(self):
        self.assertEqual(self.loup.c,"noir")
        self.assertEqual(self.perroquet.n,2)
    def test_animal_by_color(self):
        maison1 = Home("Maison_Blanche")
        maison2 = Home("Green_House")
        maison1.add_animal(self.loup,self.perroquet)
        maison2.add_animal(self.mouton,self.serpent)
        z = Zoo(maison1,maison2)

        self.assertEqual(z.animals_by_color("noir"),['loup','sérpent'])
        
        

if __name__ == '__main__':
    unittest.main()
pydoc.writedoc('test')