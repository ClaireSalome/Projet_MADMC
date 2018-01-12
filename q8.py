import numpy as np

def minimax(ensemble, intervalle):
    val_minimax = np.inf
    y_minimax = None
    for vecteur in ensemble:
        #si y1 > y2, la valeur maximale est atteinte pour alpha_max
        if vecteur[0]>vecteur[1]:
            alpha_0 = intervalle[1]
        else :
            #si y1 <= y2, la valeur maximale est atteinte pour alpha_min
            alpha_0 = intervalle[0]
        val_max = alpha_0*vecteur[0]+(1-alpha_0)*vecteur[1]
        if val_max < val_minimax:
            val_minimax = val_max
            y_minimax = vecteur
    return y_minimax