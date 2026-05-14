from wolf import Wolf 
from home import Home
from parot import Parot  # on importe les classes depuis leurs fichier
from snack import Snack 
from sheep import Sheep
from zoo import Zoo
import pydoc
def main():  
    loup = Wolf("noir")
    mouton = Sheep("blanc")
    perroquet = Parot("vert")
    serpent = Snack("noir")
    loup.Afficher()
    mouton.Afficher()
    perroquet.Afficher()
    serpent.Afficher()
    
    maison1 = Home("Maison_Blanche")
    maison2 = Home("Green_House")
    
    maison1.add_animal(loup,perroquet)
    maison2.add_animal(mouton,serpent)
    
    maison1.Afficher()
    maison2.Afficher()
    
    z = Zoo(maison1,maison2)

    l=z.animals_by_color("noir")
    print(f"listes de animaux qui ont le meme nombres de pattes {l}")
    
    z.animals_by_leps(4)
    z.total_legs()  
    
if __name__ == '__main__':
    main()
pydoc.writedoc('main')
    