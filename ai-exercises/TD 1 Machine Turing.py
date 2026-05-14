def créer_MT(etat,tete,chaine,taille):
    d={}
    ruban=[]
    for c in chaine :
        if c == "1" or c == "0" or c==" " :
            ruban.append(c)
        else :
            return print("Erreur")
    if etat in {"e1","e2","eFinal"} and tete<=len(ruban)-1 and taille >= len(chaine):
        d["etat"]=etat
        d["tete"]=tete
        d["ruban"]=ruban
        d["taille"]=taille
    return d


def deplacer_tete(mt,direction):
    if direction == "gauche" or "g" :
        mt["tete"] -= 1
    if direction == "droite" or "d":
        mt["tete"] += 1
    return mt

def lire_ruban(mt):
    c = mt["tete"]
    ruban = mt["ruban"]
    return ruban[c]


def affiche_ruban(mt):
    c = mt["tete"]
    ruban = mt["ruban"]
    return ruban[c:]