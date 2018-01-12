from algo_lex import algo_tri_lex
import itertools

def prog_dyn(k,n,f):
    P = [[[] for i in range(n)] for j in range(k+1)]
    # initialisation :
    for j in range(k+1):
        for i in range(n):
            if j==0:
                P[0][i].append([0, 0])
            elif i==0:
                if j == 1:
                    P[j][i].append(f[i])
            elif j > i+1:
                    P[j][i] = []
            else :
                nouvel_ens_1 = []
                for e, element in enumerate(P[j - 1][i - 1]):
                    nouvel_ens_1.append([x + y for (x, y) in zip(element, f[i])])
                nouvel_ens_2=P[j][i-1]
                nouvel_ens = nouvel_ens_1 + nouvel_ens_2
                # supprimer les doublons
                nouvel_ens.sort()
                nouvel_ens = list(nouvel_ens for nouvel_ens, _ in itertools.groupby(nouvel_ens))
                P[j][i] = algo_tri_lex(nouvel_ens)
    return P

# # Teste de la programmation dynamique du cours
#f = [[1,4],[2,3],[5,2],[2,2],[3,1],[2,5],[3,4]]
#P = prog_dyn(3, 7, f)
#print(P)
#print(P[3][6])
