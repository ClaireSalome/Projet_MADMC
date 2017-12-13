# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 11:54:06 2017

@author: clair
"""

import numpy as np
import matplotlib.pyplot as plt

"""QUESTION 2"""
#Implémenter une fonction qui génère un ensemble de n vecteurs
#où chaque composante est tirée aléatoirement selon une loi normale
#d'espérance m et d'écart-type m/4.

def vector_factory( n, esperance) :
    l = []
    for i in range(n) :
        vector = [np.random.normal(esperance, esperance/4.),
                  np.random.normal(esperance, esperance/4.)]
        l.append(vector)
    return l
    
    
#affichage graphique des points
def draw(data, non_domines) :
    color= 'bo'
    label = ''
    for i in range(len(data)) :
        if data[i] in non_domines :
            color = 'ro'
            label="non_domines"
        else :
            color = 'bo'
            label=''
        plt.plot(data[i][0], data[i][1], color, label=label)
        
    plt.title("Affichage des vecteurs")
    #plt.legend(loc='best')
    plt.show()
    