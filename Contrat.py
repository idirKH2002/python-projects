class Contrat:
    def __init__(self,dateDebut,dateFin, duree,estencours):
        self.dateDebut = dateDebut
        self.dateFin = dateFin
        self.duree = duree
        self.estencours = bool(estencours)
        