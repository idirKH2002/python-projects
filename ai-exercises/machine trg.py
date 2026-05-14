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
    if direction == "g" :
        mt["tete"] -= 1
    if direction == "d":
        mt["tete"] += 1
    return mt , mt["tete"]

def lire_ruban(mt):
    c = mt["tete"]
    ruban = mt["ruban"]
    return ruban[c]


def affiche_ruban(mt):
    c = mt["tete"]
    ruban = mt["ruban"]
    return ruban[c:]

def executer_prog(mt,programme):
    while mt["etat"] != "eFinal" :
        instr = programme[(mt["etat"],lire_ruban(mt))]
        if mt["etat"] == instr[0] and lire_ruban(mt)== instr[1] :
            mt["etat"] = [instr][0]
            if lire_ruban(mt) != " " :
                mt["tete"] = programme[instr][1]
            if programme[instr][2] != " " :
                deplacer_tete(mt,programme[instr][2])
    return mt

programme = {("e1","0"):["e2"," "," "],("e1","1"):["e2"," "," "],("e2","1"):["e2"," ","d"],("e2","0"):["e2","1","d"],("e2"," "):["eFinal"," "," "]}

maaat = {'etat': 'e1', 'tete':5, 'ruban': ['1', '0', '1', '0', '1', '1', '1', ' ', '1', '0', '1', '1'], 'taille': 19}
mt = créer_MT("e1",1,"10000000001",20)

print(executer_prog(mt,programme))
    

                    
                    
                
                
        
    
    