
import random

def aspirateur(EMPLACEMENT,ETAT,OBSTACLE):
    if(ETAT == "sale"):
        return ("stop","aspirer")
    else:
        if(EMPLACEMENT == "A"):
            if(OBSTACLE):
                return ("stop","droite")
            else:
                return ("avancer","droite")
        else:
            if(OBSTACLE):
                return ("stop","gauche")
            else:
                return ("avancer","gauche")

EMPLACEMENT_ARR = ["A","B"]
ETAT_ARR = ["sale","propre"]
OBSTACLE_ARR = [True,False]
EMPLACEMENT = random.choice(EMPLACEMENT_ARR)

for i in range(0,10):
    ETAT = random.choice(ETAT_ARR)
    OBSTACLE = random.choice(OBSTACLE_ARR)
    print("EMPLACEMENT : ", EMPLACEMENT," ETAT : ", ETAT, "OBSTACLE : ", OBSTACLE )
    actionAspirateur = aspirateur(EMPLACEMENT,ETAT,OBSTACLE)
    print("ACTION ASPIRATEUR : ", actionAspirateur)
    if(actionAspirateur[1] == "droite" & actionAspirateur[0] == "avancer"):
        EMPLACEMENT = "B"
    elif(actionAspirateur[1] == "gauche" & actionAspirateur[0] == "avancer"):
        EMPLACEMENT = "A"

