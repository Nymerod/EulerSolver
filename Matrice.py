ligne =[[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,2,3,4,3,2,0,0],
        [0,0,3,4,6,4,3,0,0],
        [0,0,4,6,8,6,4,0,0],
        [0,0,3,4,6,4,3,0,0],
        [0,0,2,3,4,3,2,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]
'''
La matrice représente un échiquier de taille 5x5,les 0 permettent d'eviter a
l'algorithme de partir "out of range" avec certain calcul présent dans la
suite de l'algorithme.
les valeurs de la matrice représentent le nombres de coups que peut faire le
cavalier quand il se trouve dans cette case.
'''

coupsJouer=0
caseDisponible = [0,0,0,0,0,0,0,0]#cette variable représente les case sur laquelle le cavalier peut se déplacer
a= 4
b= 4
posCavalier = [a,b]
boucle=0
while boucle!=1:
    caseDisponible[0] = ligne [a-2][b+1]
    caseDisponible[1] = ligne [a-1][b+2]
    caseDisponible[2] = ligne [a+1][b+2]
    caseDisponible[3] = ligne [a+2][b+1]
    caseDisponible[4] = ligne [a+2][b-1]
    caseDisponible[5] = ligne [a+1][b-2]
    caseDisponible[6] = ligne [a-1][b-2]
    caseDisponible[7] = ligne [a-2][b-1]
    print (posCavalier)
    print (caseDisponible)

    n=0
    i=0
    while n!=1:
        if caseDisponible[i]==0:
            i=i+1
        elif caseDisponible[i]==1:
            n=n+1
        elif caseDisponible[i]==2:
            n=n+1
        elif caseDisponible[i]==3:
            n=n+1
        elif caseDisponible[i]==4:
            n=n+1
        elif caseDisponible[i]==5:
            n=n+1
        elif caseDisponible[i]==6:
            n=n+1
        elif caseDisponible[i]==7:
            n=n+1
        elif caseDisponible[i]==8:
            n=n+1
            i=i+1





    x=caseDisponible[i]
    ditto=caseDisponible.count(x)#EN COURS  A NE PAS PRENDRE EN COMPTE
    print (ditto)






    ligne[a][b]=0
    if i==0:
        a=a-2
        b=b+1
    elif i==1:
        a=a-1
        b=b+2
    elif i==2:
        a=a+1
        b=b+2
    elif i==3:
        a=a+2
        b=b+1
    elif i==4:
        a=a+2
        b=b-1
    elif i==5:
        a=a+1
        b=b-2
    elif i==6:
        a=a-1
        b=b-2
    elif i==7:
        a=a-2
        b=b-1
    posCavalier=[a,b]
    j=0
    for j in range(0,8):
        if ligne[j][j]!=0:
            boucle=0
    coupsJouer=coupsJouer+1
    print(coupsJouer)
