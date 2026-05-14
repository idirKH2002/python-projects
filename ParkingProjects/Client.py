import Voiture
import Abonnement
class Client:
    def __init__(self, name,addresse,abonne,Superabonne,abonnement):
        self.name = name
        self.addresse = addresse
        self.abonne = bool(abonne)
        self.Superabonne = bool(Superabonne)
        self.abonnement = abonnement
       
        
        
    def sAbonner (self,abonnement):
        self.abonne = True
        self.abonnement = abonnement
        print("Le client", self.name ,"s'est abonné a " , abonnement.libellé) 
        
    def nouvelleVoiture(self,immatriculation,hauteur,longeur):
        self.voiture = Voiture.Voiture(hauteur,longeur,immatriculation,False)
        print("Le client", self.name ,"a ajoute une nouvelle voiture")
        
    def sedésabonner(self):
        self.abonne = False
        print("Le client", self.name ,"s'est désabonné")
        
    def demandeMaintenance(self):
        
        if self.Superabonne:
            print(f"Le client {self.name} (super abonne) a demande une maintenance.")
        elif self.abonne:
            print(f"Le client {self.name} (abonne) a demande une maintenance.")
        else:
            print(f"Le client {self.name} n'est pas abonné et ne peut pas demander de maintenance.")
    
    def demanderlivraison(self,addressLiv,date,heure):
        if self.Superabonne:
            print(f"Le client {self.name} (super abonne) a demande une livraison a l'adresse {addressLiv} le {date} à {heure}.")
        elif self.abonne:
            print(f"Le client {self.name} (abonne) a demande une livraison à l'adresse {addressLiv} le {date} à {heure}.")
        else:
            print(f"Le client {self.name} n'est pas abonne et ne peut pas demander de livraison.")
            
    def demanderEntretien(self):
        if self.Superabonne:
            print(f"Le client {self.name} (super abonne) a demande un entretien de sa voiture.")
        elif self.abonne:
            print(f"Le client {self.name} (abonne) a demande un entretien.")
        else:
            print(f"Le client {self.name} n'est pas abonné et ne peut pas demander d'entretien.")
            
            


 
    def afficher(self):
        print("Nom:",self.name)
        print("Adresse:",self.addresse)
        print("Abonne:",self.abonne)
        print("Superabonne:",self.Superabonne)
        print("Nombre de frequentation:",self.nbFrequantation)
        print("Voiture:",self.voiture.immatriculation)
        