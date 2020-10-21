
import random

firstChoice = None
ETAT = [("A",'sale')]
BUT = [[("A","propre"),("B","propre"),("D","propre"),("F","propre")],[("A","propre"),("C","propre"),("E","propre"),("G","propre"),("F","propre")]]

def utilityBasedAgent(percept):
    if percept == "A":
        global firstChoice
        if(firstChoice != None):
            if(firstChoice == "gauche"):
                firstChoice = "droite"
            else:
                firstChoice = "gauche"
        else:  
            firstChoice = random.choice(["gauche","droite"])
        return firstChoice
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

def obtainScore(ETAT):
    return len(ETAT)

def bestScore(score):
    return True if score <= 4 else False
      
     
def aspirateur(ETAT,lastAction):
    if(ETAT in BUT):
        if bestScore(obtainScore(ETAT)):
            print("Meilleure score trouvé: ",end='')
            return "GOAL ACHIEVE"
        else:
            print("Meilleure score non trouvé, on recommence:")
            ETAT[:] = [("A",'sale')]
            return None
    else:
        percept = obtainPercept(ETAT,lastAction)
        return(utilityBasedAgent(percept))

lastAction = None
while lastAction != "GOAL ACHIEVE":
    lastAction = aspirateur(ETAT,lastAction)
    print(ETAT)
