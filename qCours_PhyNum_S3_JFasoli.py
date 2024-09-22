import numpy as np
import matplotlib.pyplot as plt

p = len("Jonathan")
d = 5 #chiffre des dizaines de mon n° d'étudiant

angle = np.pi/(p + d)
M = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])

k = np.arange(0, p+d) #pour générer les différents angles entre 0 et 2pi de la forme k*2pi/(p+d)
angles = k*2*np.pi/(p+d)
x = np.cos(angles)
y = np.sin(angles)

coord_sommets = np.vstack((x, y)).T
print(coord_sommets)
v = coord_sommets[-1] #dernier point du cercle

M_inv = np.linalg.inv(M)

# M @ u = v  d'où  u = M_inv @ v
u = M_inv @ v

print("Vecteur u:", u)

segments = np.array([[i, i + 1] for i in range(p - 1)]).T
print(segments)

coord_rota = coord_sommets @ M.T
plt.close()
plt.figure(figsize=(6, 6))

# tracé des points de base
for i in range(p):
    plt.plot(coord_sommets[i, 0], coord_sommets[i, 1], 'bo')
    plt.text(coord_sommets[i, 0], coord_sommets[i, 1], f'{i}', fontsize=12, color='blue')

for i in range(p):
    plt.plot(coord_rota[i, 0], coord_rota[i, 1], 'ro')
    plt.text(coord_rota[i, 0], coord_rota[i, 1], f'{i}', fontsize=12, color='red')

for i in range(p - 1):
    # relier points de base
    plt.plot([coord_sommets[segments[0, i], 0], coord_sommets[segments[1, i], 0]],
             [coord_sommets[segments[0, i], 1], coord_sommets[segments[1, i], 1]], 'b--')

    # relier points après rota
    plt.plot([coord_rota[segments[0, i], 0], coord_rota[segments[1, i], 0]],
             [coord_rota[segments[0, i], 1], coord_rota[segments[1, i], 1]], 'r-')

plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])

plt.title("Rotation des points (en rouge) par rapport aux points originaux (en bleu)")
plt.show()
