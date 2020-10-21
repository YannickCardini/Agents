
import random


EMPLACEMENT_ARR = ["A","B"]
ETAT_ARR = ["sale","propre"]
OBSTACLE_ARR = [True,False]
EMPLACEMENT = random.choice(EMPLACEMENT_ARR)
ETAT = random.choice(ETAT_ARR)
MEMOIREASPIRATEUR = None

def aspirateur(EMPLACEMENT,ETAT,OBSTACLE):
    if(ETAT == "sale"):
        action = "aspirer"
    else:
        global MEMOIREASPIRATEUR
        if(EMPLACEMENT == "A"):
            if(OBSTACLE or MEMOIREASPIRATEUR == ("B","propre")):
                action = "stop"
            else:
                action = "droite"
        else:
            if(OBSTACLE or MEMOIREASPIRATEUR == ("A","propre")):
                action = "stop"
            else:
                action = "gauche"
    MEMOIREASPIRATEUR = (EMPLACEMENT,"propre")
    return action


for i in range(0,5):
    OBSTACLE = random.choice(OBSTACLE_ARR)
    print("EMPLACEMENT : ", EMPLACEMENT," ETAT : ", ETAT, "OBSTACLE : ", OBSTACLE )
    actionAspirateur = aspirateur(EMPLACEMENT,ETAT,OBSTACLE)
    print("ACTION ASPIRATEUR : ", actionAspirateur)
    if(actionAspirateur == "droite" ):
        EMPLACEMENT = "B"
    elif(actionAspirateur == "gauche"):
        EMPLACEMENT = "A"

