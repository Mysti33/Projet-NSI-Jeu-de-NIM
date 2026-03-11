from FonctionPlayer1 import *
from FonctionPlayer2 import *
from FonctionRematch import *
from FonctionScreen import *
from fonctionlose import *

def game(baton)->int:
    '''
    Cette fonction permet de gérer le comportement global du jeu et d'utiliser toutes les fonctions.
    '''
    turn = 0
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
                lose(ID, restant_baton, 1)
        else:
            ID = 2
            print("")
            print("C'est au tour du joueur", ID)
            print("")
            restant_baton = player2(ID, restant_baton) + restant_baton
            print("")
            screen(restant_baton)
            if restant_baton == 0:
                lose(ID, restant_baton, 1)
        turn = turn + 1