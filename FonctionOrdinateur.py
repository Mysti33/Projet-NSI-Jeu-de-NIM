from fonctionTake import *
from fonctiongame import *
from FonctionJcO import *

def playerO(ID: int, baton: int) -> int:
    '''
    Fonction qui gère le comportement du joueur 2.
    '''
    from fonctionTake import take
    restant_baton = baton
    if restant_baton != 0:
        if ID == 3:
            
            import random
            import time
            time.sleep(1)
            if restant_baton > 3:
                nb_baton = random.randint(1,3)
            elif restant_baton == 3:
                nb_baton = random.randint(1,2)
            elif restant_baton == 2:
                nb_baton = 1
            elif restant_baton == 1:
                return(-1)
            
            if nb_baton == 1:
                return(-1)
            elif nb_baton == 2:
                return(-2)
            elif nb_baton == 3:
                return(-3)
            
        else:
            return(None)
    else :
        if ID == 3:
            return(True)
        else:
            return(False)