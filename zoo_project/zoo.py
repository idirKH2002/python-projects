#zoo.py est utilisé comme le main .
#on creé d'abord la classe zoo 
import pydoc
class Zoo :
    def __init__(self,*homes): #contien un nombre variable de maisons
        self.homes=homes
    def animals_by_color(self,couleur):
        l=[]
        for home in self.homes :  #parcourir les maison passés en parametre stockés par defaut dans des tuples
            for animal in home.animaux :  #parcourir les animaux de la liste d'animaux de chaque maison
                if animal.c== couleur :  #si la couleur de l'animal = la couleur passés en param on ajoute le nom , nb_pattes a la liste (juste pour faciliter l'affichage) 
                    l.append(animal.e)
        return  l
    def animals_by_leps(self,n):
        l=[]
        for home in self.homes :
            for animal in home.animaux :
                if animal.n== n :
                    l.append((animal.e,animal.c))
        return  l 
    
    
    def total_legs(self): #calculer le nombre total des pattes
        total = 0
        for home in self.homes :
            for animal in home.animaux:
                total += animal.n
        return print(f"le nombre total des pattes dans le zoo est : {total}")
pydoc.writedoc('zoo')