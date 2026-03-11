from fonctiongame import *

def screen(baton: int) -> str:
    '''
    Fonction permettant d'afficher le nombre de bâtons restants graphiquement.
    '''
    n = baton
    print(n*"|", "", "(",n,")")