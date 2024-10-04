# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 11:37:40 2024

@author: leona
"""

import numpy as np



#Calcul repères

def point_milieu(A, B):
    # Calculer la moyenne des coordonnées x, y, z des deux points
    M_x = (A[0] + B[0]) / 2
    M_y = (A[1] + B[1]) / 2
    M_z = (A[2] + B[2]) / 2
    
    return [M_x, M_y, M_z]





def calcul_vect_repeteTHORAX(IJ, C7, PX, T8):
    # Convertir les points en numpy arrays pour calculer facilement les vecteurs
    IJ = np.array(IJ)
    C7 = np.array(C7)
    PX = np.array(PX)
    T8 = np.array(T8)
    
    # Calcul des vecteurs
    M1 = point_milieu(IJ, C7)
    M2 = point_milieu(PX, T8)
    M1 = np.array(M1)
    M2 = np.array(M2)
    
    yt = M1-M2

    u = C7-IJ
    v = M2-IJ

    zt = np.cross(u, v)
    xt = np.cross(yt, zt) 
    
    return xt, yt, zt




def calcul_vect_repeteCLAVICULE(SC, AC , IJ, C7, PX, T8):
    # Convertir les points en numpy arrays pour calculer facilement les vecteurs
    SC = np.array(SC)
    AC = np.array(AC)
    IJ = np.array(IJ)
    C7 = np.array(C7)
    PX = np.array(PX)
    T8 = np.array(T8)

    zc = AC-SC
    
    #yt-----------------------------------
    M1 = point_milieu(IJ, C7)
    M2 = point_milieu(PX, T8)
    M1 = np.array(M1)
    M2 = np.array(M2)
    
    yt = M1-M2
    #-------------------------------------
    
    xc = np.cross(yt, zc)
    yc = np.cross(zc, xc)

    return xc, yc, zc





def calcul_vect_repeteSCAPULA(AA, TS, AI):
    # Convertir les points en numpy arrays pour calculer facilement les vecteurs
    AA = np.array(AA)
    TS = np.array(TS)
    AI = np.array(AI)
    
    
    zs = AA-TS
    
    u = AI-AA
    v = TS-AA

    xs = np.cross(u, v)
    ys = np.cross(zs, xs)
    
    return xs, ys, zs




def calcul_vect_repeteHUMERUS(GH, EL, EM):
    # Convertir les points en numpy arrays pour calculer facilement les vecteurs
    GH = np.array(GH)
    EL = np.array(EL)
    EM = np.array(EM)
    
    # Calcul des vecteurs
    M1 = point_milieu(EL, EM)
    M1 = np.array(M1)
    
    yh = GH-M1

    u = EL-GH
    v = EM-GH

    xh = np.cross(u, v)
    zh = np.cross(xh, yh)
    
    return xh, yh, zh




def calcul_vect_repeteAVANTBRAS(US, RS, EL, EM):
    # Convertir les points en numpy arrays pour calculer facilement les vecteurs
    US = np.array(US)
    RS = np.array(RS)
    EL = np.array(EL)
    EM = np.array(EM)
    
    
    M1 = point_milieu(EL, EM)
    M1 = np.array(M1)
    
    yf = M1-US
    
    u = M1-US
    v = RS-US
    
    xf = np.cross(u, v)
    zf = np.cross(xf, yf)
    
    return xf, yf, zf



#Récupération des points par la MOCAP

#thorax
IJ = [5, 10, 0]
C7 = [5, 10, -5]
PX = [5, 5, 0]
T8 = [5, 5, -5]

#clavicule
SC = [4, 10, 0]
AC = [0, 10, 0]

#scapula
AA = [0, 10, -3]
TS = [2, 10, -3]
AI = [2, 8, -3]

#humerus
GH = [0, 10, -2]
EL = [-3, 5, -2]
EM = [0, 5, -2]

#avant-bras
US = [0, 2, -2]
RS = [-3, 2, -2]


xt, yt, zt = calcul_vect_repeteTHORAX(IJ, C7, PX, T8)
xc, yc, zc = calcul_vect_repeteCLAVICULE(SC, AC , IJ, C7, PX, T8)
xs, ys, zs = calcul_vect_repeteSCAPULA(AA, TS, AI)
xh, yh, zh = calcul_vect_repeteHUMERUS(GH, EL, EM)
xf, yf, zf = calcul_vect_repeteAVANTBRAS(US, RS, EL, EM)


print("\nRepèreThorax")

print("xt :", xt)
print("yt :", yt)
print("zt :", zt)

print("\nRepèreClavicule")

print("xc :", xc)
print("yc :", yc)
print("zc :", zc)

print("\nRepèreScapula")

print("xs :", xs)
print("ys :", ys)
print("zs :", zs)


print("\nRepèreHumerus")

print("xh :", xh)
print("yh :", yh)
print("zh :", zh)


print("\nRepèreAvant-Bras")

print("xf :", xf)
print("yf :", yf)
print("zf :", zf)













