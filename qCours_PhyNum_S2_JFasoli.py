import numpy as np

def g(x, y):
    p = 15 #2e lettre alphabet de mon prénom : j_o_nathan
    d = 5 #chiffre des dizaines de mon numéro d'étudiant : 224111_5_2
    return np.sin(x)*np.sin(p*y) - np.tanh((d+x**2+y**2)/500)

#utilisation de g
n = 10  #1er lettre de mon prénom i.e. j
x = np.linspace(0, 30, 100*n)
y = np.linspace(0, 30, 100*n)
X, Y = np.meshgrid(x, y)
Z = g(X, Y)

#recherche du max de g
maxIndex = np.argmax(Z)
maxX, maxY = np.unravel_index(maxIndex, Z.shape)

print("Le maximum de g est atteint pour x =",x[maxX], "; y =", y[maxY])
