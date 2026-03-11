from fonctionTake import *
from fonctiongame import *

def player2(ID: int, baton: int) -> int:
    '''
    Fonction qui gère le comportement du joueur 2.
    '''
    from fonctionTake import take
    restant_baton = baton
    if restant_baton != 0:
        if ID == 2:
            nb_baton = take(restant_baton)
            return(nb_baton)
        else:
            return(None)
    else :
        if ID == 2:
            return(True)
        else:
            return(False)