# -*- coding: utf-8 -*-


"""QUESTION 5"""
#Comparer les complexités des deux algorithmes proposés, et
#vérifier expérimentalement votre analyse en traçant les courbes des temps
#d'exécution respectifs des deux algorithmes en fonction de n, sur des ensembles
#de vecteurs tirés aléatoirement à l'aide de la fonction de la question
#2. Dans les expérimentations, le nombre de vecteurs variera de n = 200
#à n = 10000 (par pas de 200 par exemple), et on prendra m = 1000. Pour
#chaque valeur de n, on fera une moyenne du temps d'exécution sur 50 ensembles
#tirés aléatoirement.

import tools as tls
from algo_lex import algo_tri_lex
from algo_naif_1 import algo_naif
from timeit import default_timer as timer
from matplotlib import pyplot as plt
import numpy as np

def compare_naif_lex(nbr_experiment, start, end, step, esperance):
    l_n = []
    for n in range(start, end, step):
        # on va effectuer 50 expériences successives et stocker les résutats dans un vecteur
        l_50_exp = []
        print('running for : '+str(n)+' vectors')
        for j in range(nbr_experiment):
            # construction des vecteurs de points
            vectors = tls.vector_factory(n, esperance)
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

    plt.plot(list(range(start, end, step)), [item[0] for item in l_n], label="Algo naif")
    plt.plot(list(range(start, end, step)), [item[1] for item in l_n], label="Algo lex")
    plt.legend(loc ='best')
    plt.xlabel('Nombre de vecteurs')
    plt.ylabel('Temps d\'execution')
    plt.title("Comparaison des temps d'execution")
    plt.show()
    return l_n


#compare_naif_lex(50, 200, 10001, 200, 1000)



