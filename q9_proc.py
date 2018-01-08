import q7_prog_dyn as q7
import q8

def proc(k,n,f):
    # f est le vecteur cout de chaque objet dans l'espace des obj
    P = q7.prog_dyn(k,n,f)
    pareto_opt = P[k][n-1]
    y = q8.minimax(pareto_opt,[0,1])
    return y

# # Teste de la programmation dynamique du cours
f = [[1,4],[2,3],[5,2],[2,2],[3,1],[2,5],[3,4]]
print(proc(3, 7, f))