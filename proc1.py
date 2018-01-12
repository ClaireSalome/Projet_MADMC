# coding=utf-8
import itertools
import numpy as np
from algos import algo_tri_lex

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
                    nouvel_ens_1.append([x + y for (x, y) in zip(element, vecteurs[i])])
                nouvel_ens_2 = p[j][i - 1]
                nouvel_ens = nouvel_ens_1 + nouvel_ens_2
                # supprimer les doublons
                nouvel_ens.sort()
                nouvel_ens = list(nouvel_ens for nouvel_ens, _ in itertools.groupby(nouvel_ens))
                p[j][i] = algo_tri_lex(nouvel_ens)
            # print(P[j][i])
    return p[k][len(vecteurs)-1]


# # # Teste de la programmation dynamique du cours
# f = [[1,4],[2,3],[5,2],[2,2],[3,1],[2,5],[3,4]]
# p = prog_dyn(f,3)
# print(p)


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
    pareto_opt = prog_dyn(vectors, k)
    # print(pareto_opt)
    y = minimax(pareto_opt, interval)
    return y

# # Teste de la programmation dynamique du cours
# f = [[1,4],[2,3],[5,2],[2,2],[3,1],[2,5],[3,4]]
# print(first_proc(f, [0,1], 3))
