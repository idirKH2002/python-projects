from Client import Client
from Voiture import Voiture
from Abonnement import Abonnement
from Parking import Parking
from acces import acces

 
if __name__ == "__main__":
    parking = Parking(
    nbplacelibre=10,
    places=[],  
    abonnements=["abonne", "super abonne"],
    nbPlaceParNiveau=20, 
    prix=5.0,  
    nbniveau=3  
    )
    
    
    abonnement_super = Abonnement("super Abonne",50.0,True)
    
    C1= Client( "Jean", "Paris",False,True,abonnement_super)
    V1= C1.nouvelleVoiture("AA-123-AA", 2, 4)
    acces_parking = acces(num=1) 
    acces_parking.parking = parking  
    
   
    
    acces_parking.actionercamera(C1)
    print(acces_parking.acctionerpanneau())
    acces_parking.lancerprocedureentre(C1)
    
    # C1.demandeMaintenance()
    # C1.demanderEntretien()
    # C1.demanderlivraison("Paris","01/01/2021","12:00")