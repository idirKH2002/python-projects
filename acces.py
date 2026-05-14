from Parking import Parking
from Client import Client
from Abonnement import Abonnement


class Acces:
    def __init__(self, num):
        self.num = num
        self.parking = None

 
    def actionercamera(self,client):
        d={}
        d['nom']=client.name
        d['voiture']=client.voiture.immatriculation
        d['hauteur']=client.voiture.hauteur
        d['longeur']=client.voiture.longeur
        print(d)
        
    def acctionerpanneau(self):
        return str (self.parking.nbplacelibre)
    
    def lancerprocedureentre(self, client):
        if not client.Superabonne:
            print(f"Le client {client.name} n'est pas super abonné.")
            if self.parking.nbplacelibre > 0:
                if client.abonne:
                    service_voiturier = input("Voulez-vous un service voiturier ? (livraison, maintenance, entretien) oui/non: ").strip().lower()
                    if service_voiturier == "oui":
                        service_type = input("Quel service voulez-vous ? (livraison, maintenance, entretien): ").strip().lower()
                        if service_type == "livraison":
                            address = input("Entrez l'adresse de livraison : ").strip()
                            date = input("Entrez la date (jj/mm/aaaa) : ").strip()
                            heure = input("Entrez l'heure (hh:mm) : ").strip()
                            client.demanderLivraison(address, date, heure)
                        elif service_type == "maintenance":
                            client.demandeMaintenance()
                        elif service_type == "entretien":
                            client.demanderEntretien()
                        else:
                            print("Service non disponible.")
                    elif service_voiturier == "non":
                        print(f"Le client {client.name} n'a pas besoin de service voiturier.")
                else:
                    print("Mode de paiement (carte bancaire, espèces).")
                    abonnement_choice = input("Voulez-vous prendre un abonnement ? oui/non: ").strip().lower()
                    if abonnement_choice == "oui":
                        print("Les abonnements disponibles sont :", self.parking.abonnements)
                        abonnement_selection = input("Quel abonnement voulez-vous ? ").strip()
                        if abonnement_selection in self.parking.abonnements:
                            client.abonnement = abonnement_selection
                            print("Abonnement pris en compte.")
                        else:
                            print("Abonnement non disponible.")
                    else:
                        print("Abonnement non pris.")
            
            
                for place in self.parking.places:
                    if place.longeur >= client.voiture.longeur and place.hauteur >= client.voiture.hauteur:
                        place.estlibre = True
                        place.num = client.voiture.immatriculation
                        if place.estlibre:
                            print(f"Le client {client.name} a accès au parking.")
                            self.parking.nbplacelibre -= 1
                            print("Téléporteur active.")
                            self.actionercamera(client)
                            break
                    else:
                        print(f"Aucune place disponible pour le client {client.name}.")
            else:
                print("Le parking est complet.")
        else:
            print(f"Le client {client.name} est super abonne.")
            print("Actionner le teleporteur.")
            self.actionercamera(client)
            print(f"Le client {client.name} a acces au parking.")
            self.parking.nbplacelibre -= 1
            print("Teleporteur active.")