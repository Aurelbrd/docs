import PySimpleGUI as sg
import random as rdm


def premiere():
    """ Open the first window which displays the rules of the game and asks the players names
    :param None: None
    :param None: None
    :type None: None
    :type None: None
    :return: the names of the two players
    :retype: str, str
    
    """
    layout = [[sg.Text("règles")],
              [sg.Text("règles2")],
              [sg.Text("règles3")],
              [sg.Text("règles4")],
              [sg.Text("Entrez le pseudo du joueur 1"), sg.InputText()],
              [sg.Text("Entrez le pseudo du joueur 2"), sg.InputText()],
              [sg.Button('OK'), sg.Button('Annuler')]]
    window=sg.Window("Puissance 4", layout = layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Annuler':
            window.close()
            return "", ""
        elif event == "OK":
            window.close()
            return values[0], values[1]


def rotation(tab,sens):  #ajouter le nombre de repetitions? Pour l'instant Non
    """ Rotates by 90° an array 
    :param tab: 2d array
    :param sens: induces the side of the rotation : 0 => counterclockwise , 1 => clockwise
    :type tab: list
    :type sens: int
    :return: rotated array
    :retype: 2d list
    
    """
    L, C = len(tab), len(tab[0])
    newArr = [[None]*L for i in range(C)]
    if sens == 0: # counterclockwise
        for c in range(C):
            for l in range(L-1,-1,-1):
                newArr[C-c-1][l] = tab[l][c]
        return newArr
    elif sens == 1: # clockwise
        for c in range(C):
            for l in range(L-1,-1,-1):
                newArr[c][L-l-1] = tab[l][c]
        return newArr


def boardIniti(j1,j2):
    """ Creates the gameboard layout and a list wich contain the indices of the elements of the first array
    :param None: None
    :param None: None
    :type None: None
    :type None: None
    :return: two 7*7 list
    :retype: list, list
    
    """
    layout = [[sg.Button("   ", key=str(i)+str(j), size = ("4","2")) for j in range(7)] for i in range(7)]
    layout.append([[sg.Text("Score : ")],
                  [sg.Text(str(j1), size = (15,1), key = "J1"), sg.Text("0", key = "scorej1")],
                  [sg.Text(str(j2), size = (15,1), key = "J2"), sg.Text("0", key = "scorej2")]])#initialise le tableau avec les noms associés à la colonne et a la ligne 
    layout.insert(0,[sg.Text("Orientation : "), sg.Text("N", key = "ori")])
    arr = [[str(i)+str(j) for j in range(7)] for i in range(7)]
    return layout, arr
                    

def puissanceCorps(layout,arr):
    """ Creates the gameboard layout and a list wich contain the indices of the elements of the first array
    :param layout: the game board
    :param arr: a list that contains the indices of the game board
    :type None: 7*7 tab
    :type None: 7*7 tab
    :return: 
    :retype: list, list
    
    """
    window=sg.Window("Puissance 4", layout = layout)
    oripos = ["N","E","S","W"]
    current = 0
    turn = 0
    token = ["red", "yellow"]
    Jtoken = [30,30]

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "44":
            arr = rotation(arr,1) #variable locale qui prend toutes les valeurs du tableau
            for i in range(7):
                for j in range(7):
                    window[str(i)+str(j)].update(arr[i][j])
        for i in range(7):
            if event == str(1)+ str(i):
                for k in range(6):#verifier que c'est bien 6 et pas 7
                    if arr[i][k] == "":#trouver l'indice de la colonne
                        continue
                    else:
                        arr[i][k] = token[turn]
                        window[1 + str(i)].update(Text = token[turn])
                        Jtoken[turn] -= 1
                        if turn == 0:
                            turn = 1
                        else:
                            turn = 0
                        break
        
        nbOrientation = rdm.randint(1,3)
        Newarr = rotation(arr, nbOrientation) #dernière instruction du while True
        for i in range(7):
            for j in range(7):
                window[str(i)+str(j)].update(Newarr[i][j]) #erreur : 'NoneType' object is not subscriptable

        if nbOrientation == 1:
            window["ori"].update(oripos[(current+1)%4])
            current += 1
        elif nbOrientation == 2:
            window["ori"].update(oripos[(current+2)%4])
            current += 2
        elif nbOrientation == 3:
            window["ori"].update(oripos[(current+3)%4])
            current += 3


    window.close()


# L = [[1,2],[3,4]]
# print(L)
# print(Rotation(L,1))

# fonction qui tourne le tableau, prend en argument : un tableau, 1 ou 0 (1 => rotation sens horaire, 0=> rotation sens antihoraire) et le nombre de rotations souhaitées
# fonction Tomber qui déplace le pion vers le 'bas' prend la valeur de la colonne dans laquelle le pion est placée renvoie la ligne la plus basse libre de cette colonne
# Dans une première fenetre,
# Init qui demande les pseudos et setup le board avec liste (première case de la liste : total des points, les autres nb de coube/carré/triangle/puissance)
# Dans une deuxième fentre, 
# Game avec un while True et teste si le board est rempli ou si les deux joueurs n'ont plus de pions, finir le jeu, sinon
# Tourne le plateau avec random entre 1 et 4 et entre 0 et 1 dans Rotation
# si bouton joker pressé point -= 3 et faire apparaitre 2 boutons, rotation dans le sens horaire ou anti-horaire faire appel a rotation
# ajout du pion, puis tomber (au moins dans la colonne du pion)
# teste les différents patternes, si patterne détécté, ajouter le score equivalent dans la liste score puis retirer les pions qui le constituent et appliquer Tomber sur chacun des pions en partant des 'lignes les plus basses'

# Mettre toutes les initialisations des affichages dans une fonction Init
