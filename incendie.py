################################################
#groupe DLBI
#Pauline HOSTI
#Rania SAIFI
#Adeline MOUTOU
#Clément MAOUCHE
#Maya SANTINI
#Nathan CARRE
#https://github.com/Nathan-Carre/projet_incendie
################################################

######LIBRAIRIES################################
import tkinter as tk
import random
################################################

######CONSTANTES################################
LARGEUR = 10;
HAUTEUR = 6;
################################################

######VARIABLES GLOBALES########################
################################################

######FONCTIONS################################
def generate_field():

    terrain = [];

    for line in range(HAUTEUR):
    
        # Si la line n'existe pas on l'ajoute 
        # Si le nombre de la line +1 > à la taille du tableau donc elle n'existe pas donc on ajoute la line
        # Exemple : si le tableau contient 5 lignes et qu'on est à la 6 ème 
        # il faut ajouter une ligne car elle n'existe pas dans le tableau
        if line + 1 > len(terrain):
            terrain.append([]);
            
        # Pour chaque ligne on les remplits de façon aléatoire
        for colonne in range(LARGEUR):
            
            # On prend un nombre aléatoire entre 0 et 1
            proba = random.random();
            
            if proba < 0.33:
                
                # Si la colonne n'existe pas dans la ligne on l'ajoute avec la bonne couleur
                if colonne + 1 > len(terrain[line]):
                    terrain[line].append('Blue');
                    
                # Si non si elle existe on change la couleur.
                else:
                    terrain[line][colonne] = 'Blue';
            elif proba < 0.66 and proba >= 0.33:
                if colonne + 1 > len(terrain[line]):
                    terrain[line].append('Green');
                else:
                    terrain[line][colonne] = 'Green';
            elif proba < 1 and proba >= 0.66:
                if colonne + 1 > len(terrain[line]):
                    terrain[line].append('Yellow');
                else:
                    terrain[line][colonne] = 'Yellow';
        
    return terrain;


def take_fire(line, column):
    if (terrain[line][column]=='Green' or terrain[line][column]=='Yellow') and line >= 0 and line <= HAUTEUR and column >= 0 and column <= LARGEUR:
        terrain[line][column]='Red'
        fenetre.grid_slaves(row=line, column=column)[0].configure( background = terrain[line][column])
    
def propagation(line, column):
    #####ca marche pas c'était juste une tentative/idée
    if terrain[line][column]=='Yellow' and (terrain[line+1][column]=='Red' or terrain[line][column+1]=='Red' or terrain[line-1][column]=='Red' or terrain[line][column-1]=='Red'):
        terrain[line][column]='Red'
        fenetre.grid_slaves(row=line, column=column)[0].configure( background = terrain[line][column])

def generate_windows():# Création d'une fenêtre avec la classe Tk :
    fenetre = tk.Tk()
    for l in range(HAUTEUR):
        for c in range(LARGEUR):
            tk.Button(fenetre, background= terrain[l][c], borderwidth=1, height=2, width=5, command = lambda line=l, column=c : take_fire(line, column)).grid(row=l,column=c)
    ##il faut trouver comment détruire la fenetre générée précedemment quand on en genere une nouvelle (.destroy?)
    return fenetre
###############################################

######PROGRAMME PRINCIPAL######################

terrain = generate_field()
fenetre = generate_windows()
conteneur = tk.Toplevel(bg="black")


bouton_terrain = tk.Button(conteneur, text="Génerer un terrain", command=generate_windows, fg = "black", bg="white", activebackground="black", activeforeground="white")
bouton_save = tk.Button(conteneur, text="Sauvegarder", fg = "black", bg="white", activebackground="black", activeforeground="white")
bouton_load = tk.Button(conteneur, text="Charger un fichier", fg = "black", bg="white", activebackground="black", activeforeground="white")
bouton_etape = tk.Button(conteneur, text="Prochaine étape", command=propagation, fg = "black", bg="white", activebackground="black", activeforeground="white")
bouton_begin = tk.Button(conteneur, text="Commencer la simulation", fg = "black", bg="white", activebackground="black", activeforeground="white")
bouton_stop = tk.Button(conteneur, text="Arrêter", fg = "black", bg="white", activebackground="black", activeforeground="white")

bouton_terrain.grid(row=1,column=0, columnspan=2)
bouton_save.grid(row=0,column=3)
bouton_load.grid(row=0,column=2)
bouton_etape.grid(row=0,column=1)
bouton_begin.grid(row=0,column=0)
bouton_stop.grid(row=1,column=2, columnspan=2)

fenetre.mainloop()

###############################################

#TEST Clément

#chocolat
#TEST Clément (è(_'-'((_ç"'-èè))))

#vanille
