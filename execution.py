# -*- coding: utf-8 -*-
from tools import *
from algo_naif_1 import *
from algo_lex import *
from comparaison_naif_lex import *
from q9_proc import *
from q11 import *

#generation des vecteurs
v = vector_factory(500, 20)
k = 10
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
#minimax = proc(k,len(v),v)
#draw_minimax(v,minimax)


"""""SECONDE PROCEDURE DE RESOLUTION"""""
#minimax = seconde_proc(v,I,k)
#draw_minimax(v,minimax)


"""""COMPARAISON DES DEUX PROCEDURES DE RESOLUTION"""""