import random
import math

#Question 1
def f(x,y,z):
    if z < 0 or z > h: #point au-dessus/en-dessous du cone
        return 0
    if x**2 + y**2 <= c**2 * (h - z)**2: #dans le cone
        return 1
    else: #autres cas en dehors
        return 0

#Tests question 1
#valeurs numériques arbitraires fixees
r = 10
h = 10
c = r / h

print("Tests question 1 :")
print(f(50, 0, 2) == 1) #point en dehors (renvoie false)
print(f(5, 2, 1) == 1) #point dedans (renvoie true)
print(f(0, 0, 10) == 1) #point au sommet du cone (renvoie true)


#Question 2

def volume(N):
    volumeCylindre = math.pi * r**2 * h

    #Compteur pour les points dans le cone
    compteurPointsDansCone = 0

    for i in range(N):
        #Generation points aleatoires dans le cylindre
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        z = random.uniform(0, h)

        # point dans cone ?
        if f(x, y, z) == 1:
            compteurPointsDansCone += 1

    volumeCone = volumeCylindre * (compteurPointsDansCone / N)
    return volumeCone


print("Tests question 2 :")
volumeTheorique = (1/3)*math.pi*(r**2)*h
print("Volume théorique :", volumeTheorique)
for k in [1000,100000,1000000]:
    print("Estimation volume : ",volume(k))
#Remarque sur les résultats : volume proche mais inférieur au volume théorique