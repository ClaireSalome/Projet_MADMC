# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 12:13:19 2017

@author: clair
"""

"""QUESTION 3"""
#Proposer un premier algorithme naïf pour déterminer les vecteurs
#non-dominés, qui procède avec des comparaisons par paires systématiques.
#Implémenter cet algorithme.


from tools import *
from copy import deepcopy

def algo_naif(vectors) :
    
    non_domines = deepcopy(vectors)
    print("****Vecteurs à comparer****")
    print(non_domines)
    #comparaison par paires
    for i in range( len(vectors) ) :
        #on vérifie que le vecteur est toujours candidat à la non-dominance
        if vectors[i] in non_domines :
            dominated = False
            for j in range(i+1, len(vectors) ):
                if vectors[j] in non_domines :
                    #si 1er < 2eme, 2eme dominé, on le retire de la liste
                    if (vectors[i][0]<= vectors[j][0]) and (vectors[i][1] <= vectors[j][1]):
                        print("Vecteur ",vectors[i], "domine ", vectors[j])                        
                        non_domines.remove(vectors[j])
                        continue
                    #si 2eme < 1er, 1er dominé
                    if (vectors[j][0]<= vectors[i][0]) and (vectors[j][1] <= vectors[i][1]):
                        print("Vecteur ",vectors[j], "domine ", vectors[i])                        
                        dominated = True
                        break
            if dominated == True :
                non_domines.remove(vectors[i])
    return non_domines
            
            
v = vector_factory(60, 3.8)
non_domines = algo_naif(v)
print("****Non dominés****")
print(non_domines)
draw(v,non_domines)