import Services
import Voiturier
class Livraison(Services):
    def effectuerlivraison(self):
        voiturier.livrervoirture(self.voiture,self.dateServices,self.heure)
        
        
    