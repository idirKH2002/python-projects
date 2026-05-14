import Voiture 
class voiturier :
    def __init__(self, numvoiturier):
        self.numvoiturier = numvoiturier
        
        
    def livrervoirture(self, voiture,date,heure):
        if voiture.estDansParking == True:
            print("Voiture livrée le",date,"à",heure)
            voiture.estDansParking = False
        else:
            print("Voiture non trouvée le",date,"à",heure)