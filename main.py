# -*- coding: utf-8 -*-
__author__ = 'Sarah , Manu'

from outils import *
import os

if __name__=="__main__":


    VILLE = {}
    VILLE['PARIS'] = [395,179]
    VILLE['LYON'] = [518,400]
    VILLE['MARSEILLE'] = [556,598]
    VILLE['LILLE'] = [412,49]
    VILLE['RENNES'] = [178,237]
    VILLE['STRASBOURG'] = [653,183]
    VILLE['NANTES'] = [172,292]
    VILLE['TOURS'] = [309,271]
    VILLE['BORDEAUX'] = [224,472]
    VILLE['MONTPELLIER'] = [464,568]
    VILLE['TOULOUSE'] = [334,569]
    VILLE['TOULON'] = [594,606]
    VILLE['NICE'] = [654,555]
    VILLE['CLERMONT-FERRAND'] = [421,397]
    VILLE['CHERBOURG'] = [188,118]
    VILLE['DUNKERQUE'] = [385,21]
    VILLE['ORLEANS'] = [370,245]
    VILLE['POITIERS'] = [268,332]
    VILLE['LIMOGES'] = [326,390]
    VILLE['LE HAVRE'] = [277,126]
    VILLE['ROUEN'] = [317,131]
    VILLE['BREST'] = [32,200]
    VILLE['SAINT-ETIENNE'] = [490,438]
    VILLE['GRENOBLE'] = [556,441]
    VILLE['AJACCIO'] = [631,701]
    VILLE['METZ'] = [582,152]
    VILLE['NANCY'] = [577,174]
    VILLE['DIJON'] = [534,287]
    VILLE['BESANCON'] = [585,288]
    VILLE['MULHOUSE']= [635, 260]

    listeVilles = []
    for key in VILLE.keys():
        listeVilles.append(key)
    #print(listeVilles)
    nombreVilles = len(listeVilles)
    villeEnCours = 0

    etatJeu = ETAT_JEU_DEPART


    x = 100
    y = 50
    pygame.init()

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
    pygame.display.set_caption("Titre !")
    SCREEN = pygame.display.set_mode((LARGEUR, HAUTEUR))

    compteurDelai = -1
    nombreVillesJustes = 0
    nombreVillesFausses = 0


    while True:
        SCREEN.fill(0)
        SCREEN.blit(IMAGE_CARTE,(5,5))

        if etatJeu == ETAT_JEU_BRAVO :
            compteurDelai+=1
            surface = FONT.render("Bravo !", True, VERT)
            rect = surface.get_rect(topleft=(700, 240))
            SCREEN.blit(surface, rect)
            pygame.draw.circle(SCREEN, VERT, VILLE[listeVilles[villeEnCours]], 7, 0)
        elif etatJeu == ETAT_JEU_PERDU:
            compteurDelai+=1
            surface = FONT.render("Perdu !", True, ROUGE)
            rect = surface.get_rect(topleft=(700, 240))
            SCREEN.blit(surface, rect)
            pygame.draw.circle(SCREEN, ROUGE, VILLE[listeVilles[villeEnCours]], 7, 0)
        elif etatJeu == ETAT_JEU_FINI:
            surface = FONT.render("Fini !", True, BLEU)
            rect = surface.get_rect(topleft=(700, 240))
            SCREEN.blit(surface, rect)
        elif etatJeu==ETAT_JEU_QUESTION:
            texte = "Où est: "
            texte = texte + listeVilles[villeEnCours]
            texte = texte + " ?"
            surface = FONT.render(texte, True, BLANC)
            rect = surface.get_rect(topleft=(700, 240))
            SCREEN.blit(surface, rect)

        texte = "Score : "+str(nombreVillesJustes)+"/"+str(nombreVillesFausses+nombreVillesJustes)
        surface = FONT.render(texte, True, JAUNE)
        rect = surface.get_rect(topleft=(700, 50))
        SCREEN.blit(surface, rect)



        if compteurDelai >DELAI_AFFICHAGE:
            compteurDelai=-1
            if villeEnCours<nombreVilles-1:
                villeEnCours +=1
                etatJeu = ETAT_JEU_QUESTION
            else:
                etatJeu = ETAT_JEU_FINI


        for event in pygame.event.get():
            #print (event)

            # un clic sur le X de fermeture de fenetre ?
            if event.type==pygame.QUIT:
                    pygame.quit()
                    exit(0)

            if event.type==pygame.KEYDOWN:
                #print(event.key)

                # Q
                if event.key==97:
                    pygame.quit()
                    exit(0)

                # Espace
                if event.key==32:
                    if etatJeu==ETAT_JEU_DEPART or etatJeu==ETAT_JEU_FINI:
                        villeEnCours=0
                        nombreVillesJustes = 0
                        nombreVillesFausses = 0
                        etatJeu=ETAT_JEU_QUESTION





            #if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #    print("click",x_souris,y_souris)


            if etatJeu == ETAT_JEU_QUESTION:
                # handle MOUSEBUTTONUP
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                    souris = pygame.mouse.get_pos()
                    x_souris = souris[0]
                    y_souris = souris[1]

                    #print("ville : ",listeVilles[villeEnCours])
                    #print("dico ville : ",VILLE[listeVilles[villeEnCours]])

                    x_ville = VILLE[listeVilles[villeEnCours]][0]
                    y_ville = VILLE[listeVilles[villeEnCours]][1]


                    if abs(x_souris-x_ville) < MARGE_DE_CLIQUE and abs(y_souris-y_ville) < MARGE_DE_CLIQUE:
                        etatJeu=ETAT_JEU_BRAVO
                        nombreVillesJustes +=1
                    else:
                        etatJeu=ETAT_JEU_PERDU
                        nombreVillesFausses +=1


            if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                print(pygame.mouse.get_pos())


        pygame.display.update()
        pygame.time.Clock().tick(FPS)