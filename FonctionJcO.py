from FonctionPlayer1 import *
from FonctionRematch import *
from FonctionScreen import *
from fonctionlose import *
from FonctionOrdinateur import *

def game_jco(baton)->int:
    '''
    Cette fonction permet de gérer le comportement global du jeu et d'utiliser toutes les fonctions.
    '''
    import random
    turn = random.randint(0,1)
    restant_baton = baton
    screen(restant_baton)
    while restant_baton != 0:
        if turn % 2 == 0:
            ID = 1
            print("")
            print("C'est au tour du joueur", ID)
            print("")
            restant_baton = player1(ID, restant_baton) + restant_baton
            print("")
            screen(restant_baton)
            if restant_baton == 0:
                lose(ID, restant_baton, 2)
        else:
            ID = 3
            print("")
            print("C'est au tour de l'ordinateur")
            print("")
            restant_baton = playerO(ID, restant_baton) + restant_baton
            print("")
            screen(restant_baton)
            from fonctionlose import lose
            if restant_baton == 0:
                lose(ID, restant_baton, 2)
        turn = turn + 1