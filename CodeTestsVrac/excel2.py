# -*- coding: utf-8 -*-
"""
Created on Fri May 10 14:04:34 2024

@author: leona
"""

import pandas as pd
import time

# Chemin vers votre fichier Excel
excel_file_path = 'test.xlsx'

# Charger le fichier Excel
df = pd.read_excel(excel_file_path)

# Obtenir le nombre total de lignes dans le DataFrame
total_rows = len(df)

# Itérer à travers les lignes et récupérer les valeurs chaque seconde
for i in range(total_rows):
    # Récupérer les valeurs de la ligne actuelle
    #row_values = df.iloc[i].values
    # Récupérer les chiffres de la deuxième ligne
    chiffres_ligne = df.iloc[i, 0].split(',') if pd.notnull(df.iloc[1, 0]) else []
    # Convertir les chiffres en entiers
    chiffres_ligne = [int(chiffre) for chiffre in chiffres_ligne]


    # Afficher les valeurs de la ligne
    print(f"Valeurs de la ligne {i+1}: {chiffres_ligne}")
    
    
    x1 = chiffres_ligne[8]
    print(x1)

    # Attendre une seconde avant de passer à la ligne suivante
    time.sleep(1)






'''
# Récupérer les chiffres de la deuxième ligne (index 1 dans pandas, correspondant à la ligne 2 dans Excel)
chiffres_deuxieme_ligne = df.iloc[1, 0].split(',') if pd.notnull(df.iloc[1, 0]) else []

# Récupérer les chiffres de la troisième ligne (index 2 dans pandas, correspondant à la ligne 3 dans Excel)
chiffres_troisieme_ligne = df.iloc[2, 0].split(',') if pd.notnull(df.iloc[2, 0]) else []

# Convertir les chiffres en entiers
chiffres_deuxieme_ligne = [int(chiffre) for chiffre in chiffres_deuxieme_ligne]
chiffres_troisieme_ligne = [int(chiffre) for chiffre in chiffres_troisieme_ligne]

# Afficher les chiffres de la deuxième ligne
print("Chiffres de la deuxième ligne:", chiffres_deuxieme_ligne)

# Afficher les chiffres de la troisième ligne
print("Chiffres de la troisième ligne:", chiffres_troisieme_ligne)

x1 = chiffres_deuxieme_ligne[8]
print(x1)
x1 = chiffres_troisieme_ligne[8]
print(x1)
'''