from random import randint
import colorama 
colorama.init()
RED = colorama.Back.RED
GREEN = colorama.Back.GREEN
END = colorama.Back.RESET

def printRed(a):
    print(RED + a + END, end='')

def printGreen(a):
    print(GREEN + a + END, end='')

#Les fonctions
def StockageList():
    chemin = "scrabble.txt"
    liste =[]
    with open(chemin,"r") as f:
        contenu = f.read()
        liste = [mot.strip() for mot in contenu.split("\n") if 4 <= len(mot) <= 12] 
    return liste

def randomWord(dico):
    return dico[randint(0,len(dico)-1)]

def randomWord(dico, l):
    return dico[l][randint(0,len(dico[l])-1)]


def StockageDico(liste):
    dictionnaire = {}
    for i in range(len(liste)):
        taille = len(liste[i])
        if dictionnaire.get(taille) is None : 
            Liste = [liste[i]]
            dictionnaire[taille] = Liste
        else :
            dictionnaire[taille].append(liste[i])
    return dictionnaire

def inside(w ,lst):
    debut = 0
    fin = len(lst)-1
    taille = len(w)
    while debut <= fin:
        milieu = (debut + fin) // 2
        if lst[milieu] == w:
            return True
        if len(lst[milieu]) < taille:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return False

def verifyWord(w, dico):
    l = len(w)
    for i in dico[l]:
        if w == i:
            return True
    return False


def isValid(w , x, dico):
    l = len(x)
    if l == len(w) and verifyWord(w, dico) and w[0] == x[0]:
        return True
    return False

def partie(n):
    longueur = randint(4,12)
    mot = randomWord(Dico, longueur)
    print('Voici la longeur du mot à deviner',len(mot))
    print('Voici la premier lettre du mot à deviner',mot[0])
    etatPartie = False
    messagePartie = ''
    nEff = 0
    while(n > 0 and etatPartie == False):
        motUtilisateur = input('Veillez proposer un mot et fait attention à la longeur du mot :')
        if not isValid(motUtilisateur, mot, Dico):
            continue
        else:
            tableau = compare(motUtilisateur, mot)
            n -= 1
            nEff += 1
            print('Il vous reste', n, 'essai')
            print('Il vous avez fait', nEff, 'essai')
            printCompare(motUtilisateur ,tableau)
            print('\n')
            if n == 0:
                etatPartie = True
                messagePartie = 'Vous avez perdu'
                print(messagePartie)
                print('Le mot à deviner était', mot)
            if mot == motUtilisateur:
                etatPartie = True
                messagePartie = 'Vous avez gagné'
                print(messagePartie)
                print('Le mot à deviner était', mot)
    print('Fin de la partie')
    return 1


def updateWord(words, w, comp):
    Liste = []
    for i in words:
        if compare(w, i) == comp:
            Liste.append(i)
    return Liste

# le but de ce code est d'utiliser la liste comp pour trouver la solution de façon iterative
def partieNaive(x):
    n = 0 #Soit n le nombre de tentative effectué
    dico = StockageDico(StockageList())
    words =  dico[len(x)]# on part du principe que words est la liste de mots de longueur x qui se trouve dans le dictionnaire
    etatPartie = False
    #Construction de la variable comp
    comp = [2]
    for i in range(len(x) - 1):
        comp.append(1)

    for i in range(len(comp)):
        comp[i] = 2
        listeSolu = updateWord(words, x, comp)
        n += 1
    
    print('Le mot à deviner est', listeSolu[0])
    return n

def compare(w, x):
    tableau = []
    for i in range(len(w)):
        if w[i] == x[i]:
            tableau.append(2)
        elif w[i] != x[i]:
            tableau.append(1)
    return tableau


def printCompare(w, tableau):
    for i in range(len(tableau)):
        if tableau[i] == 1:
            printGreen(w[i])
        else:
            printRed(w[i])
    

#Partie code
Liste = StockageList()
Dico = StockageDico(Liste)
partie(5)
#print(partieNaive('rocker'))




