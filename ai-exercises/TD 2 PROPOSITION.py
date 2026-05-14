def fbf(formule):
    if len(formule) == 0 :
        return False
    if len(formule) == 1 :
        if formule in "abcdefghijklmnopqrstuvwxyz":
            return True
        else :
            return False
    if len(formule) >= 2 :
        f=""
        l=list(formule)
        if l[0] == "~" :
            for i in l[1:] :
                f+=i
            return fbf(f) 
        else :
            if l[0] =="(" and l[-1] == ")" :
                f1=""
                f2=""
                p=0
                indice = 0
                for i in range(1,len(l)-1):
                    if l[i] == "(" :
                        p+=1
                    if l[i] == ")" :
                        p-=1
                    if l[i] in "&|<>" and p == 0 :
                        indice = i
                for j in range(1,indice):
                    f1+=l[j]
                for j in range(indice+1 , len(l)-1):
                    f2+=l[j]
                return (fbf(f1) and fbf(f2))
            else :
                return False
def evalue(formule, interp) :
    if fbf(formule):
         l=list(formule)
    if len(l)== 1 :
        return interp[str(l[0])]
    if len(l) >= 2 :
        if l[0] == "~":
            return not(interp[str(l[1])])
        else :
            if l[0] =="(" and l[-1] == ")":
                f1=""
                f2=""
                p=0
                res = True
                indice = 0
                for i in range(1,len(l)-1):
                    if l[i] == "(" :
                        p+=1
                    if l[i] == ")" :
                        p-=1
                    if l[i] in "&|<>" and p==0 :
                        indice = i
                    if l[i] in "&|<>" and p != 0:
                        if l[i] == "&":
                            return evalue(str(l[i-1]),interp) and evalue(str(l[i+1]),interp)
                        if l[i] == "|":
                            return evalue(str(l[i-1]),interp) or evalue(str(l[i+1]),interp)
                        if l[i] == "~":
                            res = not interp[str(l[i+1])]
                for j in range(1,indice):
                    f1+=l[j]
                for j in range(indice+1 , len(l)-1):
                    f2+=l[j]
                if l[indice] == "&":
                    return evalue(f1,interp) and evalue(f2,interp)
                if l[indice] == "|":
                    return evalue(f1,interp) or evalue(f2,interp)
def  table_verite(formule) :
    if fbf(formule):
        l=list(formule)
        mot=""
        c = set()
        cont = 1
        for i in formule :
            if i in "abcdefghigklmnopqrstuvwxyz":
                c.add(i)
        if len(c) == 1 :
            res ="| "
            for i in c:
                mot = i
                res+= i + " | "
                inp={str(i):True}
            res +="f\n"
            for i in range(len(c)):
                cont*=2
            for i in range(1,cont+1):
                if i%2 == 1:
                    res += " | " + "False" + " | "+str(not evalue(mot,inp))+" |\n"
                else :
                    res += " | " + "True" + " | "+str(evalue(mot,inp))+" |\n"   
            return res 
        if len(c)>=2:
            if l[0] == "~":
                res ="| "
                for i in c:
                    mot = i
                    res+= i + " | "
                    inp={str(i):True}
                res +="f |\n"
                for i in range(len(c)):
                    cont*=2
                for i in range(1,cont+1):
                    if i%2 == 1:
                        res += " | " + "False" + " | "+str(evalue(mot,inp))+" |\n"
                    else :
                        res += " | " + "True" + " | "+str(not evalue(mot,inp))+" |\n"
                return res
            if l[0] =="(" and l[-1] == ")" :
                f1=""
                f2=""
                p=0
                indice = 0
                for i in range(1,len(l)-1):
                    if l[i] == "(" :
                        p+=1
                    if l[i] == ")" :
                        p-=1
                    if l[i] in "&|<>" and p == 0 :
                        indice = i
                for j in range(1,indice):
                    f1+=l[j]
                for j in range(indice+1 , len(l)-1):
                    f2+=l[j]
                return (table_verite(f1) + table_verite(f2))
            
    
        
        
        
    
                
                        
                    
            
print(fbf("((a&b)|~(a&c))"))
print(fbf("((a&b)|~a&c)"))
print(evalue("((a&b)|~(a&c))",{"a":True,"b":False,"c":True}))
print(evalue("((a&b)|~(a&c))",{"a":True,"b":True,"c":False}))
print(table_verite("(a&b)"))
