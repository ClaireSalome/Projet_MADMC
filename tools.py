# -*- coding: utf-8 -*-
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