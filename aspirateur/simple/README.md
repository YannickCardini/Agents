# Agent Aspirateur Réflexe
Programme d'un agent-aspirateur-réflexe simple
dont l’emplacement initial (salles A ou B) est aléatoire. Il en est de
même pour l’état des salles (sale ou propre).
## Executer:
```bash
python3 aspirateur.py
```
## Fonctionnement:

Un salle aléatoire est générée aléatoirement à l'initialisation (salle A ou B) puis une boucle de 10 répétitions est lancé.
A chaque répétition un état (propre ou sale) ainsi qu'un obstacle (true ou false) est générés aléatoirement.

1. Si l'aspirateur se trouve dans la salle A
2. Si il n'y a pas d'obstacle
3. Si l'état est propre

Il avance à la salle B

1. Si l'aspirateur se trouve dans la salle B
2. Si il n'y a pas d'obstacle
3. Si l'état est propre

Il avance à la salle A

1. Si l'aspirateur se trouve dans la salle A
2. Si il y a un obstacle
3. Si l'état est propre

Il se stoppe 

1. Si l'aspirateur se trouve dans la salle B
2. Si il y a un obstacle
3. Si l'état est propre

Il se stoppe 

1. Si l'aspirateur se trouve dans la salle A ou B
2. Si il y a un obstacle ou si il y en pas
3. Si l'état est sale

Il se stoppe et aspire



