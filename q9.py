import q7
import q8

def first_proc(vectors, interval, k):
    # f est le vecteur cout de chaque objet dans l'espace des obj
    P = q7.prog_dyn(vectors,k)
    n = len(vectors)
    pareto_opt = P[k][n-1]
    #print(pareto_opt)
    y = q8.minimax(pareto_opt,interval)
    return y

# # Teste de la programmation dynamique du cours
#f = [[1,4],[2,3],[5,2],[2,2],[3,1],[2,5],[3,4]]
#print(proc(3, 7, f))