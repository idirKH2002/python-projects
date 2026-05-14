import Place
class Parking:
    def __init__(self, nbPlaceParNiveau, prix, nbniveau, nbplacelibre, places = [], abonnements = []):
        self.nbPlaceParNiveau = nbPlaceParNiveau
        self.nbplacelibre = nbplacelibre
        self.prix = prix
        self.nbniveau = nbniveau
        self.abonnements = []
        self.places = []
        
    def reprendrevoiture(self,client):
        print("avez vous votre ticket ?")
        T = input("oui/non")
        if T == "oui":  
            for place in self.places:
                if place.num == client.voiture.immatriculation:
                    place.estlibre = False
                    place.num = None
                    print("Le client", client.name, "a repris sa voiture")
                    self.nbplacelibre += 1
                    print("teleporteur activé")