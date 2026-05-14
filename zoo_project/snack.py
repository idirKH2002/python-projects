#creation de la classe Snack (fille) heritée depuis la classe mere Animal 
from animal import Animal  #on importe depuis le fichier animal.py la classe Animal
class Snack(Animal):
    def __init__(self,couleur):
        super().__init__(couleur,"sérpent",0)   #heritage fct super(), et chaque espece on lui donne son nom et son nb de pattes par defaut , la couleur sera passée en parametre