# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 12:34:39 2024

@author: leona
"""

import numpy as np
import math
from scipy.spatial.transform import Rotation as R

'''
v1 = np.array([1, 0, -1])
v2 = np.array([1, -1, -1])
v3 = np.array([1, -1, -1])

u1 = np.array([1, 0, -1])
u2 = np.array([1, -1, -1])
u3 = np.array([1, -1, -1])
'''


#DEFINITION REPERES
#définition repère 1
repere1 = [
    np.array([1, 0, 0]),  # vecteur x1
    np.array([0, 1, 0]),  # vecteur y1
    np.array([0, 0, 1])   # vecteur z1
]


#définition repère 2
repere2 = [
    np.array([1, 1, 2]),  # vecteur x2
    np.array([1, 3, 0]),  # vecteur y2
    np.array([0, 0, 4])   # vecteur z2
]





#CALCUL VECTEURS UNITAIRES
def vecteur_unitaire(v):
    # Calcul de la norme du vecteur
    norme_v = np.linalg.norm(v)
    
    # Si la norme est non nulle, calcul du vecteur unitaire
    if norme_v != 0:
        return v / norme_v
    else:
        raise ValueError("La norme du vecteur est nulle, impossible de calculer le vecteur unitaire.")


# Liste qui contiendra les vecteurs unitaires
vecteurs_unitaires = []

# Boucle sur les deux repères
for repere in [repere1, repere2]:
    for vecteur in repere:
        vecteur_unit = vecteur_unitaire(vecteur)
        vecteurs_unitaires.append(vecteur_unit)


# Affichage des vecteurs unitaires
#for i, vecteur in enumerate(vecteurs_unitaires):
#    print(f"Vecteur unitaire {i + 1} : {vecteur}")




# Créer deux nouvelles listes pour stocker les vecteurs unitaires des deux repères
repere1_unitaires = []
repere2_unitaires = []

# Calcul des vecteurs unitaires pour le repère 1
for vecteur in repere1:
    vecteur_unit = vecteur_unitaire(vecteur)
    repere1_unitaires.append(vecteur_unit)

# Calcul des vecteurs unitaires pour le repère 2
for vecteur in repere2:
    vecteur_unit = vecteur_unitaire(vecteur)
    repere2_unitaires.append(vecteur_unit)

# Affichage des vecteurs unitaires pour chaque repère
print("Vecteurs unitaires du repère 1 :")
for vecteur in repere1_unitaires:
    print(vecteur)

print("\nVecteurs unitaires du repère 2 :")
for vecteur in repere2_unitaires:
    print(vecteur)




#GENERATION MATRICE DE ROTATION ET CALCUL DES ANGLES D'EULER
def calcul_matrice_rotation(repere1, repere2):
    # Matrice de rotation du repère1 vers repère2
    # La matrice de rotation se construit avec les vecteurs unitaires de chaque repère comme colonnes
    R1 = np.column_stack(repere1)  # Matrice formée des vecteurs de repère1
    R2 = np.column_stack(repere2)  # Matrice formée des vecteurs de repère2
    
    # Matrice de rotation qui transforme repère1 en repère2
    R_matrix = R2 @ np.linalg.inv(R1)
    
    # Décomposition en angles d'Euler (Y-X-Y)
    r = R.from_matrix(R_matrix)
    angles_euler = r.as_euler('yxy', degrees=True)  # Y-X-Y en degrés
    
    return R_matrix, angles_euler


# Calcul de la matrice de rotation et des angles d'Euler
R_matrix, angles_euler = calcul_matrice_rotation(repere1_unitaires, repere2_unitaires)

# Affichage des résultats
print("\nMatrice de rotation R :\n", R_matrix)
print("\nAngles d'Euler (Y-X-Y) :\n", angles_euler)








