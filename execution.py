# -*- coding: utf-8 -*-
from tools import *
from algos import *
from proc1 import *
from proc2 import *
from compare_results import *

#generation des vecteurs
v = vector_factory(20, 20)
k = 1
I = [0,1]

"""""ALGORITHME NAIF"""""
#res = algo_naif(v)
#draw(v,res) 


"""""ALGORITHME TRI LEXICOGRAPHIQUE"""""
#res =  algo_tri_lex(v)
#draw(v,res) 


"""""COMPARAISON DES DEUX ALGORITHMES"""""
#compare_naif_lex(50, 200, 10001, 200, 1000)

 
"""""PREMIERE PROCEDURE DE RESOLUTION"""""
minimax, P = first_proc(v,I,k)
print(minimax)
draw_minimax(v,P, minimax, I,k)
print(v)


"""""SECONDE PROCEDURE DE RESOLUTION"""""
minimax, P = seconde_proc(v,I,k)
print(minimax)
draw_minimax(v, P, minimax, I, k, True)


"""""COMPARAISON DES DEUX PROCEDURES DE RESOLUTION"""""
#comparaison_procedures(50, 10, 1000, 50)