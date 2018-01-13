# coding=utf-8
import proc1
import tools as tls
import numpy as np
import matplotlib.pyplot as plt

'''QUESTION 11'''

'''Implémenter cette approche pour permettre
la détermination des points non I-dominés.'''


def transformee(pi, interval):
    alpha_min = interval[0]
    alpha_max = interval[1]
    pi_prime = []
    for vecteur in pi:
        new_y1 = alpha_min * vecteur[0] + (1 - alpha_min) * vecteur[1]
        new_y2 = alpha_max * vecteur[0] + (1 - alpha_max) * vecteur[1]
        new_vect = [new_y1, new_y2]
        pi_prime.append(new_vect)
    return pi_prime


def transformee_inverse(pi_prime, interval):
    alpha_min = interval[0]
    alpha_max = interval[1]
    pi = []
    for vecteur in pi_prime:
        y1 = ((1 - alpha_max) * vecteur[0] - (1 - alpha_min) * vecteur[1]) / (alpha_min - alpha_max)
        y2 = (alpha_min * vecteur[1] - alpha_max * vecteur[0]) / (alpha_min - alpha_max)
        new_vect = [y1, y2]
        pi.append(new_vect)
    return pi


# seconde procedure de resolution
# parametres : vectors : l'ensemble des vecteurs ; I l'intervalle, et k le nombre d'objets
def seconde_proc(vectors, interval, k):
    # transformation des vecteurs du pb de I-dominance vers le pb de Pareto-dominance
    p_vectors = transformee(vectors, interval)
    # programmation dynamique sur la transformee
    p = proc1.prog_dyn(p_vectors, k)
    pareto_opt = p[k][len(vectors)-1]
    # transformee inverse pour avoir les non I-domines
    i_opt = transformee_inverse(pareto_opt, interval)
    # calcul du minimax
    y = proc1.minimax(i_opt, interval)
    return y , p

# # Test de la programmation dynamique du cours
# f = [[1,4],[2,3],[5,2],[2,2],[3,1],[2,5],[3,4]]
# print(seconde_proc(f, [0,1], 3))
#v = tls.vector_factory(50,30)
#print("PREMIERE")
#y = proc1.first_proc(v,[0,1],10)
#print(y)
#print("SECONDE")
#y = seconde_proc(v,[0,1],10)
#print(y)

#affichage pour le minimax
def draw_minimax(vectors,P, minimax, I, k, second = False):
    legend = True
    #si c'est la seconde procédure
    if second :
        sol=[]
    else:
        sol = proc1.backward_prog_dyn(P, minimax, vectors, [])
    print('sol')
    print(sol)
    for i in range(len(vectors)):
        if vectors[i] in sol :
            if legend :
                plt.plot(vectors[i][0], vectors[i][1], 'ro', label="solution minimax")
                legend = False
            else:
                plt.plot(vectors[i][0], vectors[i][1], 'ro')
        else :
            plt.plot(vectors[i][0], vectors[i][1], 'bo')
    
    plt.title("Affichage des vecteurs et de la solution minimax")
    plt.xlabel('y1')
    plt.ylabel('y2')
    plt.legend(loc='best')
    plt.show()