
import random

MEMOIREASPIRATEUR = None
ETAT = [("A",'sale')]
BUT = [[("A","propre"),("B","propre"),("D","propre"),("F","propre")],[("A","propre"),("C","propre"),("E","propre"),("G","propre"),("F","propre")]]

def goalBasedAgent(percept):
    if percept == "A":
        return random.choice(["gauche","droite"])
    elif percept == "B" or percept == "C" or percept == "D" or percept == "E":
        return "avancer"
    elif percept == "G":
        return "gauche"
    else:
        return "stop"

def obtainPercept(ETAT,lastAction):
    ETAT[-1] = (ETAT[-1][0],"propre")
    if(lastAction != None):
        if(lastAction == "gauche"):
            if(ETAT[-1][0] == "A"):
                ETAT.append(("B","sale"))
            elif(ETAT[-1][0] == "G"):
                ETAT.append(("F","sale"))
        elif(lastAction == "droite"):
            if(ETAT[-1][0] == "A"):
                ETAT.append(("C","sale"))
        elif(lastAction == "avancer"):
            if(ETAT[-1][0] == "B"):
                ETAT.append(("D","sale"))
            elif(ETAT[-1][0] == "C"):
                ETAT.append(("E","sale"))
            elif(ETAT[-1][0] == "D"):
                ETAT.append(("F","sale"))
            elif(ETAT[-1][0] == "E"):
                ETAT.append(("G","sale"))
    return ETAT[-1][0]
        
     
def aspirateur(ETAT,lastAction):
    if(ETAT in BUT):
        return "GOAL ACHIEVE"
    else:
        percept = obtainPercept(ETAT,lastAction)
        return(goalBasedAgent(percept))

lastAction = None
while lastAction != "GOAL ACHIEVE":
    lastAction = aspirateur(ETAT,lastAction)
    print(ETAT)
print("GOAL ACHIEVE !")