# On importe les librairies dont on aura besoin pour ce tp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_mldata
from sklearn.model_selection import train_test_split

from sklearn import neighbors


def main():
    xtrain, xtest, ytrain, ytest = init()
    #affichage_randomprediction(xtrain, xtest, ytrain, ytest)
    affichage_errorprediction(xtrain, xtest, ytrain, ytest)

def init():
    print('charger les données')
    mnist = fetch_mldata('MNIST original', data_home='./donnees_scikit')

    # generer un sampling de test a partir des données brute
    # utiliser plutot : sklearn.utils.resample car randint peut generer des doublons
    print('sampling')
    sample = np.random.randint(70000, size=5000)
    
    # data contient les images a identifier
    data = mnist.data[sample]

    # target contient les annotations (solutions) correspondant a chaque data
    target = mnist.target[sample]

    #separation des données entre trainset et testset (80%/20%)
    print('creation set training/tests')
    xtrain, xtest, ytrain, ytest = train_test_split(data, target, train_size=0.8)

    return xtrain, xtest, ytrain, ytest


def recherchemeilleurk(xtrain, xtest, ytrain, ytest):
    # Utilisation du classifieur Kneighboors (pas de regression ou d'optimisation)
    print('entrainement KNN')
    knn = neighbors.KNeighborsClassifier(n_neighbors=3)
    knn.fit(xtrain, ytrain)

    # verification du taux d'erreur sur le test score 
    error = 1 - knn.score(xtest, ytest)
    print('Taux dErreur sur testset : %f' % error)

    #Recherche du nombre de voisins optimal pour minimisation du taux d'erreurs
    errors = []
    #boucle d'entrainements consecutifs entre 2 et 15 voisins
    print('boucle d''optimisation')
    for k in range(2, 15):
        knn = neighbors.KNeighborsClassifier(k)
        errors.append(100*(1 - knn.fit(xtrain, ytrain).score(xtest, ytest)))
        print('essai k = {}, taux derreur = {}'.format(k, errors[len(errors)-1]))

    plt.plot(range(2, 15), errors, 'o-')
    plt.show()


def affichage_randomprediction(xtrain, xtest, ytrain, ytest):
    # On récupère le classifieur le plus performant
    K = 7
    knn = neighbors.KNeighborsClassifier(K)
    knn.fit(xtrain, ytrain)

    # On récupère les prédictions sur les données test
    predicted = knn.predict(xtest)

    # On redimensionne les données sous forme d'images
    images = xtest.reshape((-1, 28, 28))

    # On selectionne un echantillon de 12 images au hasard
    select = np.random.randint(images.shape[0], size=12)

    # On affiche les images avec la prédiction associée
    for index, value in enumerate(select):
        plt.subplot(3,4,index+1)
        plt.axis('off')
        plt.imshow(images[value],cmap=plt.cm.gray_r,interpolation="nearest")
        plt.title('Predicted: %i' % predicted[value])

    plt.show()

def affichage_errorprediction(xtrain, xtest, ytrain, ytest):
    # On récupère le classifieur le plus performant
    K = 7
    knn = neighbors.KNeighborsClassifier(K)
    knn.fit(xtrain, ytrain)

    # On récupère les prédictions sur les données test
    predicted = knn.predict(xtest)
    # On redimensionne les données sous forme d'images
    images = xtest.reshape((-1, 28, 28))

    # on récupère les données mal prédites 
    misclass = (ytest != predicted)
    misclass_images = images[misclass,:,:]
    misclass_predicted = predicted[misclass]

    # on sélectionne un échantillon de ces images
    select = np.random.randint(misclass_images.shape[0], size=12)

    # on affiche les images et les prédictions (erronées) associées à ces images
    for index, value in enumerate(select):
        plt.subplot(3,4,index+1)
        plt.axis('off')
        plt.imshow(misclass_images[value],cmap=plt.cm.gray_r,interpolation="nearest")
        plt.title('Predicted: %i' % misclass_predicted[value])

    plt.show()
