def deplacer_tete(mt,direction):
    if direction == "gauche":
        mt["tete"] -= 1
    if direction == "droite" :
        mt["tete"] += 1
    return mt


    
print(deplacer_tete({'etat': 'e1', 'tete': 4, 'ruban': ['1', '0', '1', '0', '1', '1', '1', ' ', '1', '0', '1', '1'], 'taille': 19},"gauche"))

    
    
