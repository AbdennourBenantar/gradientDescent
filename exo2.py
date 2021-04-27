
### BENANTAR ABDENOUR SIT1 MODULE : BDM 2020-2021
### CALCUL DE LA DESCENTE DE GRADIENT ET DES BIAIS ET DES INTERCEPTS JUSQU'A LA CONVERGENCE DU COUT CALCULé CHAQUE ITéRATION

import numpy as np
import random
import matplotlib.pyplot as plt

c=np.zeros(7000)
iz=np.zeros(7000)
def descente_du_gradient(x, y, p, alpha, m):
    
    xT = x.transpose()  # on calcule la transposé de X pour effectuer le produit matriciel plutard
    i=0 # compteur d'iterations
    cout=0 # cout de chaque itération
    while True:
        h = np.dot(x, p)   #calcule de h(x) de cette itération (avec ses p0 et p1)
        err = h - y    #calcule de l"erreur
        # on verifie si le cout converge on s'arrete
        if (np.sum(err ** 2) / (2 * m))==cout:
            cout = np.sum(err ** 2) / (2 * m)
            print("Itération n° %d pour un Cout de : %f" % (i, cout))
            gradient = np.dot(xT, err) / m
            p = p - alpha * gradient
            print(p)
            break
        #sinon on calcule le cout
        cout = np.sum(err ** 2) / (2 * m)
        print("Itération n° %d avec un Cout de : %f" % (i, cout))
        # calcule du gradient descendant
        gradient = np.dot(xT, err) / m
        # mise à jour de p0 et p1
        p = p - alpha * gradient
        print(p)
        c[i]=cout
        iz[i]=i
        i=i+1 #iteration suivante
        
        
        
    return p,c,iz


x = np.zeros(shape=(3, 2))
y = np.zeros(shape=3)
x[0][0] = 1
x[0][1] = 1
x[1][0] = 1
x[1][1] = 2
x[2][0] = 1
x[2][1] = 4
y[0]=2
y[1]=1
y[2]=5
m=3
alpha = 0.01
p = np.zeros(2)
print(p)
p,c,iz = descente_du_gradient(x, y, p,alpha, m)
plt.plot(iz,c)
plt.title('Dernier modèle (version de p0 et p1) aprés convergence')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(left=0)
plt.show()

