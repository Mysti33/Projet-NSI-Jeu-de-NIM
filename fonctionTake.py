from FonctionPlayer1 import *
from FonctionPlayer2 import *
from fonctiongame import *

def take(restant_baton) -> int:
    '''
    Fonction qui permet de demander au joueur de choisir entre 1 à 3 bâtons à retirer
    '''
    nbr_batons = int(input("Combien de bâtons voulez vous retirer ? [1/2/3] : "))
    if restant_baton >= 3:
        if nbr_batons == 1 or nbr_batons == 2 or nbr_batons == 3 :
            if nbr_batons == 1:
                return(-1)
            elif nbr_batons == 2:
                return(-2)
            elif nbr_batons == 3:
                return(-3)
        else :
            return(take(restant_baton))
    elif restant_baton == 2:
        if nbr_batons == 1 or nbr_batons == 2:
            if nbr_batons == 1:
                return(-1)
            elif nbr_batons == 2:
                return(-2)
        else :
            return(take(restant_baton))
    elif restant_baton == 1:
        if nbr_batons == 1:
            if nbr_batons == 1:
                return(-1)
        else :
            return(take(restant_baton))