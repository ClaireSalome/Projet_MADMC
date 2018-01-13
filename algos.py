# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 17:10:15 2017

@author: clair
"""

from copy import deepcopy

import tools as tls
from timeit import default_timer as timer
from matplotlib import pyplot as plt
import numpy as np

"""QUESTION 3"""

# Proposer un premier algorithme naïf pour déterminer les vecteurs
# non-dominés, qui procède avec des comparaisons par paires systématiques.
# Implémenter cet algorithme.


def algo_naif(vectors):
    non_domines = deepcopy(vectors)
    # comparaison par paires
    for i in range(len(vectors)):
        # on vérifie que le vecteur est toujours candidat à la non-dominance
        if vectors[i] in non_domines:
            dominated = False
            for j in range(i + 1, len(vectors)):
                if vectors[j] in non_domines:
                    # si 1er < 2eme, 2eme dominé, on le retire de la liste
                    if (vectors[i][0] <= vectors[j][0]) and (vectors[i][1] <= vectors[j][1]):
                        non_domines.remove(vectors[j])
                        continue
                    # si 2eme < 1er, 1er dominé
                    if (vectors[j][0] <= vectors[i][0]) and (vectors[j][1] <= vectors[i][1]):
                        dominated = True
                        break
            if dominated == True:
                non_domines.remove(vectors[i])
    return non_domines


# v = tls.vector_factory(1000, 3.8)
# non_domines = algo_naif(v)
# tls.draw(v, non_domines)
#
# print("****Non dominés****")
# print(non_domines)


"""QUESTION 4"""

'''Proposer un second algorithme qui détermine les vecteurs nondominés
en réalisant tout d'abord (1) un tri lexicographique des vecteurs,
puis (2) un seul parcours de la liste obtenue pour identifier les vecteurs nondominés.
Implémenter cet algorithme.'''

def algo_tri_lex(vectors):
    non_domines = []
    sorted_vect = deepcopy(vectors)
    sorted_vect.sort(key=lambda colonne: (colonne[0], colonne[1]))
    vect_min = sorted_vect[0]
    c2_min = vect_min[1]
    # Le min sur le critère est forcément non dominé
    non_domines.append(vect_min)
    # pour tous les autres critèrs avec c1 > vect_min[0]
    for i in range(1, len(sorted_vect)):
        if (sorted_vect[i][0] > vect_min[0]):
            # comme liste est triée, pour le premier vecteur d'un c1 > vect_min[0]
            # si son c2 est > au c2_min, tous les autres le seront aussi
            # donc on peut passer au prochain c1
            vect_min = sorted_vect[i]
            # si un c2 est < vect_min[1] on garde ce c2 en tant que min
            # puis on cherche un autre c2 qui serait inférieur à ce min
            if sorted_vect[i][1] < c2_min:
                non_domines.append(sorted_vect[i])
                c2_min = vect_min[1]

    return non_domines

# v = tls.vector_factory(1000,20)
# non_domines = algo_tri_lex(v)
# tls.draw(v, non_domines)
# print("****Non dominés****")
# print(non_domines)


"""QUESTION 5"""

'''
Comparer les complexités des deux algorithmes proposés, et
vérifier expérimentalement votre analyse en traçant les courbes des temps
d'exécution respectifs des deux algorithmes en fonction de n, sur des ensembles
de vecteurs tirés aléatoirement à l'aide de la fonction de la question
2. Dans les expérimentations, le nombre de vecteurs variera de n = 200
à n = 10000 (par pas de 200 par exemple), et on prendra m = 1000. Pour
chaque valeur de n, on fera une moyenne du temps d'exécution sur 50 ensembles
tirés aléatoirement.
'''


def compare_naif_lex(nbr_experiment, start, end, step, m):
    l_n = []
    for n in range(start, end, step):
        # on va effectuer 50 expériences successives et stocker les résutats dans un vecteur
        l_50_exp = []
        print('running for : '+str(n)+' vectors')
        for j in range(nbr_experiment):
            # construction des vecteurs de points
            vectors = tls.vector_factory(n, m)
            # mesure du temps pour l'algo naif
            start_timer = timer()
            algo_naif(vectors)
            end_timer = timer()
            timer_naif = end_timer - start_timer
            # mesure du temps pour l'algo lex
            start_timer = timer()
            algo_tri_lex(vectors)
            end_timer = timer()
            timer_lex = end_timer - start_timer
            # sauvegarde
            l_50_exp.append([timer_naif, timer_lex])
        l_n.append(np.mean(l_50_exp, axis=0).tolist())

    plt.plot(list(range(start, end, step)), [item[0] for item in l_n], label="Algo. naif")
    plt.plot(list(range(start, end, step)), [item[1] for item in l_n], label="Algo. lexicographique")
    plt.legend(loc ='best')
    plt.xlabel('Nombre de vecteurs')
    plt.ylabel('Temps d\'execution')
    plt.title("Comparaison des temps d'execution")
    plt.show()
    return l_n


# compare_naif_lex(1, 200, 10001, 200, 1000)
