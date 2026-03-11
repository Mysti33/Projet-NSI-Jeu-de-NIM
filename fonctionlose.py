from fonctiongame import *
from FonctionGameMode import *
from FonctionJcO import *

def lose (ID: int, restant_baton: int, mode: int)->int:
    '''
    Cette fonction s'occupe de la fin de partie en désignant le gagnant
    '''
    game_mode = mode
    if game_mode == 1:
        if ID == 1 and restant_baton == 0:
            return(print("Le joueur 2 à gagner la partie !"))
        elif ID == 2 and restant_baton == 0:
            return(print("Le joueur 1 à gagner la partie !"))
        else:
            return(None)
    elif game_mode == 2:
        if ID == 1 and restant_baton == 0:
            return(print("L'ordinateur à gagner la partie !"))
        elif ID == 3 and restant_baton == 0:
            return(print("Le joueur 1 à gagner la partie !"))
        else:
            return(None)