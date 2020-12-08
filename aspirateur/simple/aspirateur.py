
import random

def aspirateur(EMPLACEMENT,ETAT,OBSTACLE):
    if(ETAT == "sale"):
        return "aspirer"
    else:
        if(OBSTACLE):
            return ("stop")
        else:
            return ("avancer")


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
    if(actionAspirateur == "avancer"):
        if(EMPLACEMENT == "A"):
            EMPLACEMENT = "B"
        else:
            EMPLACEMENT = "A"

