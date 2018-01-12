
# coding=utf-8
import tools as tls
from timeit import default_timer as timer
import numpy as np
from matplotlib import pyplot as plt
from proc1 import first_proc
from proc2 import seconde_proc

'''QUESTION 12'''

'''Comparer expérimentalement la première et la seconde proc
édure de résolution en traçant les courbes des temps d'exécution respectifs
des deux procédures en fonction de max 􀀀 min, sur des ensembles de vecteurs
tirés aléatoirement à l'aide de la fonction de la question 2. Dans les
expérimentations, on xera n = 50, k = 10 et m = 1000. On considérera les
intervalles I_epsilon= [0.5 - epsilon ; 0.5 + epsilon] en faisant varier epsilon de 0.025 à 0.5 (par pas
de 0.025 par exemple). Pour chaque intervalle I_epsilon, on fera une moyenne du
temps d'exécution sur 50 instances tirées aléatoirement.'''


def comparaison_procedures(n, k, m, nbr_tests):
    # pour chaque interval
    results = []
    for epsilon in np.arange(0.025, 0.51, 0.025):
        i_epsilon = [0.5 - epsilon, 0.5 + epsilon]
        print("run for intervalle : [0.5-" + str(epsilon) + ", 0.5+" + str(epsilon) + "]")
        results_test = []
        for test in range(nbr_tests):
            # construction des vecteurs de points
            vectors = tls.vector_factory(n, m)

            # mesure du temps pour la procedure 1
            start_timer = timer()

            first_proc(vectors, i_epsilon, k)
            end_timer = timer()
            timer_proc1 = end_timer - start_timer

            # mesure du temps pour la procedure 2
            start_timer = timer()
            seconde_proc(vectors, i_epsilon, k)
            end_timer = timer()
            timer_proc2 = end_timer - start_timer

            # sauvegarde
            results_test.append([timer_proc1, timer_proc2])

        results.append(np.mean(results_test, axis=0).tolist())

    plt.plot(list(np.arange(0.025, 0.51, 0.025)), [item[0] for item in results], label="Procedure 1")
    plt.plot(list(np.arange(0.025, 0.51, 0.025)), [item[1] for item in results], label="Procedure 2")
    plt.legend(loc='best')
    plt.xlabel('Epsilon')
    plt.ylabel('Temps d\'execution')
    plt.title("Comparaison des temps d'execution")
    plt.show()
    return results


comparaison_procedures(1, 10, 1000, 50)
