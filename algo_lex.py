# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 17:10:15 2017

@author: clair
"""

"""QUESTION 4"""
#Proposer un second algorithme qui détermine les vecteurs nondominés
#en réalisant tout d'abord (1) un tri lexicographique des vecteurs,
#puis (2) un seul parcours de la liste obtenue pour identifier les vecteurs nondominés.
#Implémenter cet algorithme.

from tools import *
from copy import deepcopy


# tri_critere : le critere sur lequel on veut trier les vecteurs
def algo_tri_lex(vectors) :
    non_domines = []
    sorted_vect = deepcopy(vectors)
    sorted_vect.sort(key=lambda colonne : (colonne[0], colonne[1]))
    vect_min = sorted_vect[0]
    c2_min = vect_min[1]
    #Le min sur le critère est forcément non dominé
    non_domines.append(vect_min)
    #pour tous les autres critèrs avec c1 > vect_min[0]
    for i in range(1, len(sorted_vect)):
        if(sorted_vect[i][0] > vect_min[0]) :
            #comme liste est triée, pour le premier vecteur d'un c1 > vect_min[0]
            #si son c2 est > au c2_min, tous les autres le seront aussi
            # donc on peut passer au prochain c1 
            vect_min = sorted_vect[i]
            #si un c2 est < vect_min[1] on garde ce c2 en tant que min
            # puis on cherche un autre c2 qui serait inférieur à ce min
            if sorted_vect[i][1] < c2_min :
                non_domines.append(sorted_vect[i])
                c2_min = vect_min[1]
      
    return non_domines
    

#v = vector_factory(1000,20)
#sol = algo_tri_lex(v)
#draw(v, sol)  
#print("""""""")
#print(sol)
