#creation de la classe (mere) Animal 
class Animal:
    def __init__(self,couleur,espece,nb_pattes) :
        self.c = couleur 
        self.e = espece
        self.n = nb_pattes
    def Afficher(self):
        print(f"je suis un : {self.e} , de couleur : {self.c} , et j'ai {self.n} pattes") 