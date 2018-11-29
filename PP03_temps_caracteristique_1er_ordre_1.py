# pour l'import des donnees
import numpy as np
# La lecture proprement dite
t1,u1,t2,u2 = np.loadtxt('regime_transi2.txt',unpack=True)

# Au cas ou vous auriez besoin de l'exponentielle
from math import exp

# t1 et t2 ne commencent pas a t=0, mais commencent au debut de la zone 
# interessante pour le regime transitoire. A vous d'en tirer profit pour faire 
# une fonction qui permettent d'obtenir une bonne estimation de la valeur de 
# tau (il y a plusieurs methodes possibles)




# Appliquez la fonction precedemment definie pour trouver les temps 
# caracteristiques des deux enregistrements

tau1 = 'Resultat pour (t1,u1)'
tau2 = 'Resultat pour (t2,u2)'

# On affiche les resultats
print(tau1,tau2)
