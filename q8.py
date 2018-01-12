import numpy as np

def minimax(ensemble, intervalle):
    val_minimax = np.inf
    y_minimax = None
    for vecteur in ensemble:
        if vecteur[0]>vecteur[1]:
            alpha_0 = intervalle[1]
        else :
            alpha_0 = intervalle[0]
        val_max = alpha_0*vecteur[0]+(1-alpha_0)*vecteur[1]
        if val_max < val_minimax:
            val_minimax = val_max
            y_minimax = vecteur
    return y_minimax