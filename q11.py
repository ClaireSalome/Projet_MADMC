import q7 as q7
import q8
import q9
import tools

def transformee(pi, I):
    alpha_min = I[0]
    alpha_max = I[1]
    pi_prime = []
    for vecteur in pi :
        new_y1 = alpha_min * vecteur[0] + (1 - alpha_min) * vecteur[1]
        new_y2 = alpha_max * vecteur[0] + (1 - alpha_max) * vecteur[1]
        new_vect = [new_y1,new_y2]
        pi_prime.append(new_vect)
    return(pi_prime)

def transformee_inverse(pi_prime, I):
    alpha_min = I[0]
    alpha_max = I[1]
    pi = []
    for vecteur in pi_prime :
        y1 = ((1-alpha_max) * vecteur[0] - (1 - alpha_min) * vecteur[1])/(alpha_min-alpha_max)
        y2 = (alpha_min * vecteur[1]- alpha_max * vecteur[0])/(alpha_min-alpha_max)
        new_vect = [y1,y2]
        pi.append(new_vect)
    return(pi)

#seconde procedure de resolution
#parametres : I_vectors : l'ensemble des vecteurs ; I l'intervalle, et k le nombre d'objets
def seconde_proc(I_vectors, I, k):
    #transformation des vecteurs du pb de I-dominance vers le pb de Pareto-dominance
    P_vectors = transformee(I_vectors,I)
    #programmation dynamique sur la transformee
    P = q7.prog_dyn(P_vectors, k)
    #recuperation des vecteurs Pareto-optimaux
    pareto_opt = P[k][len(P_vectors)-1]
    #transformee inverse pour avoir les non I-domines
    I_opt = transformee_inverse(pareto_opt, I)
    #calcul du minimax
    y = q8.minimax(I_opt,I)
    return y



# # Test de la programmation dynamique du cours
#f = [[1,4],[2,3],[5,2],[2,2],[3,1],[2,5],[3,4]]
#print(seconde_proc(f, [0,1], 3))
# v = tools.vector_factory(50,30)
# print("PREMIERE")
# y = q9.first_proc(v,[0,1],10)
# print(y)
# print("SECONDE")
# y = seconde_proc(v,[0,1],10)
# print(y)
