#creation de la classe Home

class Home :
    def __init__(self,nom): 
        self.nom = nom
        self.animaux = [] #chaque maison a un nombre d'animaux stocké dans des listes . la on initialise une liste vide 
    def add_animal(self,*animals): #fct pour ajouter les animaux a la liste , elle prend un nombre variable de parametre
        for animal in animals : #on parcoure les animaux passés en parametre stockés par defaut dans un tuple
            self.animaux.append(animal) # et on l'ajoute dans le liste
            print(f"{animal.e} a été ajouté a {self.nom}") #afficher que l'animal a été bien ajouté !
    def Afficher(self):
        l=[]
        for animal in self.animaux : #comme la liste des animaux contien des classe Animal on affiche juste les nom,couleur,pattes pour faciliter !
            l.append((animal.e,animal.c,animal.n))
        print(f" | Maison : {self.nom} ---> listes des animaux : {l} | ")