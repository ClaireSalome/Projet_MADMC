# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import proc1
import proc2

"""QUESTION 2"""

'''Implémenter une fonction qui génère un ensemble de n vecteurs 
où chaque composante est tirée aléatoirement selon une loi normale
d'espérance m et d'écart-type m/4.'''

def vector_factory(n, esperance):
#np.random.seed(1)
    l = []
    for i in range(n):
        vector = [int(np.random.normal(esperance, esperance / 4.)),
                  int(np.random.normal(esperance, esperance / 4.))]
        l.append(vector)
    return l

    
    
#affichage graphique des points
def draw(data, non_domines) :
    color= 'bo'
    #pour la legende
    first_blue = True
    first_red = True
    
    for i in range(len(data)) :
 
        if data[i] in non_domines :
            color = 'ro'
            if first_red == True :
                first_red = False
                plt.plot(data[i][0], data[i][1], color, label="non-dominé")
                continue 
        else :
            color = 'bo'
            if first_blue == True :
                first_blue = False
                plt.plot(data[i][0], data[i][1], color, label="dominé")
                continue
            
        plt.plot(data[i][0], data[i][1], color)
        
    plt.title("Affichage des vecteurs")
    plt.xlabel('y1')
    plt.ylabel('y2')
    plt.legend(loc='best')

    plt.show()

# Fonction qui permet de tester l'égalité de deux vecteurs de floats très proches
def approximatively_equals(vector1, vector2, precision = 0.00001):
    test = False
    if abs(vector1[0]-vector2[0])<precision and abs(vector1[1]-vector2[1])<precision:
        test = True
    return test

# Fonction qui permet de tester si un vecteur est contenu dans une liste avec un degré d'approximation
def approximatively_in(vector1, list):
    test = False
    for element in list :
        if approximatively_equals(vector1, element):
            test = True
            break
    return test


#affichage pour le minimax
def draw_minimax(vectors,P, minimax, I, k, second = False):
    legend = True
    #si c'est la seconde procédure
    if second :
        # On calcule l'équivalent dans ∏' du point minimax
        minimax_prime = proc2.transformee([minimax], I)
        # On calcule l'équivalent dans ∏' des vecteurs objets
        vecteurs_prime = proc2.transformee(vectors, I)
        # On fait la programmation dynamique arrière dans ∏'
        sol = proc1.backward_prog_dyn(P, minimax_prime[0], vecteurs_prime, [])
        # On ramène le résultat dans ∏
        sol = proc2.transformee_inverse(sol, I)
    else:
        sol = proc1.backward_prog_dyn(P, minimax, vectors, [])
    for i in range(len(vectors)):
        if vectors[i] in sol :
            if legend :
                plt.plot(vectors[i][0], vectors[i][1], 'ro', label="solution minimax")
                legend = False
            else:
                plt.plot(vectors[i][0], vectors[i][1], 'ro')
        else:
            plt.plot(vectors[i][0], vectors[i][1], 'bo')
    if second:
        plt.title(u"Affichage des objets consituant la solution minimax - procédure 2")
    else :
        plt.title(u"Affichage des objets consituant la solution minimax - procédure 1")
    plt.xlabel('critere 1')
    plt.ylabel('critere 2')
    plt.legend(loc='best')
    plt.show()

#affichage pour le point minimax, les points I-opts et les points I-P
def draw_point_minimax(P, vectors, minimax, I, k, I_domines =[]):
    for i, point in enumerate(P[k][len(vectors)-1]):
        if point == minimax:
            plt_minimax, = plt.plot(point[0], point[1], 'ro')
        elif point in I_domines:
            plt_I_opt, = plt.plot(point[0], point[1], 'go')
        else:
            plt_P_opt, = plt.plot(point[0], point[1], 'bo')
    plt.legend([plt_minimax, plt_I_opt, plt_P_opt], ["Point minimax", "Non I-domines", "Pareto-optimaux"],loc='best')
    plt.title(u"Affichage du point minimax, des points I-Opt et P-Opt")
    plt.xlabel('y1')
    plt.ylabel('y2')
    plt.show()

