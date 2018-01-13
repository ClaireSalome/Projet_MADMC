# coding=utf-8
import itertools
import numpy as np
import matplotlib.pyplot as plt
from algos import algo_tri_lex
import copy
import tools as tls

'''QUESTION 7'''

'''Implémenter la procédure de programmation dynamique en utilisant
la fonction de la question 4 pour déterminer les points non-dominés en
chaque case du tableau de programmation dynamique'''


def prog_dyn(vecteurs, k):
    n = len(vecteurs)
    p = [[[] for i in range(n)] for j in range(k + 1)]
    # initialisation :
    for j in range(k + 1):
        for i in range(n):
            # print('i = '+str(i)+' , j = '+str(j))
            if j == 0:
                p[0][i].append([0, 0])
            elif i == 0:
                if j == 1:
                    p[j][i].append(vecteurs[i])
            elif j > i + 1:
                p[j][i] = []
            else:
                nouvel_ens_1 = []
                for e, element in enumerate(p[j - 1][i - 1]):
                    #print([x + y for (x, y) in zip(element, vecteurs[i])])
                    nouvel_ens_1.append([x + y for (x, y) in zip(element, vecteurs[i])])
                nouvel_ens_2 = p[j][i - 1]
                nouvel_ens = nouvel_ens_1 + nouvel_ens_2
                # supprimer les doublons
                nouvel_ens.sort()
                nouvel_ens = list(nouvel_ens for nouvel_ens, _ in itertools.groupby(nouvel_ens))
                p[j][i] = algo_tri_lex(nouvel_ens)
            # print(P[j][i])
    return p#[k][len(vecteurs)-1]


# # # Teste de la programmation dynamique du cours
#f = [[1,4],[2,3],[5,2],[2,2],[3,1],[2,5],[3,4]]
#p = prog_dyn(f,3)
#print(p)
#print(p[3][6])


def backward_prog_dyn(p, vector, vecteurs, liste_sols):
    p = np.array(p)
    # verifier que vector est bien dans la dernière case.
    sol = copy.deepcopy(liste_sols)
    test_end = False
    if tls.approximatively_in(vector, p[len(p)-1][len(p[0])-1]):
        test_ligne = True
        i = len(p[0])-1
        while test_ligne is True and i != -1:
            # on teste s'il est dans la case de gauche
            if not tls.approximatively_in(vector, p[len(p)-1][i-1]): # si non, on va interrompre la boucle
                test_ligne = False
            else : # si oui, on continue en passant à la case de gauche
                i = i -1
        if i == -1 :
            sol.append(vecteurs[i+1])
        else :
            # en sortie de la boucle on a le i de la case la plus à gauche ou on retrouve le point.
            # il faut remonter d'une ligne dans le tableau, on en deduit un premier point
            sol.append(vecteurs[i])
            # on calcul le nouveau vecteur :
            new_vect = [x - y for x, y in zip(vector, vecteurs[i])]
            if not tls.approximatively_equals(new_vect, [0,0]):
                # on recommence avec
                sol = (backward_prog_dyn(p[:len(p)-1, :i], new_vect, vecteurs, sol))
    return sol

#p = prog_dyn(f,3)
#print(p[3][6])
#print(backward_prog_dyn(p,[5,9],f,[]))
#for i in range(len(p[3][len(f)-1])):
#    print(backward_prog_dyn(p,p[3][len(f)-1][i],f,[]))

'''QUESTION 8'''

'''En déduire un algorithme pour
déterminer un vecteur minimax dans un ensemble de vecteurs (en dimension
2). Implémenter cet algorithme'''


def minimax(vectors, interval):
    val_minimax = np.inf
    y_minimax = None
    for vecteur in vectors:
        if vecteur[0] > vecteur[1]:
            alpha_0 = interval[1]
        else:
            alpha_0 = interval[0]
        val_max = alpha_0 * vecteur[0] + (1 - alpha_0) * vecteur[1]
        if val_max < val_minimax:
            val_minimax = val_max
            y_minimax = vecteur
    return y_minimax


'''QUESTION 9'''

'''Utiliser les fonctions implémentées dans les question 7 et 8
pour implémenter la procédure en deux temps décrite plus haut.'''


def first_proc(vectors, interval, k):
    # f est le vecteur cout de chaque objet dans l'espace des obj
    P = prog_dyn(vectors, k)
#    print(pareto_opt)
    pareto_opt = P[k][len(vectors)-1]
    y = minimax(pareto_opt, interval)
    return y, P

# # Teste de la programmation dynamique du cours
# f = [[1,4],[2,3],[5,2],[2,2],[3,1],[2,5],[3,4]]
#print(first_proc(f, [0,1], 3))