# Agent Aspirateur Réflexe
Agent aspirateur réflexe avec état interne, un but et utilité.
## Executer:
```bash
python3 aspirateur.py
```
## Fonctionnement:

L'aspirateur commence dans la salle A. Il se déplace ensuite aléatoirement à gauche ou à droite.
Selon son ancienne action, il va soit avancer, soit aller à droite, soit aller à gauche pour réaliser son but.
Son but étant d'arriver à la salle F en nettoyant l’une des deux trajectoires possibles.
Tant que l'aspirateur ne renvoie pas "GOAL ACHIEVE" le programme continue.
Pour que le programme renvoie "GOAL ACHIEVE" il doit en plus de réaliser son but, trouver le meilleur chemin.
Si il ne trouve pas le meilleure chemin du premier coup, il recommence du début en changeant son premier choix (si il avait fait gauche, il ira à droite cette fois-ci et inversement).

