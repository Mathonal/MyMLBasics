# On importe les librairies dont on aura besoin pour ce tp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def regression_using_librairie():
	#from sklearn import linear_model
	regr = linear_model.LinearRegression()
	regr.fit(surface, loyer)
	regr.predict(donnee_test)

def main():
	# DECOMPOSITION DES ETAPES DE CREATION D UNE REGRESSION LINEAIRE.

    # On charge le dataset
    house_data_raw = pd.read_csv('house.csv')
    # on filtre le data set (tronque les valeurs élevées)
    house_data = house_data_raw[house_data_raw['loyer'] < 7000]

    # On affiche le nuage de points dont on dispose
    plt.plot(house_data['surface'], house_data['loyer'], 'ro', markersize=1)
    #plt.show()


    # On décompose le dataset et on le transforme en matrices pour pouvoir effectuer notre calcul

    X = np.matrix([np.ones(house_data.shape[0]), house_data['surface'].as_matrix()]).T
    # fonction matrice(vecteur1dimension(formedetableauhousedata)), valeurdesdonnéeshousedata).TRANSPOSEE
    # matrice(vecteur(1), reste des données).TRANSPOSEE
    #le but de la premiere valeur est d'avoir une valeur d'ordonnée a l'origine d'abscisse.
    # la transposée est utilisé pour avoir une matrice format colonne

    y = np.matrix(house_data['loyer']).T

    # On effectue le calcul exact du paramètre theta
    # la formule est obtenue : θ^=(XTX)−1XTy
    # (derivée d'une fonction normale pour regression lineaire : 
    #https://eli.thegreenplace.net/2014/derivation-of-the-normal-equation-for-linear-regression)
    theta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

    # print(theta)
    # theta donne : [294.3;30],donc l'approximation donne : loyer = 30 × surface + 294.3

    # On affiche la droite entre 0 et 250
    plt.plot([0,250], [theta.item(0),theta.item(0) + 250 * theta.item(1)], linestyle='--', c='#000000')




    #ON utilise ensuite les valeur de theta pour prédire une réponse pour une valeur données
    while 1:
        print('saisir une surface dappartement: ')
        surfaceinpt = input("->")

        try:
            loyervaleur = theta.item(0) + theta.item(1) * int(surfaceinpt)
            print('loyer estimé pour une surface de {}m²: {}'.format(surfaceinpt, loyervaleur))
        except:
            break

    plt.show()