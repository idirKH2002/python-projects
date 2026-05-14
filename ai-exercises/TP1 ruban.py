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
def lire_ruban(mt):
    c = mt["tete"]
    ruban = mt["ruban"]
    return ruban[c]
def affiche_ruban(mt):
    c = mt["tete"]
    ruban = mt["ruban"]
    return ruban[c:]
    
    
print(affiche_ruban({'etat': 'e1', 'tete': 4, 'ruban': ['1', '0', '1', '0', '1', '1', '1', ' ', '1', '0', '1', '1'], 'taille': 19}))

            
            
     
    
    
    
