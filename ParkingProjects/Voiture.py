class Voiture :
    def __init__(self, hauteur, longeur,immatriculation,estDansParking):
        self.hauteur = hauteur
        self.longeur = longeur
        self.immatriculation = immatriculation
        self.estDansParking = bool(estDansParking)