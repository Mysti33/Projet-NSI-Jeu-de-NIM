from fonctiongame import *
from FonctionRematch import *
from FonctionGameMode import *
from FonctionJcO import *

Mode = game_mode()
Nombre_baton = int(input("Combien de batons voulez vous avoir pour la partie ? (20 par défaut) : "))

if Mode == 1:
    game(Nombre_baton)
else:
    game_jco(Nombre_baton)


while rematch() != False:
    Mode = game_mode()
    Nombre_baton = int(input("Combien de batons voulez vous avoir pour la partie ? (20 par défaut) : "))
    if Mode == 1:
        game(Nombre_baton)
    else:
        game_jco(Nombre_baton)


print("")