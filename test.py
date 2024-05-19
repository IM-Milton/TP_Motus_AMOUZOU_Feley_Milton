from collections import Counter


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


fleurs = ['rose', 'tulipe', 'marguerite', 'lys', 'orchidée', 'jonquille', 'pivoine', 'lilas', 'hibiscus', 'bleuet']

print(inside('lys', fleurs)) # True

