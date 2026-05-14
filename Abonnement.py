class Abonnement :
    def __init__(self,libellé,prix, estPackGar):
        self.libellé = libellé
        self.prix = prix
        self.estPackGar = bool(estPackGar)
        
       