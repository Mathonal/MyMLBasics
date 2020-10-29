import numpy as np
from enum import Enum

class Strategie(Enum):
    CHANGER = 1
    GARDER = 2

def play(strategie, nb_tours):
    '''
    Simule une suite de tours du jeu.
    
    Cette fonction renvoie les résultats de plusieurs parties
    du jeu Monty Hall sous forme d'un tableau de gains par le 
    joueur.
    
    Args:
        strategie (Strategie): La strategie du joueur
        nb_tours (int): Nombre de tours
        
    Returns:
        numpy array: Tableau des gains du joueurs à chaque partie
    '''
    
    # Création d'un tableau stockant la bonne porte pour chaque tour.
    bonne_porte = np.random.randint(low=0, high=3, size=(nb_tours,))
    
    # Création d'un tableau stockant le premier choix pour chaque tour.
    premier_choix = np.random.randint(low=0, high=3, size=(nb_tours,))
    
    # Après le premier choix, on propose une porte restante pouvant être choisie à la place de la première.
    # La porte restante n'est pas:
    #    - la porte choisie en premier choix
    #    - la porte éliminée qui ne contient rien
    # On a donc 4 possibilités pour chaque partie:
    #   1. premier_choix != bonne_porte donc porte_restante = bonne_porte
    #   2. premier_choix == bonne_porte et premier_choix == 0 donc porte_restante = 1 ou 2
    #   3. premier_choix == bonne_porte et premier_choix == 1 donc porte_restante = 0 ou 2
    #   4. premier_choix == bonne_porte et premier_choix == 2 donc porte_restante = 0 ou 1
        
    # Création d'un tableau stockant la porte restante pour chaque tour.
    porte_restante = np.zeros((nb_tours,), dtype=int)
    
    # Création des index de parties par possibilités
    index_different = np.where(bonne_porte!=premier_choix) # Index des parties ou bonne_porte != premier_choix
    index_1_2 = np.where((bonne_porte==premier_choix) & (premier_choix == 0))
    index_0_1 = np.where((bonne_porte==premier_choix) & (premier_choix == 2))
    index_0_2 = np.where((bonne_porte==premier_choix) & (premier_choix == 1))
 
    # Création de trois tableaux stockant la porte restante pour chaque tour selon 3 possibilités.
    random_1_2 = np.random.randint(low=1, high=3, size=nb_tours)
    random_0_1 = np.random.randint(low=0, high=2, size=nb_tours)
    random_0_2 = np.random.choice([0,2], size=nb_tours)

    # Actualisation tableau porte_restante
    porte_restante[index_different] = bonne_porte[index_different]
    porte_restante[index_1_2] = random_1_2[index_1_2]
    porte_restante[index_0_1] = random_0_1[index_0_1]
    porte_restante[index_0_2] = random_0_2[index_0_2]

    if strategie == Strategie.CHANGER:
        deuxieme_choix = porte_restante
    elif strategie == Strategie.GARDER:
        deuxieme_choix = premier_choix
    else:
        assert("Erreur")
    
    return np.equal(deuxieme_choix, bonne_porte)*1