from fonctionTake import *
from fonctiongame import *

def player1(ID: int, baton: int) -> int:
    '''
    Fonction qui gère le comportement du joueur 1.
    '''
    from fonctionTake import take
    restant_baton = baton
    if restant_baton != 0:
        if ID == 1:
            nb_baton = take(restant_baton)
            return(nb_baton)
        else:
            return(None)
    else :
        if ID == 1:
            return(True)
        else:
            return(False)
        