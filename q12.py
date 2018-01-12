import q11
import q9
import tools as tls
from timeit import default_timer as timer
import numpy as np
from matplotlib import pyplot as plt

def comparaison_procedures(n, k, m, nbr_tests):
    # pour chaque interval
    results = []
    for epsilon in np.arange(0.025, 0.51, 0.025):
        I_epsilon = [0.5 - epsilon, 0.5 + epsilon]
        print("run for intervalle : [0.5-"+str(epsilon)+", 0.5+"+str(epsilon)+"]")
        results_test = []
        for test in range(nbr_tests):
            # construction des vecteurs de points
            vectors = tls.vector_factory(n, m)

            # mesure du temps pour la procedure 1
            start_timer = timer()
            q9.first_proc(vectors, I_epsilon, k)
            end_timer = timer()
            timer_proc1 = end_timer - start_timer

            # mesure du temps pour la procedure 2
            start_timer = timer()
            q11.seconde_proc(vectors, I_epsilon, k)
            end_timer = timer()
            timer_proc2 = end_timer - start_timer

            # sauvegarde
            results_test.append([timer_proc1, timer_proc2])

        results.append(np.mean(results_test, axis=0).tolist())

    plt.plot(list(np.arange(0.025, 0.51, 0.025)), [item[0] for item in results], label="Procedure 1")
    plt.plot(list(np.arange(0.025, 0.51, 0.025)), [item[1] for item in results], label="Procedure 2")
    plt.legend(loc ='best')
    plt.xlabel('Epsilon')
    plt.ylabel('Temps d\'execution')
    plt.title("Comparaison des temps d'execution")
    plt.show()
    return results

comparaison_procedures(50, 10, 1000, 50)