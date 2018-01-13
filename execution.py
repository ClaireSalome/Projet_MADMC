# -*- coding: utf-8 -*-
from tools import *
from algos import *
from proc1 import *
from proc2 import *
from compare_results import *

#generation des vecteurs
n = 50
v = vector_factory(n, 1000)
k = 10
I = [0.3,0.7]

"""""ALGORITHME NAIF"""""
#res = algo_naif(v)
#draw(v,res)


"""""ALGORITHME TRI LEXICOGRAPHIQUE"""""
#res =  algo_tri_lex(v)
#draw(v,res)


"""""COMPARAISON DES DEUX ALGORITHMES"""""
#compare_naif_lex(50, 200, 10001, 200, 1000)

 
"""""PREMIERE PROCEDURE DE RESOLUTION"""""
#minimax, P = first_proc(v,I,k)
#print(minimax)
#print(v)
#draw_minimax(v,P, minimax, I,k)


"""""SECONDE PROCEDURE DE RESOLUTION"""""
#minimax, P, I_domines = seconde_proc(v,I,k)
#print(minimax)
#print(v)
#draw_minimax(v, P, minimax, I, k, True)


"""AFFICHAGE COMPARE DES POINTS PARETO OPTIMAUX ET I OPTIMAUX"""
# minimax, P = first_proc(v,I,k)
# minimax, P_prime, I_domines = seconde_proc(v,I,k)
# print minimax
# draw_point_minimax(P, v, minimax, I, k, I_domines)


"""COMPARAISON DES ENSEMBLES I-OPT ET P-OPT POUR LES DIFFERENTS INTERVALLES CONSIDERES"""
# comparaison_I_P_opts(50, 10, 1000, 50)
# plot_comparaison(50, 10, 1000)

"""""COMPARAISON DES DEUX PROCEDURES DE RESOLUTION"""""
#comparaison_procedures(50, 10, 1000, 50)