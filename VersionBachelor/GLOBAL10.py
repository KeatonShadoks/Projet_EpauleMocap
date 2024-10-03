# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 18:51:21 2024

@author: leona
"""


import math as mt
import matplotlib.pyplot as plt
import pandas as pd
import time
import tkinter as tk
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
import random
from PIL import Image, ImageTk
from moviepy.editor import VideoFileClip
import socket
import struct
import numpy as np
import pygame



    
fenetre = Tk()
fenetre.geometry('1000x500')
fenetre.title('Fenêtre Utilisateur (GLOBAL10)')
fenetre['bg']='white'
fenetre.resizable(height=True,width=True)


coteG = Canvas(fenetre, width="700",height="400",bg="aquamarine2")
coteG.pack(side=tk.LEFT, padx=0, pady=0)

#canvas = Canvas(coteG, width="600",height="200",bg="aquamarine2")
#canvas.place(x='0',y='0') #placement par rapport au canva maitre

root = Canvas(coteG, width="100",height="300")
root.place(x='250',y='320')
#root.pack()





#label
labelAngle = Label(root, text="Angle Maximal Accepté", fg='black')
labelAngle.pack()


#détermination de alpha
global ALPHA
ALPHA = IntVar()
entree = Entry(root, textvariable=ALPHA)
entree.pack()


angleG_var = tk.DoubleVar(value=0)
angleD_var = tk.DoubleVar(value=0)


new_window = None


#variables globales
r_globale = 170
alphaG = 90
B1x_globale = 220
B1y_globale = 120
B2x_globale = 485
B2y_globale = 120



#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
def normal_vector_from_points(p1, p2, p3):

    # Vecteurs formés par les points
    v1 = p2 - p1
    v2 = p3 - p1
    
    # Produit vectoriel de v1 et v2
    normal_vector = np.cross(v1, v2)
    
    return normal_vector


def projection_on_plane(v, n):

    #On vérifie que n n'est pas un vecteur nul
    #if np.linalg.norm(n) == 0:
        #raise ValueError("Le vecteur normal ne peut pas être le vecteur nul.")

    # Projection de v sur n (composante parallèle)
    v_parallel = (np.dot(v, n) / np.dot(n, n)) * n
    
    # Projection de v sur le plan (composante perpendiculaire)
    v_perpendicular = v - v_parallel
    
    return v_perpendicular



def angle_between_vectors(a, b):

    # Produit scalaire des vecteurs
    dot_product = np.dot(a, b)
    
    # Norme des vecteurs
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    
    # Calcul du cosinus de l'angle
    cos_theta = dot_product / (norm_a * norm_b)
    
    # Assurez-vous que la valeur est dans l'intervalle [-1, 1] pour éviter des erreurs numériques
    cos_theta = np.clip(cos_theta, -1.0, 1.0)
    
    # Calcul de l'angle en radians
    angle = np.arccos(cos_theta)
    
    # Convertir l'angle en degrés
    angle_degrees = np.degrees(angle)
    
    return angle_degrees

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------





def affichage_video():
    video_file = 'video1_1.mp4'
    clip = VideoFileClip(video_file)
    clip.preview()

    # Après la prévisualisation, fermer le clip
    clip.close()
    
    # Fermer Pygame pour s'assurer que toutes les fenêtres sont correctement fermées
    pygame.quit()



def stop_video():
    clip.close()
    pygame.quit()




#ouverture fenêtre patient
def open_new_window():
    global new_window
    if new_window and new_window.winfo_exists():
        new_window.deiconify()
        return

    # Créer une nouvelle fenêtre Toplevel
    new_window = tk.Toplevel(root)
    new_window.title("Fenêtre Patient")

    # Définir les dimensions de la nouvelle fenêtre
    new_window.geometry("1000x600")
    
    
    # Spécifier la taille du canevas
    canvas_width = 300
    canvas_height = 200

    # Charger l'image de fond
    image_path = "AnimationAvatar/shema6.png"  # Chemin vers votre image de fond
    image = Image.open(image_path)
    # Convertir l'image en PhotoImage pour tkinter
    photo = ImageTk.PhotoImage(image)

    new_window.avatar = tk.Canvas(new_window, width=image.width, height=image.height)
    new_window.avatar.pack()
    new_window.avatar.create_image(0, 0, image=photo, anchor=tk.NW)
    new_window.image = photo
    
        
    
    new_window.trig1 = new_window.avatar.create_polygon(0, 0, 0, 0, 0, 0, fill="chartreuse1", outline="black")
    new_window.trig2 = new_window.avatar.create_polygon(0, 0, 0, 0, 0, 0, fill="chartreuse1", outline="black")
    new_window.trig3 = new_window.avatar.create_polygon(0, 0, 0, 0, 0, 0, fill="chartreuse1", outline="black")
    new_window.trig4 = new_window.avatar.create_polygon(0, 0, 0, 0, 0, 0, fill="chartreuse1", outline="black")


    #variables globales
    r_globale = 170
    alphaG = 90
    BP1x_globale = 300
    BP1y_globale = 180
    BP2x_globale = 740
    BP2y_globale = 180
    deltaX1G = mt.cos(mt.radians(alphaG))*r_globale
    deltaY1G = mt.sin(mt.radians(alphaG))*r_globale
    BPGx = BP1x_globale-deltaX1G
    BPGy = BP1y_globale+deltaY1G

    alphaD = 90
    deltaX1D = mt.cos(mt.radians(alphaD))*r_globale
    deltaY1D = mt.sin(mt.radians(alphaD))*r_globale
    BPDx = BP2x_globale+deltaX1D
    BPDy = BP2y_globale+deltaY1D
    new_window.brasGaucheP_globale = new_window.avatar.create_line(BP1x_globale,BP1y_globale,BPGx,BPGy, width=20, fill="deeppink4")
    new_window.brasDroitP_globale = new_window.avatar.create_line(BP2x_globale,BP2y_globale,BPDx,BPDy, width=20, fill="deeppink4")
    
    new_window.avatar.create_oval(BP1x_globale-15,BP1y_globale-15,BP1x_globale+15,BP1y_globale+15, fill="deeppink4")
    new_window.avatar.create_oval(BP2x_globale-15,BP2y_globale-15,BP2x_globale+15,BP2y_globale+15, fill="deeppink4")
    

    # Ajouter un bouton pour lancer la vidéo
    close_button = tk.Button(new_window, text="Lancer la vidéo", command=affichage_video)
    close_button.pack(pady=10)

    # Ajouter un bouton de fermeture
    #close_button = tk.Button(new_window, text="Fermer la fenêtre", command=new_window.destroy)
    #close_button.pack(pady=10)



#fonction adaptant la taille de notre image à la taille du canvas
def resize_image(image_path, width, height):
    
    #Charger l'image depuis le chemin spécifié
    original_image = Image.open(image_path)

    #Redimensionner l'image à la taille spécifiée avec interpolation BILINEAR
    resized_image = original_image.resize((width, height), Image.BILINEAR)

    return resized_image



#On détermine la taille du nouveau canevas
canvas_width = 700
canvas_height = 350

#Chemin vers votre image de fond
image_path = "AnimationAvatar/shema5.png"

#Redimensionner l'image de fond
resized_image = resize_image(image_path, canvas_width, canvas_height)

#Convertir l'image redimensionnée en PhotoImage
photo = ImageTk.PhotoImage(resized_image)

#Créer un canevas avec la taille spécifiée
canvas = tk.Canvas(fenetre, width=canvas_width, height=canvas_height)
canvas.pack()

#Afficher l'image redimensionnée sur le canevas
canvas.create_image(0, 0, image=photo, anchor=tk.NW)





trig1 = canvas.create_polygon(0, 0, 0, 0, 0, 0, fill="chartreuse1", outline="blue")
trig2 = canvas.create_polygon(0, 0, 0, 0, 0, 0, fill="chartreuse1", outline="black")
trig3 = canvas.create_polygon(0, 0, 0, 0, 0, 0, fill="chartreuse1", outline="black")
trig4 = canvas.create_polygon(0, 0, 0, 0, 0, 0, fill="chartreuse1", outline="black")


labelAngleG = Label(fenetre, text="angleG", fg="black")
labelAngleG.pack()
labelAngleD = Label(fenetre, text="angleD", fg="black")
labelAngleD.pack()

labelFrame = Label(fenetre, text="frame", fg="black")
labelFrame.pack()


deltaX1G = mt.cos(mt.radians(alphaG))*r_globale
deltaY1G = mt.sin(mt.radians(alphaG))*r_globale
BGx = B1x_globale-deltaX1G
BGy = B1y_globale+deltaY1G

alphaD = 90
deltaX1D = mt.cos(mt.radians(alphaD))*r_globale
deltaY1D = mt.sin(mt.radians(alphaD))*r_globale
BDx = B2x_globale+deltaX1D
BDy = B2y_globale+deltaY1D
brasGauche_globale = canvas.create_line(B1x_globale,B1y_globale,BGx,BGy, width=20, fill="deeppink4")
brasDroit_globale = canvas.create_line(B2x_globale,B2y_globale,BDx,BDy, width=20, fill="deeppink4")



LiveRect = canvas.create_rectangle(0,0,700,350,width=20, outline = "grey")







#fonction qui récupère l'angle IN et dessinne les zones vertes permises sur le shéma
def changeTriangles():
    #print("changeTriangle")
    angle_degrees = ALPHA.get()
    # Convertir l'angle en radians
    angle_radians = mt.radians(angle_degrees)
    
    side_length = 190
    
    #----------------------------------------------------------------------------------------------
    #Mise à jour des triangles - fenêtre utilisateur
    x = B2x_globale
    y = B2y_globale
    
    delta = side_length * mt.tan(angle_radians)
    # Calculer les coordonnées des sommets du triangle en fonction de l'angle donné
    x1 = x
    y1 = y
    x2 = x + side_length
    y2 = y - delta
    x3 = x + side_length
    y3 = y + delta
    
    x4 = x + delta
    y4 = y + side_length
    x5 = x - delta
    
    x6 = B1x_globale
    x7 = x6 - side_length
    
    x9 = x6 - delta
    x10 = x6 + delta

    canvas.coords(trig1, x1, y1, x2, y2, x3, y3)
    canvas.coords(trig2, x1, y1, x4, y4, x5, y4)
    canvas.coords(trig3, x6, y, x7, y2, x7, y3)
    canvas.coords(trig4, x6, y, x9, y4, x10, y4)
    
    #canvas.itemconfig(LiveRect, outline="red")
    
    
    
    
    #----------------------------------------------------------------------------------------------
    # Mettre à jour des triangles - la fenêtre patient (si elle existe)
    if new_window and new_window.winfo_exists():
        #calculs
        side_lengthP = 190
        BP1x_globale = 300
        #BP1y_globale = 180
        BP2x_globale = 740
        BP2y_globale = 180
        
        xP = BP2x_globale
        yP = BP2y_globale
        
        #delta = side_lengthP * mt.tan(angle_radians)
        # Calculer les coordonnées des sommets du triangle en fonction de l'angle donné
        x1 = xP
        y1 = yP
        x2 = xP + side_lengthP
        y2 = yP - delta
        x3 = xP + side_lengthP
        y3 = yP + delta
        
        x4 = xP + delta
        y4 = yP + side_lengthP
        x5 = xP - delta
        
        x6 = BP1x_globale
        x7 = x6 - side_lengthP
        
        x9 = x6 - delta
        x10 = x6 + delta
        
        new_window.avatar.coords(new_window.trig1, x1, y1, x2, y2, x3, y3)
        new_window.avatar.coords(new_window.trig2, x1, y1, x4, y4, x5, y4)
        new_window.avatar.coords(new_window.trig3, x6, yP, x7, y2, x7, y3)
        new_window.avatar.coords(new_window.trig4, x6, yP, x9, y4, x10, y4)



boutonAlpha = Button(root, text="valider",command=changeTriangles)
boutonAlpha.pack()




#calcul de l'angle grâce au produit scalaire
def angle_between_points(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    ux, uy, uz = x2 - x1, y2 - y1, z2 - z1
    vx, vy, vz = x3 - x1, y3 - y1, z3 - z1

    dot_product = ux * vx + uy * vy + uz * vz
    norm_u = mt.sqrt(ux**2 + uy**2 + uz**2)
    norm_v = mt.sqrt(vx**2 + vy**2 + vz**2)

    cos_theta = dot_product / (norm_u * norm_v)
    angle_radians = mt.acos(cos_theta)
    angle_degrees = mt.degrees(angle_radians)
    
    return angle_degrees





def update_bras(*args):
    #récupération des angles mis à jour
    alphaG = float(angleG_var.get())
    alphaD = float(angleD_var.get())
    
    #----------------------------------------------------------------------------------------------
    #Mise à jour des bras - fenêtre utilisateur
    deltaX1G = mt.cos(mt.radians(alphaG))*r_globale
    deltaY1G = mt.sin(mt.radians(alphaG))*r_globale
    BGx = B1x_globale-deltaX1G
    BGy = B1y_globale+deltaY1G
    canvas.coords(brasGauche_globale,B1x_globale,B1y_globale,BGx,BGy)

    deltaX1D = mt.cos(mt.radians(alphaD))*r_globale
    deltaY1D = mt.sin(mt.radians(alphaD))*r_globale
    BDx = B2x_globale+deltaX1D
    BDy = B2y_globale+deltaY1D
    canvas.coords(brasDroit_globale,B2x_globale,B2y_globale,BDx,BDy)
    
    #----------------------------------------------------------------------------------------------
    #Mise à jour des bras - fenêtre patient
    BP1x_globale = 300
    BP1y_globale = 180
    BP2x_globale = 740
    BP2y_globale = 180
    deltaX1G = mt.cos(mt.radians(alphaG))*r_globale
    deltaY1G = mt.sin(mt.radians(alphaG))*r_globale
    BPGx = BP1x_globale-deltaX1G
    BPGy = BP1y_globale+deltaY1G

    deltaX1D = mt.cos(mt.radians(alphaD))*r_globale
    deltaY1D = mt.sin(mt.radians(alphaD))*r_globale
    BPDx = BP2x_globale+deltaX1D
    BPDy = BP2y_globale+deltaY1D
    
    #Mise à jour de la nouvelle fenêtre si elle est ouverte
    if new_window and new_window.winfo_exists():
        new_window.avatar.coords(new_window.brasGaucheP_globale, BP1x_globale,BP1y_globale,BPGx,BPGy)
        new_window.avatar.coords(new_window.brasDroitP_globale, BP2x_globale,BP2y_globale,BPDx,BPDy)
        
        



def calculate_angle():
    # Effectuez ici votre calcul complexe pour déterminer l'angle
    angleG = int(random.uniform(0,360))
    angleD = int(random.uniform(0,360))

    angleG_var.set(angleG)  # Met à jour la variable avec le nouvel angle
    angleD_var.set(angleD)




def MOCAPvalues():
    
    #on créer une boucle infinie
    while(1):
        print("MOCAPvalues")
        canvas.itemconfig(LiveRect, outline="red")
        #canvas.create_rectangle(0,0,700,350,width=20, outline = "grey")
        
        debutFct = time.time()
        
        #nombre de narkeurs d'intéret
        markerTot = 6
        Vector3 = struct.Struct( '<fff' )
        
        #initilisation des cinq points
        a = np.array([0.0, 0, 0])
        b = np.array([0.0, 0, 0])
        c = np.array([0.0, 0, 0])
        d = np.array([0.0, 0, 0])
        e = np.array([0.0, 0, 0])
        f = np.array([0.0, 0, 0])
        
        #liste de différents offsets pour différents modèles
        #offset = [31,43,55,67]#test
        #offset = [32,44,56,68]#markerset(4)
        #offset = [33,45,57,69]#skeleton(4)
        #offset = [36,24,48,60,72]#markerSet(5)
        #offset = [24,36,48,60,72]#markerSet2(5)
        offset = [24,36,48,60,72,84]#markerSet(6)

        #création de la matrice des positions vide (4x4)
        PosPoints = np.zeros((6,4))
        
        #création du socket de réception
        recoit_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        #liaison du socket en local au port 1519
        recoit_socket.bind(('localhost',1519))
        
        #récupération des données envoyées sur le port 1519
        data, addr = recoit_socket.recvfrom(64*1024)
    
        #vérification de ID du message
        message_id = int.from_bytes( data[0:2], byteorder='little',  signed=True )
        
        #si l'ID correspond => on parcourt les marqueurs et on enregistre leur position
        if message_id == 7:
            for marker in range(markerTot):
                print("Offset = ", offset[marker])
                pos = Vector3.unpack( data[offset[marker]:offset[marker]+12] )
                print( "\tPosition%2.0f : [%3.2f, %3.2f, %3.2f]"% (marker, pos[0], pos[1], pos[2] ))
                
                #enregistrement du point
                PosPoints[marker][0] = marker
                for i in range(3):
                    PosPoints[marker][i+1] = round(pos[i],2)                    
            print("PosPoints =", PosPoints)
             
            #définition des coordonnées des cinq points
            for i in range(len(a)):
                a[i] = PosPoints[3][i+1]
                
            for i in range(len(b)):
                b[i] = PosPoints[0][i+1]
                
            for i in range(len(c)):
                c[i] = PosPoints[5][i+1]
                
            for i in range(len(d)):
                d[i] = PosPoints[4][i+1]

            for i in range(len(e)):
                e[i] = PosPoints[1][i+1]
                
            for i in range(len(e)):
                f[i] = PosPoints[2][i+1]

            #print(a)
            #print(b)
            #print(c)

            #calcul vecteur normal A, B, C
            #normal = normal_vector_from_points(a, b, c)
            normal = np.array([1, 0, 0.0])
            #print(normal)
            
            #calcul vecteur BrasG
            #cm1 = (a+b)/2
            cm2 = (b+c)/2
            brasG = cm2-a
            #print(bras)
            #print(cm2)
            
            #calcul vecteur BrasD
            cm3 = (e+f)/2
            brasD = cm3-d
            
            #nT = c-cm1
            #print(nT)
            nT = np.array([0.0, 1, 0.0])
            
            #print("nT = ",nT)
            
            # Calcul de la projection (vect_B, vect_nT)
            BG_proj = projection_on_plane(brasG, nT)
            print("Projection de B_proj sur le plan :", BG_proj)
            
            # Calcul de la projection (vect_normal, vect_nT)
            n_proj = projection_on_plane(normal, nT)
            print("Projection de n_proj sur le plan :", n_proj)
            
            # Calcul de l'angle
            alphaG = 180 - angle_between_vectors(BG_proj, n_proj)
            print("Angle entre a et b (degrés) :", alphaG)
    

            # Calcul de la projection (vect_B, vect_nT)
            BD_proj = projection_on_plane(brasD, nT)
            print("Projection de B_proj sur le plan :", BD_proj)
            
            # Calcul de l'angle
            alphaD = angle_between_vectors(BD_proj, n_proj)
            print("Angle entre a et b (degrés) :", alphaD)



            '''
            #calcul des angles
            alphaG = 180 - angle_between_points(x1, y1, z1, x2, y2, z2, x3, y3, z3)
            print("alphaG : ",alphaG)
            alphaD = angle_between_points(x1, y1, z1, x2, y2, z2, x4, y4, z4)
            print("alphaD : ",alphaD)
            '''
            #mise à jour des variables avec le nouvel angle
            angleG_var.set(alphaG)  
            angleD_var.set(alphaD)
            
            
            #print(f"iter = {i}")
            #labelFrame.config(text=f"frame : {i}")
            alphaG = "{:.2f}".format(alphaG)
            labelAngleG.config(text=f"angleG : {alphaG}")
            alphaD = "{:.2f}".format(alphaD)
            labelAngleD.config(text=f"angleD : {alphaD}")
            
            

            
            #Mise a jour de la fenête
            fenetre.update()
            finFct = time.time()
            #Temps d'attente
            #time.sleep(0.05)
            temps = finFct - debutFct
            print("Temps = ",temps)



def Stop_MOCAPvalues():
    canvas.itemconfig(LiveRect, outline="grey")
    fenetre.mainloop()
    


#fonction principale
def main():
    
    # Ajouter un bouton qui ouvre une nouvelle fenêtre
    open_button = tk.Button(fenetre, text="Ouvrir Fenêtre Patient", command=open_new_window)
    open_button.pack(pady=20)
    
    # Ajouter un bouton qui lance la vidéo
    open_button = tk.Button(fenetre, text="Afficher vidéo", command=affichage_video)
    open_button.pack(pady=20)
    
    #détermination de alpha
    ALPHA = IntVar()
    #entree = Entry(fenetre, textvariable=ALPHA)
    #entree.pack()
    

    
    # Ajouter un bouton pour commencer la lecture des valeurs d'un Excel
    boutonAlpha = Button(fenetre, text="Get Values Excel",command=lambda: get_values())
    boutonAlpha.pack()
    
    # Ajouter un bouton pour commencer la MOCAP
    boutonGetMocap = Button(fenetre, text="Get MOCAP Values",command=lambda: MOCAPvalues())
    boutonGetMocap.pack()
    
    # Ajouter un bouton pour arrêter la MOCAP
    boutonStopMocap = Button(fenetre, text="STOP MOCAP Values",command=lambda: Stop_MOCAPvalues())
    boutonStopMocap.pack()
    
    # Ajouter un bouton pour vérifier la sychronisation des deux fenêtres
    calc_button = tk.Button(fenetre, text="Test Sychronisation Fenêtres", command=calculate_angle)
    calc_button.pack()
    
    # Ajouter un bouton pour stopper la vidéo
    stopVideo_button = tk.Button(fenetre, text="Arrêter la vidéo", command=stop_video)
    stopVideo_button.pack()
    
    

    
    
    #création des points-épaules
    canvas.create_oval(B1x_globale-15,B1y_globale-15,B1x_globale+15,B1y_globale+15, fill="deeppink4")
    canvas.create_oval(B2x_globale-15,B2y_globale-15,B2x_globale+15,B2y_globale+15, fill="deeppink4")
    canvas.place(x='0',y='0') #placement par rapport au canva maitre
    
    
    
    angleG_var.trace("w",update_bras)
    angleD_var.trace("w",update_bras)
    
    
    fenetre.mainloop()
    
    

if __name__ == "__main__":
    main()
    
        
        
    


