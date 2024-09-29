import numpy as np

#ma date de naissance : 25/01/2004
c = [2, 5, 0, 1, 2, 0, 0, 4]

M = np.zeros((8, 8))

#remplissage de la matrice M selon règles de l'énoncé
for i in range(8):
    M[0, 0] += 1 / (1 + c[0])
    M[i, 0] += 1 / (i + 1 + c[i])
    M[0, i] += 1 / (i + 1 + c[i])
    M[i, i] += 1 / (i + 1 + c[i]) #remarque : puisque i commence à 0 on rajoute 1

#caklcul des valeurs propres
valeursPropres = np.linalg.eigvals(M)

sortedValeursPropres = np.sort(valeursPropres)

differences = np.diff(sortedValeursPropres)

print("Valeurs propres rangées : ", sortedValeursPropres)
print("Différences entre les valeurs propres successives : ", differences)
