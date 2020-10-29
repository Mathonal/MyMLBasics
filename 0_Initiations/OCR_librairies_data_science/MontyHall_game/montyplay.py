from enum import Enum
import numpy as np
# Ici nous définissons une sous-classe de Enum, qui contiendra 
# les stratégies possibles.
class Strategie(Enum):
    CHANGER = 1
    GARDER = 2
    
def playgame(strategie, nb_tours):
    '''Simule une suite de tours du jeu.
    
    Cette fonction renvoie les résultats de plusieurs parties
    du jeu Monty Hall sous forme de tableau (numpy) de gains par le 
    joueur.
    
    Args:
        strategie (Strategie): La strategie du joueur
        nb_tours (int): Nombre de tours
        
    Returns:
        tableau matrice [1;nb_tours]: resultat des gains du joueurs à chaque partie
    '''
    
    #génération des tirages : autant de tirage random [0:3[ que de nbtours
    tab_BonnesPortes = np.random.randint(0,3,nb_tours)
    tab_1erChoix = np.random.randint(0,3,nb_tours)
    
    # Traitement par stratégie :
    if strategie == Strategie.GARDER:
        # on compte juste le nombre de bon choix dès le départ
        # genere un tableau de comparaison booleen
        tab_CheckWin = tab_BonnesPortes == tab_1erChoix
        return tab_CheckWin
        # on compte le nombre de True dans le tableau
        int_WinCount = sum(tab_CheckWin)
        return int_WinCount
    
    if strategie == Strategie.CHANGER:
        # on compte juste le nombre de mauvais choix dès le départ,
        # en changeant de choix, ils gagneront automatiquement
        
        # genere un nouveau tableau conservant tous les mauvais premier choix
        tab_CheckMauvais1erChoix = tab_BonnesPortes != tab_1erChoix
        return tab_CheckMauvais1erChoix
        # on compte le nombre de True dans le tableau
        int_WinCount = sum(tab_CheckMauvais1erChoix)
        return int_WinCount
        