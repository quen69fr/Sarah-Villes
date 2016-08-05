# -*- coding: utf-8 -*-
__author__ = 'Sarah , Manu'

import pygame


# SCREEN sera une "surface de dessin"
LARGEUR = 1300
HAUTEUR = 748

FPS = 60                 # nombre d'image par seconde
DELAY = 1               # vitesse du jeu

NOIR =  (  0,   0,   0)
BLANC = (255, 255, 255)
BLEU =  (  0,   0, 255)
VERT =  (  0, 255,   0)
ROUGE = (255,   0,   0)
JAUNE = (255, 255,   0)

# tous les fichiets IMAGES
IMAGE_CARTE = pygame.image.load("fond_carte_france.jpg")

MARGE_DE_CLIQUE = 10

pygame.font.init()
FONT = pygame.font.Font(None,30)

ETAT_JEU_DEPART = "DEPART"
ETAT_JEU_QUESTION = "QUESTION"
ETAT_JEU_BRAVO = "BRAVO"
ETAT_JEU_PERDU = "PERDU"
ETAT_JEU_FINI = "FINI"

DELAI_AFFICHAGE = 30
