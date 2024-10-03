# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 16:59:40 2024

@author: leona
"""

#Ne pas oublier d'installer la bibliothèque: pip install NatNetClient



from NatNetClient import NatNetClient

def on_frame_received(data, client, info):
    # Récupérer les données des marqueurs
    if 'markers' in data:
        for marker in data['markers']:
            print("ID:", marker['id'], "Position:", marker['position'])

# Créer un client NatNet
client = NatNetClient()

# Connecter le client à l'adresse IP du serveur OptiTrack
client.newFrameListener = on_frame_received
client.run()  # Démarre l'écoute des trames


