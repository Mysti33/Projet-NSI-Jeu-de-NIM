from fonctiongame import *

def rematch() -> bool:
    '''
    Fonction permettant de demander aux joueurs de relancer une partie
    '''
    rejouer = input("Voulez vous rejouer ? [O/N] : ")
    if rejouer == "O" or rejouer == "o":
        return(True)
    else:
        return(False)