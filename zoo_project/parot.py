#creation de la classe Parot heritée par la classe Animal

from animal import Animal   #on importe depuis le fichier animal.py la classe Animal
class Parot(Animal):
    def __init__(self,couleur):
        super().__init__(couleur,"Perroquet",2) #heritage fct super(), et chaque espece on lui donne son nom et son nb de pattes par defaut , la couleur sera passée en parametre
