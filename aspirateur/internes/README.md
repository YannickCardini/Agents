# Agent Aspirateur Réflexe
Agent aspirateur réflexe avec un état interne dont l'emplacement initial (salles A ou B) est initialement aléatoire, puis dépend de l'état précédent. Il en est de même pour l'état des salles (sale ou propre).

## Executer:
```bash
python3 aspirateur.py
```
## Fonctionnement:

L'aspirateur est initialement dans une sale aléatoire qui aléatoirement propre ou sale.

### Si la salle est sale

Il la nettoie, passe à la suivate et mémorise la salle ou il se trouvait ainsi que son nouvelle état.

### Si la salle est propre

Il  passe à la suivate et mémorise la salle ou il se trouvait ainsi que son nouvelle état.

### Si il y a un obstacle

L'aspirateur s'arrête de bouger.

Comme il mémorise la salle précédente où il se trouvait ainsi que son état, il ne fait rien si il se trouve dans une sale propre et que l'ancienne l'était aussi.

