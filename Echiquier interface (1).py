from tkinter import*        #Import de TKInter qui aidera à créer la partie graphique sur Canvas
import time                 #Import de Time pour avoir des repères temporels
#Definition des fonctions

def lignes():       #Création de la grille
    Cases = 5
    Pas = 500 / 5
    x = 0
    while x <= Cases:
        fond.create_line(0,Pas*x,500,Pas*x,fill='black')
        x=x+1
    y = 0
    while y <= Cases:
        fond.create_line(Pas*y,0,Pas*y,500,fill='black')
        y=y+1

def rectangle():    #Création des cases noirs/blanches
    nbrCNoir=1
    nbrCBlanc=0
    x0noir=100
    y0noir=0
    x0blanc=0
    y0blanc=0
    while nbrCNoir < 25:
        rectangle = fond.create_rectangle(x0noir, y0noir, x0noir+100, y0noir+100, fill='sienna4')
        nbrCNoir = nbrCNoir + 2
        i = int(nbrCNoir/5)
        j=nbrCNoir%5
        x0noir=j*100
        y0noir=i*100
    while nbrCBlanc < 25:
        rectangle = fond.create_rectangle(x0blanc, y0blanc, x0blanc+100, y0blanc+100, fill='burlywood1')
        nbrCBlanc = nbrCBlanc + 2
        i = int(nbrCBlanc/5)
        j=nbrCBlanc%5
        x0blanc=j*100
        y0blanc=i*100

def movement():     #Déplacement du cavalier et coloration cases déjà occupé
    global x        #w1 et v1 sont respectivement les mouvements à reproduire issues de la matrice de calcul, multiplié par 100 pour être transcrit en pixel
    w1 = 1
    v1 = 1
    if x < 24:   #Condition pour stopper la boucle au dernier mouvement
        w2 = w1     #w2 et v2 sont les variables qui pendant le run de la boucle permettront de garder la précédente valeur de w1 et v1
        v2 = v1
        p = listeabcisse[x] - listeabcisse[x+1]     #p est la différence entre la position actuelle, et la position du prochain coup
        m = listeordonnée[x] - listeordonnée[x+1]   #idem pour m, mais dans les ordonnées
        w1 = -p*100                                 #Multiplication par 100 car 1 dans l'algorithme = 1 case et 1 case = 100pixels
        v1 = -m*100
        fond.move(a, w1, v1,)                       #Commande mouvement (a = cavalier, w1 position abcisse, v1 position ordonnée)
        x = x + 1                                   #Compteur de la boucle(stop à 24)
        print (w1)
        print (v1)
        position = (fond.coords(a))                 #Variable qui a chaque loop va garder en mémoire la position du cavalier
        print (position)
        fond.create_image(position, image=couleurcase)      #On assigne ici à la position du cavalier un fond rougeatre pour marquer les cases occupées

    fond.after(2000,movement)










#Création de la fenêtre et du Canvas(Tkinter)

fenetre=Tk()
fenetre.title('Echiquier')
fenetre.geometry("500x500")     #définition du modèle de l'échiquier(ici 500x500pixels soit 5x5cases)
fond=Canvas(fenetre,width=500,height=500,bg='white')    #Création du Canvas
fond.pack()
lignes()    #Appel fonction créant les lignes
rectangle() #Appel fonction créant les rectangles
cavalier=Tk()
photo = PhotoImage(file = 'cavalier.png')     #Image du cavalier avec background transparent(esthétique)
couleurcase = PhotoImage(file = 'casetrans.png')
a = fond.create_image(50, 50, image=photo)
position = (fond.coords(a))
coloration = fond.create_image(position, image=couleurcase)
x = 0
listeabcisse = [1, 2, 1, 3, 5, 4, 5, 3, 1, 2, 4, 5, 3, 1, 2, 4, 5, 4, 2, 1, 3, 5, 4, 2, 3]
listeordonnée = [1, 3, 5, 4, 5, 3, 1, 2, 3, 5, 4, 2, 1, 2, 4, 5, 3, 1, 2, 4, 5, 4, 2, 1, 3]    #1 = 50 2 = 150 3 = 250 4 = 350 5 = 450 Trouver un if qui transforme chaque valeur de l'index





fond.after(2000,movement)

cavalier.mainloop()



fenetre.mainloop()


